import re
from typing import List, Dict

def split_into_chunks(entry: Dict, max_chars: int = 500) -> List[Dict]:
    """
    Splits the text of a Vachanamrut into chunks, keeping metadata.
    """
    text = entry["text"]
    paragraphs = re.split(r'\n\s*\n', text.strip())  # split on paragraph breaks
    chunks = []
    chunk_text = ""
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        if len(chunk_text) + len(para) < max_chars:
            chunk_text += " " + para
        else:
            chunks.append({
                "id": entry["id"],
                "reference": entry["reference"],
                "title": entry["title"],
                "chunk": chunk_text.strip()
            })
            chunk_text = para

    # Add last leftover chunk
    if chunk_text:
        chunks.append({
            "id": entry["id"],
            "reference": entry["reference"],
            "title": entry["title"],
            "chunk": chunk_text.strip()
        })

    return chunks