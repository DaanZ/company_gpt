
from history import History
from loader import load_knowledge_logs, load_knowledge_website
from streaming_interface import streaming_interface


if __name__ == "__main__":
    company_name = "Coliver Coliving"
    emoji = "🏡🍹🐠"
    company_id = "coliver"

    # Main program logic (call this function when you want to start the thread)
    try:
        history: History = load_knowledge_website(company_id)
        history.assistant("""Welcome to Coliver, here are some of the community rules for Coliving:

**1. Respect Arrival and Departure Times**
- Access the Villa common areas from 9am and your room from 3pm.
- On departure, vacate your room by 11am. You may leave your luggage in common areas if departing later.

**2. Key Access and Security**
- Collect keys from the designated key box upon arrival. After retrieving the keys for your room, return the key box key to its original spot for the next guest.
- When leaving, place keys on your door as instructed.

**3. Kitchen Etiquette**
- Clean up immediately after cooking by washing, drying, and putting away dishes to keep the kitchen accessible for others.
- Wipe all surfaces with a sponge to prevent ants.

**4. Common Areas Cleanliness**
- After meals, wipe tables, trays, and other surfaces to deter ants. Keep shared areas clean and organized, and pick up personal belongings.

**5. Trash Management**
- Avoid overfilling trash bins. If they’re full, please take bags to the containers by the entrance. Extra bags are under the sink.

**6. Laundry and Washing Machines**
- Feel free to use the washing machines but bring your own detergent.

**7. Spa, Sauna, and Jacuzzi Use**
- User guides are accessible via QR codes in your room. Follow all instructions for safe and proper use.

**8. Professional Environment Consideration**
- Keep shared spaces tidy to accommodate professional events and workspaces during the day.

**9. Feedback and Reviews**
- If you enjoyed your stay, please leave a 5-star review. For any issues, reach out directly so we can improve.

**10. Departure Checklist**
- Place sheets and towels in the laundry basket, empty trash if needed, and leave any remaining items in the fridge labeled.

We hope these simple guidelines help everyone enjoy their time at Coliving!""")
        print(len(history.logs))
        streaming_interface(company_name, emoji, history)
    except KeyboardInterrupt:
        print("Program interrupted.")

