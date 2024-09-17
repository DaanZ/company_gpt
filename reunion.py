from company_interface import create_interface
from fireflies.fetch import last_transcript_id
from fireflies.transcript import get_transcript
from history import History
from loader import history_pages, load_knowledge_logs

if __name__ == "__main__":
    company_name = "M Riviera"
    emoji = "🏘️🔷💰"
    company_id = "reunion"

    history: History = history_pages(f"data/{company_id}")
    print(len(history.logs))
    prompt = f"""You are a warm, approachable, and knowledgeable assistant for {company_name}. You are currently engaged in a conversation with a real estate agent. Answer their questions in a friendly and professional manner, showcasing your expertise in real estate, market trends, property listings, and client needs."""
    create_interface(company_name, emoji, history, prompt=prompt)
    