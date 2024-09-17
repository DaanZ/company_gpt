
import threading
import time
import os
import streamlit as st

from company_interface import create_interface
from history import History
from loader import history_pages, load_knowledge_logs

# Global flag to track if the thread has started
transcript_thread_started = False


from fireflies.fetch import last_transcript_id
from fireflies.transcript import get_transcript



def save_transcript_to_file(transcript):
    # Ensure the directory exists
    directory = "data/nyx"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the transcript to a file
    file_path = os.path.join(directory, "transcript.txt")
    with open(file_path, "w") as file:
        file.write(transcript + "\n\n")  # Append new transcripts to the file


def process_transcript():
    while True:
        result = last_transcript_id()  # Execute the query
        if result is not None:
            sentences, transcript = get_transcript(result)
            save_transcript_to_file(transcript)
            print("Transcript saved: " + transcript)
        time.sleep(10)  # Wait for 10 seconds before the next request


def start_transcript_thread():
    if 'transcript' not in st.session_state:
        st.session_state['transcript'] = 'started'
        # Create and start the thread
        transcript_thread = threading.Thread(target=process_transcript)
        transcript_thread.daemon = True  # Set to daemon so it exits when the main program does
        transcript_thread.start()
        print("Transcript thread started.")
    else:
        print("Transcript thread is already running.")


if __name__ == "__main__":
    company_name = "NYX Cosmetics"
    emoji = "💄🪞💅"
    company_id = "nyx"
    # Main program logic (call this function when you want to start the thread)
    try:
        start_transcript_thread()  # Start the thread, will only start once
        history: History = history_pages(f"data/{company_id}")
        history.extend(load_knowledge_logs(f"data/{company_id}.json"))
        print("rerun")
        print(len(history.logs))
        create_interface(company_name, emoji, history)
    except KeyboardInterrupt:
        print("Program interrupted.")

