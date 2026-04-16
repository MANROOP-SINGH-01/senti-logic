import os
import sys
import subprocess
import json

REQUIRED_DIRS = ['data', 'scripts', 'assets', 'docs', 'outputs', 'dashboard', 'notebooks']
REQUIRED_FILES = {
    'data/letter_frequency_en_US.csv': 'Linguistic baseline for Chi-Square test.',
    'requirements.txt': 'Project dependency list.',
    'outputs/research_logs.json': 'Live Evidence Source of Truth.'
}

DATA_SOURCES = {
    'Sentiment140': 'data/training.1600000.processed.noemoticon.csv',
    'GloVe': 'data/glove.6B.300d.txt'
}

def check_structure():
    print("[SYSTEM] Checking workspace integrity...")
    missing_dirs = [d for d in REQUIRED_DIRS if not os.path.exists(d)]
    if missing_dirs:
        print(f"[!] Missing directories: {missing_dirs}")
        for d in missing_dirs:
            os.makedirs(d)
            print(f"    Created: {d}")
    else:
        print("[OK] All structural layers verified.")

def check_files():
    print("\n[SYSTEM] Verifying critical evidence files...")
    for file, desc in REQUIRED_FILES.items():
        if os.path.exists(file):
            print(f"[OK] Found {file} ({desc})")
        else:
            print(f"[ERROR] Missing {file} ({desc})")

def check_datasets():
    print("\n[SYSTEM] Auditing Heavyweight Datasets (v7.2 Root Mapping)...")
    for name, path in DATA_SOURCES.items():
        if os.path.exists(path):
            size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"[OK] {name} found at {path} ({size_mb:.1f} MB)")
        else:
            print(f"[ERROR] {name} MISSING at {path}!")
            print(f"        Please ensure the files are in the 'data/' folder.")

def check_nltk():
    print("\n[SYSTEM] Validating NLTK Corpora...")
    try:
        import nltk
        assets = ['stopwords', 'punkt', 'wordnet']
        for asset in assets:
            print(f"    Checking {asset}...")
            nltk.download(asset, quiet=True)
        print("[OK] NLTK resources ready.")
    except ImportError:
        print("[!] NLTK not installed. Run 'pip install -r requirements.txt' first.")

def check_dependencies():
    print("\n[SYSTEM] Verifying Python Environment...")
    try:
        import tensorflow
        import pandas
        import matplotlib
        import sklearn
        print(f"[OK] TensorFlow {tensorflow.__version__} and core libraries verified.")
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        print("        Running 'pip install -r requirements.txt' is recommended.")

def main():
    print("="*60)
    print(" SOCIAL MEDIA SENTIMENT ANALYSIS: CONTROLLED RESEARCH SYSTEM ")
    print(" v7.2 - 'Academic Defense' Edition ")
    print("="*60)
    check_structure()
    check_files()
    check_datasets()
    check_dependencies()
    check_nltk()
    print("\n" + "="*60)
    print(" SYSTEM READY: Launch START_PLATFORM.bat to view Dashboard. ")
    print("="*60)

if __name__ == "__main__":
    main()
