

from company_interface import create_interface
from history import History
from loader import load_instagram_logs

# Global flag to track if the thread has started
transcript_thread_started = False


if __name__ == "__main__":
    company_name = "Mirzam"
    emoji = "🍫🎁🏭"
    company_id = "mirzamchocolate"
    # Main program logic (call this function when you want to start the thread)
    try:
        print(f"data/{company_id}.json")
        history: History = load_instagram_logs(company_name, f"data/{company_id}.json")
        print("rerun")
        print(len(history.logs))
        create_interface(company_name, emoji, history)
    except KeyboardInterrupt:
        print("Program interrupted.")

