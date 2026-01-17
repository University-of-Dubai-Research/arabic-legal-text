# Contributing to the UAE Arabic Legal Text Corpus

Thank you for your interest in contributing to the **University of Dubai** open-science initiative. This dataset is a shared resource for the academic and research community, aimed at advancing Arabic NLP and Legal Intelligence.

To maintain the high quality required for scientific research (and to ensure our automation pipeline works), please follow these governance guidelines.

---

## 1. The "Golden Rule" of Data

**Do not break the schema.**

Our automation scripts expect strict **JSON Lines (JSONL)** formatting. If you upload a broken JSON file, the pipeline to Hugging Face will fail.

### The Required Schema

Every entry must be a valid JSON object on a single line with these four fields:

```json
{
  "text": "The full Arabic text of the article. Cleaned of headers/footers.",
  "source": "Official Name of the Law (e.g., UAE Federal Decree-Law No. 34)",
  "year": 2026,
  "category": "One of: Civil, Criminal, Commercial, Labor, Cybersecurity, Family"
}
```

---

## 2. Contribution Workflow (The GitHub Flow)

We follow standard open-source practices. Please do not commit directly to the `main` branch.

### Step 1: Fork and Clone

1. Fork this repository to your personal account.
2. Clone it to your local machine.

### Step 2: Create a Branch

Create a branch for your specific contribution. Use a descriptive name:

```bash
git checkout -b data/penal-code-2026
```

### Step 3: Add Your Data

1. Place your new `.jsonl` file in the `data/` folder.
2. **File Naming Convention:** `law_name_year.jsonl` (e.g., `cybercrime_law_2026.jsonl`).
3. Ensure your JSON is valid (use a linter if possible).

### Step 4: Push and Pull Request

1. Push your branch to your fork.
2. Open a Pull Request (PR) against our `main` branch.
3. In the PR description, explicitly state the source of the data (e.g., "Scraped from UAE Legislation Portal" or "Converted from Ministry PDF").

---

## 3. Data Quality Standards

* **Language:** Arabic Only. Please remove English translations if they exist in the same document.
* **Cleaning:** Remove page numbers, headers, and footers from the `text` field.
* **Privacy:** Ensure no PII (Personally Identifiable Information) is included (e.g., names of real people in court case examples). This corpus is for laws, not court verdicts.

---

## 4. Code of Conduct

As a University of Dubai project, we adhere to high standards of academic integrity.

* Do not upload data you do not have the right to distribute (though UAE Laws are generally public domain, verify first).
* Be respectful in Pull Request comments and reviews.

---

## Questions?

Contact the maintainers by opening an [Issue](https://github.com/University-of-Dubai-Research/arabic-legal-text/issues) in this repository.
