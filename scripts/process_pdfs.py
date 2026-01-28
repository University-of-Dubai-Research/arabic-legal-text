import os
import json
import pdfplumber
import re

# CONFIGURATION
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FOLDER = os.path.join(BASE_DIR, "raw_pdfs")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "batch_import.jsonl")

def clean_text(text):
    if not text: return ""
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def process_pdfs():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    print(f"🚀 Checking {INPUT_FOLDER}...")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        for filename in os.listdir(INPUT_FOLDER):
            if filename.endswith(".pdf"):
                path = os.path.join(INPUT_FOLDER, filename)
                print(f"Processing: {filename}")
                
                try:
                    with pdfplumber.open(path) as pdf:
                        full_text = ""
                        for page in pdf.pages:
                            txt = page.extract_text()
                            if txt: full_text += txt + " "
                        
                        # Write to JSONL
                        entry = {"text": clean_text(full_text), "source": filename, "year": 2026}
                        f_out.write(json.dumps(entry, ensure_ascii=False) + "\n")
                except Exception as e:
                    print(f"Error: {e}")

    print("✅ Done! Data saved to data/batch_import.jsonl")

if __name__ == "__main__":
    process_pdfs()