# from backend.utils.vachanamrut_loader import load_vachanamrut
# from backend.utils.chunker import split_into_chunks

# entries = load_vachanamrut("data/raw/vachanamrut_combined.json")

# all_chunks = []
# for entry in entries:
#     chunks = split_into_chunks(entry)
#     all_chunks.extend(chunks)

# print(f"Total chunks: {len(all_chunks)}")
# print(all_chunks[0])  # Preview

from backend.rag.pipeline import ask_question

response = ask_question("How can one overcome ego?")
print(response)
