import requests

from fireflies.api import api_key

headers = {"Authorization": f"Bearer {api_key}"}


def last_transcript_id():  # A simple function to use requests.post to make the API call. Note the json= section.
    query = """
        {
          user {
            email
            recent_transcript
          }
        }
        """
    request = requests.post('https://api.fireflies.ai/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        data = request.json()
        recent_transcript = data["data"]["user"]["recent_transcript"]  # Drill down the dictionary
        return recent_transcript
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


if __name__ == "__main__":
    # The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
    result = last_transcript_id()  # Execute the query
    print("Most recent transcript from user - {}".format(result))

