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

[![University of Dubai](https://img.shields.io/badge/University%20of%20Dubai-Research-004d40?style=for-the-badge)](https://ud.ac.ae)
[![🤗 Hugging Face Dataset](https://img.shields.io/badge/Hugging%20Face-Dataset-FFD21E?style=for-the-badge)](https://huggingface.co/datasets/University-of-Dubai/arabic-legal-text)
[![License](https://img.shields.io/badge/License-CC--BY--4.0-blue?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)
[![Language](https://img.shields.io/badge/Language-Arabic-green?style=for-the-badge)](https://huggingface.co/languages/ar)

</div>

# UAE Arabic Legal Text Corpus

## Dataset Description

This repository contains a curated corpus of **United Arab Emirates (UAE) legal texts**, structured specifically for **Natural Language Processing (NLP)** tasks.

The dataset is maintained by **University of Dubai Research** to support research in:

- Arabic legal intelligence  
- Automated summarization  
- Retrieval-Augmented Generation (RAG)  
- Legal information systems  

### Key Information

- **Curated by:** Mohamed Asath (BuildingTHEITGUY) & University of Dubai Research  
- **Language:** Arabic (Modern Standard / Legal)  
- **License:** Creative Commons Attribution 4.0 (CC BY 4.0)  
- **Repository:**  
  https://github.com/University-of-Dubai-Research/arabic-legal-text  

---

## Supported Tasks

- **Legal Text Classification**  
  Categorizing texts into Civil, Criminal, Commercial, Labor, Cybersecurity, etc.

- **Legal Information Retrieval**  
  Building search and semantic retrieval systems for UAE laws.

- **Language Modeling**  
  Fine-tuning Large Language Models (LLMs) on domain-specific Arabic legal terminology.

---

## Dataset Structure

The dataset is formatted using **JSON Lines (JSONL)**.  
Each line represents a distinct legal article or provision.

### Data Fields

- `text` — Full content of the legal article or provision  
- `source` — Name of the law or decree  
- `year` — Year of issuance  
- `category` — Legal domain (e.g., Cybersecurity, Penal, Labor)

---

### Example Instance

```json
{
  "text": "تسري أحكام هذا القانون على جرائم تقنية المعلومات...",
  "source": "UAE Federal Decree-Law No. 34 on Rumors and Cybercrimes",
  "category": "Cybersecurity",
  "year": 2026
}
```

---

## Usage
You can load this dataset directly in Python using the Hugging Face datasets library:

```python
from datasets import load_dataset

dataset = load_dataset("University-of-Dubai/arabic-legal-text")

# Print the first example
print(dataset['train'][0])
```

---

## Citation
If you use this dataset in your research or academic work, please cite it as follows:

```bibtex
@dataset{university_of_dubai_arabic_legal_2026,
  author    = {Asath, Mohamed and University of Dubai},
  title     = {UAE Arabic Legal Text Corpus},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/University-of-Dubai/arabic-legal-text}
}
```

---

## Contribution & Governance
This dataset is managed via GitHub to ensure version control and academic integrity.

**Faculty/Researchers:** Please push your data updates to the GitHub Repository.

**Automation:** Changes on GitHub are automatically validated and synced to Hugging Face.

---

## Contributors
* **Mohamed Asath** (Lead Maintainer)
* [Future Faculty contributors can be added here]
