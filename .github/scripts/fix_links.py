#!/usr/bin/env python3
"""
Helper script to identify and suggest fixes for broken links.
"""

import re
from pathlib import Path

# Known URL mappings (old -> new)
URL_FIXES = {
    # MIT OCW - Linear Algebra
    'https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/exams/': 
        'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/',
    
    # IITM Data Science
    'https://study.iitm.ac.in/ds/course_pages/BSCS3003.html':
        'https://onlinedegree.iitm.ac.in/data-science',
    
    # Elements of Statistical Learning
    'https://hastie.su.domains/ElemStatLearn/':
        'https://hastie.su.domains/ElemStatLearn/print_pages/TISL.pdf',
    
    # Inference book
    'https://www.inference.org.uk/itila/':
        'https://www.inference.org.uk/mackay/itila/book.html',
    
    # Princeton COS597G
    'https://www.cs.princeton.edu/courses/archive/fall22/cos597G/':
        'https://www.cs.princeton.edu/courses/archive/fall23/cos597G/',
}

def find_urls_in_file(filepath):
    """Extract URLs with their context from a Markdown file."""
    url_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)', re.IGNORECASE)
    results = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines, 1):
                matches = url_pattern.findall(line)
                for text, url in matches:
                    if url.startswith('http'):
                        results.append({
                            'file': str(filepath),
                            'line': line_num,
                            'text': text,
                            'url': url.rstrip(')**'),
                            'context': line.strip()
                        })
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    return results

def main():
    workspace = Path('/workspace')
    markdown_files = list(workspace.rglob('*.md'))
    
    all_urls = []
    for md_file in markdown_files:
        urls = find_urls_in_file(md_file)
        all_urls.extend(urls)
    
    print("🔍 URLs that need fixing:\n")
    
    for url_info in all_urls:
        url = url_info['url']
        if url in URL_FIXES:
            print(f"📁 File: {url_info['file']}:{url_info['line']}")
            print(f"   Text: {url_info['text']}")
            print(f"   ❌ Old: {url}")
            print(f"   ✅ New: {URL_FIXES[url]}")
            print(f"   Context: {url_info['context'][:80]}...")
            print()

if __name__ == '__main__':
    main()
