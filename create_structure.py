from pathlib import Path

# Project root: folder containing this script
root_dir = Path(__file__).parent

# Directories to create
folders = [
    "backend",
    "notebooks",
]

# Files to create
files = [
    "backend/main.py",
    "backend/predictor.py",
    "backend/schemas.py",
    "requirement.txt",
    "notebooks/Laptop Price Predictor.ipynb"
]

# Create directories
for folder in folders:
    (root_dir / folder).mkdir(parents=True, exist_ok=True)

# Create files without overwriting existing content
for file in files:
    (root_dir / file).touch(exist_ok=True)

print("Project structure created successfully!")