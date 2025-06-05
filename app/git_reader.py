import os

def extract_repo_info(repo_path):
    readme = ""
    for fname in ["README.md", "readme.md"]:
        try:
            with open(os.path.join(repo_path, fname), "r") as f:
                readme = f.read()
        except FileNotFoundError:
            continue
    return {
        "readme": readme
    }