from company_interface import create_interface
from fireflies.fetch import last_transcript_id
from fireflies.transcript import get_transcript
from history import History
from loader import history_pages, load_knowledge_logs

if __name__ == "__main__":
    company_name = "NYX Cosmetics"
    emoji = "💄🪞💅"
    company_id = "nyx"

    history: History = history_pages(f"data/{company_id}")
    history.extend(load_knowledge_logs(f"data/{company_id}.json"))
    result = last_transcript_id()  # Execute the query
    sentences, transcript = get_transcript(result)
    history.system("Transcript: " + transcript)
    print(len(history.logs))
    create_interface(company_name, emoji, history)
    