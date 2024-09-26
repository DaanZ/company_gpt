from company_interface import create_interface
from loader import load_knowledge_logs

if __name__ == "__main__":
    company_name = "Madrí Excepcional"
    company_id = "madri"
    emoji = "🍺🇪🇸❤️"
    history = load_knowledge_logs(company_name, f"data/{company_id}.json")
    create_interface(company_name, emoji, history)
