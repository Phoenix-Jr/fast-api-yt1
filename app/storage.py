from pathlib import Path
import json


DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "issues.json"


def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            content =  json.load(f)
            if content.strip():
                return json.loads(content)
    return []

def save_data(data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE,'w') as f:
        json.dump(data,f,indent=2)