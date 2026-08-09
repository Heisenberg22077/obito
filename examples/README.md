# Reference Examples & Notebooks

This directory contains reference implementations and Jupyter notebooks for key concepts in the Data Science & AI Roadmap.

## 📚 Contents

### Module 1: Python Programming
- `m1_phase_project.py` - Example CLI project demonstrating file I/O, APIs, and testing
- `m1_data_processing.ipynb` - Pandas basics with real dataset examples

### Module 9: Classical Machine Learning
- `m9_logistic_regression_scratch.py` - Logistic regression from scratch with NumPy
- `m9_ml_pipeline_template.py` - Reusable scikit-learn pipeline template

### Module 21: RAG & Vector Databases
- `m21_rag_minimal.py` - Minimal RAG implementation with sentence transformers
- `m21_evaluation_harness.py` - RAG evaluation metrics and testing

### Module 24: MLOps & Production
- `m24_project_template/` - Complete project structure with tests, Docker, CI/CD
- `m24_monitoring_example.py` - Model monitoring with drift detection

## 🎯 How to Use

1. **Study first**: Read the corresponding module in the main curriculum
2. **Run examples**: Execute notebooks locally or in Colab
3. **Modify**: Adapt code for your own projects
4. **Build**: Use templates as starting points for portfolio projects

## 📦 Requirements

```bash
pip install jupyter numpy pandas scikit-learn matplotlib pytest docker
```

For module-specific requirements, see individual notebook headers.

## 🔧 Contributing Examples

When contributing example code:

1. **Keep it minimal**: Focus on one concept per example
2. **Add tests**: Include pytest tests for core functionality
3. **Document**: Clear docstrings and comments
4. **Test data**: Use small, included datasets or public APIs
5. **Reproducibility**: Pin versions and set random seeds

---

*Examples are educational references, not production code. Always adapt for your specific use case.*
