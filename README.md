---
language:
- ar
license: cc-by-4.0
task_categories:
- text-classification
- text-generation
- question-answering
tags:
- legal
- uae
- law
- arabic-nlp
- university-of-dubai
pretty_name: UAE Arabic Legal Text Corpus
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*.jsonl
---

<div align="center">

[![University of Dubai](https://img.shields.io/badge/University%20of%20Dubai-Research-004d40?style=for-the-badge&logo=university)](https://ud.ac.ae)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-FFD21E?style=for-the-badge)](https://huggingface.co/datasets/University-of-Dubai/arabic-legal-text)
[![License](https://img.shields.io/badge/License-CC--BY--4.0-blue?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)
[![Language](https://img.shields.io/badge/Language-Arabic-green?style=for-the-badge)](https://huggingface.co/languages/ar)

</div>

# UAE Arabic Legal Text Corpus

## Dataset Description

This repository contains a curated corpus of **United Arab Emirates (UAE) legal texts**, structured specifically for Natural Language Processing (NLP) tasks. The dataset is maintained by the **University of Dubai** to support research in Arabic legal intelligence, automated summarization, and retrieval-augmented generation (RAG).

* **Curated by:** University of Dubai IT Services & BuildingTHEITGUY
* **Language:** Arabic (Modern Standard / Legal)
* **License:** CC-BY-4.0
* **Repository:** [GitHub: University-of-Dubai-Research/arabic-legal-text](https://github.com/University-of-Dubai-Research/arabic-legal-text)

### Supported Tasks
* **Legal Text Classification:** Categorizing texts into Civil, Criminal, Commercial, etc.
* **Legal Information Retrieval:** Building search engines for UAE laws.
* **Language Modeling:** Fine-tuning LLMs on domain-specific Arabic legal terminology.

---

## Dataset Structure

The dataset is formatted in **JSON Lines (JSONL)**. Each line represents a distinct legal article or provision.

### Data Fields
* `text`: The content of the legal article/provision.
* `source`: The name of the law or decree (e.g., "UAE Federal Decree-Law No. 34").
* `year`: The year of issuance.
* `category`: The domain of law (e.g., "Cybersecurity", "Penal", "Labor").

### Example Instance
```json
{
  "text": "تسري أحكام هذا القانون على جرائم تقنية المعلومات...",
  "source": "UAE Federal Decree-Law No. 34 on Rumors and Cybercrimes",
  "category": "Cybersecurity",
  "year": 2026
}
