import json
from typing import List, Dict

def load_vachanamrut(filepath: str) -> List[Dict]:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    processed = []
    for item in data:
        if "text_en" in item and item["text_en"].strip():
            processed.append({
                "id": item.get("vachno"),
                "reference": item.get("section"),
                "title": item.get("title_en"),
                "text": item.get("text_en").strip()
            })

    return processed