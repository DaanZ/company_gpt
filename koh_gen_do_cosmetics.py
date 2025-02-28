
from history import History
from loader import load_knowledge_logs
from streaming_interface import streaming_interface

from core.main_interface import start_menu

if __name__ == "__main__":
    company_name = "Koh Gen Do - Cosmetics"
    emoji = "💄"
    company_id = "koh_gen_do_cosmetics"
    start_menu(company_name, company_id)
