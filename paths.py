import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMAGE_DIR = os.path.join(ASSETS_DIR, "images")
DOCS_DIR = os.path.join(ASSETS_DIR, "docs")
DATA_DIR = os.path.join(BASE_DIR, "data")

DB_PATH = os.path.join(DATA_DIR, "SELF.db")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def image_path(filename: str) -> str:
    return os.path.join(IMAGE_DIR, filename)

def doc_path(filename: str) -> str:
    return os.path.join(DOCS_DIR, filename)
