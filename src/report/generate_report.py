import json

def generate_qaqc_report(summary: dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
