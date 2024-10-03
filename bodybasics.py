
from history import History
from loader import load_knowledge_logs
from streaming_interface import streaming_interface


if __name__ == "__main__":
    company_name = "Body Basics Fitness"
    emoji = "🏋️‍♂️🏠🛠️"
    company_id = "bodybasics"
    # Main program logic (call this function when you want to start the thread)
    try:
        #start_transcript_thread()  # Start the thread, will only start once
        history: History = load_knowledge_logs(company_name, f"data/{company_id}.json")
        print(len(history.logs))
        streaming_interface(company_name, emoji, history)
    except KeyboardInterrupt:
        print("Program interrupted.")

