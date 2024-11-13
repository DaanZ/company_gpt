from company_interface import create_interface
from fireflies.fetch import last_transcript_id
from fireflies.transcript import get_transcript
from history import History
from loader import history_pages, load_knowledge_logs, read_pages
from streaming_interface import streaming_interface

if __name__ == "__main__":
    company_name = "Dyson Zone"
    emoji = "🏘️🔷💰"
    company_id = "dyson"

    try:
        history = History()
        streaming_interface(company_name, emoji, history, pages=read_pages(f"data/{company_id}"), agent="Report")
    except KeyboardInterrupt:
        print("Program interrupted.")