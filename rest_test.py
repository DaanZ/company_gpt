# app.py
import streamlit as st
import json


# Define a function to process the incoming JSON data
def process_data(data):
    # For this example, the response will contain the received data with a simple message
    result = {"received_data": data, "status": "processed"}
    return result


# Add a query parameter check to simulate an API call
query_params = st.experimental_get_query_params()

# Check if 'api' and 'data' parameters exist in the query
if 'api' in query_params and 'data' in query_params:
    try:
        # Parse the 'data' parameter as JSON
        data = json.loads(query_params.get('data')[0])
        response = process_data(data)

        # Use the `st.write()` function to output JSON directly as an API response
        st.write(response)
    except json.JSONDecodeError:
        # Display error if JSON parsing fails
        st.write({"error": "Invalid JSON data"})
else:
    st.title("Basic Streamlit REST API Simulation")

    # Provide a text area for manual JSON input within the app for testing
    input_json = st.text_area("Enter JSON data:", '{"name": "test", "value": 123}')

    # When the user clicks "Submit", process the input JSON
    if st.button("Submit"):
        try:
            # Parse input JSON and display response
            data = json.loads(input_json)
            response = process_data(data)
            st.json(response)
        except json.JSONDecodeError:
            st.error("Invalid JSON input.")
