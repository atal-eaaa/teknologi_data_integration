import os
import platform
import shutil
import subprocess
import sys

print("\n\n")
print("Python installation")
print(f"Version: {sys.version}")
print(f"Executable: {sys.executable}")
print(f"Platform: {platform.platform()}")

print("\nEnvironment")
print(f"Current directory: {os.getcwd()}")
print(f"Virtual environment: {os.environ.get('VIRTUAL_ENV', 'None')}")

print("\nGit installation")
git_path = shutil.which("git")

if git_path:
    print(f"Git executable: {git_path}")
    result = subprocess.run(
        ["git", "--version"],
        capture_output=True,
        text=True,
        check=False
    )
    print(result.stdout.strip())
else:
    print("Git is not installed or is not available in PATH.")

print("\nJupyter kernels")
jupyter_path = shutil.which("jupyter")

if jupyter_path:
    print(f"Jupyter executable: {jupyter_path}")
    result = subprocess.run(
        ["jupyter", "kernelspec", "list"],
        capture_output=True,
        text=True,
        check=False
    )
    print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip())
else:
    print("Jupyter is not installed or is not available in PATH.")

print("\n\n")