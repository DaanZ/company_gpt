from company_interface import create_interface
from fireflies.fetch import last_transcript_id
from fireflies.transcript import get_transcript
from history import History
from loader import history_pages, load_knowledge_logs, load_knowledge_website
from streaming_interface import streaming_interface

if __name__ == "__main__":
    company_name = "Mon Kit Solar"
    emoji = "🌞"
    company_id = "mon_kit_solar"

    try:
        history: History = load_knowledge_website(company_id)
        streaming_interface(company_name, emoji, history, agent="")
    except KeyboardInterrupt:
        print("Program interrupted.")
    