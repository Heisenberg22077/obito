#!/usr/bin/env python3
"""
Automated link checker for Data Science & AI Roadmap repository.
Checks all URLs in Markdown files and reports broken links.
"""

import os
import re
import sys
import time
import requests
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
MAX_WORKERS = 10
TIMEOUT = 15
USER_AGENT = "Mozilla/5.0 (compatible; LinkChecker/1.0; +https://github.com/your-repo)"
IGNORE_PATTERNS = [
    r'^mailto:',
    r'^tel:',
    r'^#',  # Internal anchors
    r'^\{%',  # Jekyll templates
    r'^\{\{',  # Liquid templates
]

# Status classification
def classify_status(status_code):
    if status_code is None:
        return "FAIL"
    if 200 <= status_code < 400:
        return "PASS"
    if status_code in [401, 403, 405, 429]:
        return "WARN"
    return "FAIL"

def extract_urls_from_file(filepath):
    """Extract all URLs from a Markdown file."""
    url_pattern = re.compile(
        r'(https?://[^\s<>"{}|\\^`\[\]]+)',
        re.IGNORECASE
    )
    
    urls = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = url_pattern.findall(content)
            for url in matches:
                # Clean trailing punctuation
                url = url.rstrip('.,;:!?)">')
                if not any(re.match(pattern, url) for pattern in IGNORE_PATTERNS):
                    urls.add(url)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return urls

def check_url(url):
    """Check a single URL and return status."""
    try:
        headers = {'User-Agent': USER_AGENT}
        response = requests.head(url, headers=headers, timeout=TIMEOUT, allow_redirects=True)
        return url, response.status_code
    except requests.exceptions.RequestException:
        try:
            # Fallback to GET if HEAD fails
            response = requests.get(url, headers=headers, timeout=TIMEOUT, stream=True)
            return url, response.status_code
        except requests.exceptions.RequestException:
            return url, None

def main():
    workspace = Path('/workspace')
    markdown_files = list(workspace.rglob('*.md'))
    
    all_urls = {}
    for md_file in markdown_files:
        urls = extract_urls_from_file(md_file)
        for url in urls:
            if url not in all_urls:
                all_urls[url] = []
            all_urls[url].append(str(md_file.relative_to(workspace)))
    
    print(f"Found {len(all_urls)} unique URLs in {len(markdown_files)} Markdown files")
    print(f"Checking links at {datetime.now().isoformat()}...\n")
    
    results = {'PASS': [], 'WARN': [], 'FAIL': []}
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(check_url, url): url for url in all_urls.keys()}
        
        completed = 0
        for future in as_completed(futures):
            url, status_code = future.result()
            status = classify_status(status_code)
            results[status].append((url, status_code, all_urls[url]))
            
            completed += 1
            if completed % 50 == 0:
                print(f"Checked {completed}/{len(all_urls)} URLs...")
            
            # Rate limiting
            time.sleep(0.1)
    
    # Generate report
    output_dir = Path('/workspace/.github/outputs')
    output_dir.mkdir(exist_ok=True)
    
    report_file = output_dir / 'broken_links.md'
    summary_file = output_dir / 'link_check_summary.txt'
    
    # Write detailed report for broken links
    with open(report_file, 'w') as f:
        f.write("# Broken Links Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- ✅ PASS: {len(results['PASS'])}\n")
        f.write(f"- ⚠️ WARN: {len(results['WARN'])}\n")
        f.write(f"- ❌ FAIL: {len(results['FAIL'])}\n\n")
        
        if results['FAIL']:
            f.write("## Failed Links (Action Required)\n\n")
            for url, status, files in sorted(results['FAIL']):
                f.write(f"### ❌ {url}\n")
                f.write(f"**Status Code:** {status or 'Connection Error'}\n")
                f.write(f"**Found in:**\n")
                for file in files:
                    f.write(f"- `{file}`\n")
                f.write("\n---\n\n")
        
        if results['WARN']:
            f.write("## Warning Links (Manual Review)\n\n")
            for url, status, files in sorted(results['WARN']):
                f.write(f"### ⚠️ {url}\n")
                f.write(f"**Status Code:** {status}\n")
                f.write(f"**Found in:**\n")
                for file in files:
                    f.write(f"- `{file}`\n")
                f.write("\n---\n\n")
    
    # Write summary for CI
    with open(summary_file, 'w') as f:
        f.write(f"Link Check Summary - {datetime.now().isoformat()}\n")
        f.write("=" * 50 + "\n")
        f.write(f"Total URLs: {len(all_urls)}\n")
        f.write(f"✅ PASS: {len(results['PASS'])}\n")
        f.write(f"⚠️ WARN: {len(results['WARN'])}\n")
        f.write(f"❌ FAIL: {len(results['FAIL'])}\n")
        
        if results['FAIL']:
            f.write("\nFAILED LINKS:\n")
            for url, status, _ in results['FAIL']:
                f.write(f"  [{status or 'ERROR'}] {url}\n")
            sys.exit(1)
        else:
            print("\n✅ All links are accessible!")
            sys.exit(0)

if __name__ == '__main__':
    main()
