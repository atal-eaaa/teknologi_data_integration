import subprocess
import shutil
import sys
import os

def get_git_version():
    # Try to find git in PATH first
    git_path = shutil.which("git")

    # If not found, try common installation paths
    if not git_path:
        possible_paths = [
            r"C:\Program Files\Git\bin\git.exe",  # Windows default
            r"C:\Program Files (x86)\Git\bin\git.exe",
            "/usr/bin/git",                      # Linux default
            "/usr/local/bin/git",                 # macOS/Linux
            "/opt/homebrew/bin/git"               # macOS (Apple Silicon)
        ]
        for path in possible_paths:
            if os.path.exists(path):
                git_path = path
                break

    if not git_path:
        return None  # Git not found

    try:
        # Run 'git --version'
        result = subprocess.run(
            [git_path, "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        # Extract only the version number
        return result.stdout.strip().split()[-1]
    except subprocess.CalledProcessError:
        return None

if __name__ == "__main__":
    version = get_git_version()
    if version:
        print(f"Installed Git version: {version}")
    else:
        print("Git is not installed or could not be found.")
