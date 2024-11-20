
from history import History
from loader import load_knowledge_logs
from streaming_interface import streaming_interface


if __name__ == "__main__":
    company_name = "Inform Data"
    emoji = "📈"
    company_id = "inform_data"

    # Main program logic (call this function when you want to start the thread)
    try:
        history: History = load_knowledge_logs(company_name, f"data/{company_id}.json")
        print(len(history.logs))
        streaming_interface(company_name, emoji, history)
    except KeyboardInterrupt:
        print("Program interrupted.")

