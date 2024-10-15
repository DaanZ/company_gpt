
import threading
import time
import os
import streamlit as st

from history import History
from loader import load_knowledge_documents, read_pages
from streaming_interface import streaming_interface

from fireflies.fetch import last_transcript_id
from fireflies.transcript import get_transcript
from streaming_logo import streaming_logo_interface

# Global flag to track if the thread has started
transcript_thread_started = False


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
    company_name = "Hello, I'm Gaia."
    emoji = "🪞"
    company_id = "nyx"
    # Main program logic (call this function when you want to start the thread)
    try:
        #start_transcript_thread()  # Start the thread, will only start once
        pages = read_pages(f"data/{company_id}")
        pages.extend(load_knowledge_documents(company_name, f"data/{company_id}.json"))
        print(len(pages))
        history = History()
        print("rerun")
        history.assistant("Hi, I’m Gaia. What would you like to know?")
        print(len(history.logs))
        streaming_logo_interface(company_name, emoji, history, pages=pages)
    except KeyboardInterrupt:
        print("Program interrupted.")

