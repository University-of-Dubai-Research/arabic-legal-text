import os
from huggingface_hub import HfApi, upload_folder

# Configuration
# This points to your Hugging Face dataset
HF_REPO_ID = "University-of-Dubai/arabic-legal-text" 
DATA_FOLDER = "data" 

def sync_hub():
    print(f"[INFO] Starting sync to Hugging Face: {HF_REPO_ID}")
    
    # Get the token from GitHub Secrets
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        # If this fails, it means the Secret wasn't added correctly
        print("[ERROR] HF_TOKEN is missing. Check GitHub Secrets.")
        return

    api = HfApi()

    # 1. Upload the 'data' folder content
    upload_folder(
        folder_path=DATA_FOLDER,
        path_in_repo="data", 
        repo_id=HF_REPO_ID,
        repo_type="dataset",
        token=hf_token,
        commit_message=f"Sync from GitHub: {os.environ.get('GITHUB_SHA', 'Manual Update')[:7]}"
    )
    
    # 2. Upload the README (to keep the citation and metadata in sync)
    api.upload_file(
        path_or_fileobj="README.md",
        path_in_repo="README.md",
        repo_id=HF_REPO_ID,
        repo_type="dataset",
        token=hf_token
    )
    
    print("[SUCCESS] Sync complete! Check your Hugging Face repo.")

if __name__ == "__main__":
    sync_hub()
