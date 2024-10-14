from history import History
from loader import load_instagram_logs
from streaming_logo import streaming_logo_interface

if __name__ == "__main__":
    company_name = "Mirzam 🍫"
    emoji = "🍫🎁🏭"
    company_id = "mirzamchocolate"
    # Main program logic (call this function when you want to start the thread)
    try:
        print(f"data/{company_id}.json")
        history: History = load_instagram_logs(company_name, f"data/{company_id}.json")
        print(len(history.logs))
        history.assistant("I am Mirzam's AI.\nHow can I help you?")
        streaming_logo_interface(company_name, emoji, history, background="chocolate.png")
    except KeyboardInterrupt:
        print("Program interrupted.")
