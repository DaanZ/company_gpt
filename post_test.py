# client.py
import requests
import json

# Define the URL of the Streamlit app with the 'api' and 'data' query parameters
url = "http://localhost:8502/?api=true&data="

# JSON data to send
data = {"name": "example", "value": 42}

# Encode the JSON data and add it as a query parameter
response = requests.get(url + json.dumps(data))

# Display the response
print("Response Status:", response.status_code)
print(response.content)
print("Response Data:", response.json())