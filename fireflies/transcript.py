import requests

from fireflies.api import api_key


def get_transcript(transcript_id = "yv4zI2iqjvbdgbyz"):
    url = 'https://api.fireflies.ai/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = '{"query": "query Transcript($transcriptId: String!) { transcript(id: $transcriptId) { title id sentences {text} } }", "variables": {"transcriptId": "' + transcript_id + '"}}'

    response = requests.post(url, headers=headers, data=data)
    #print(response.json())
    data = response.json()
    sentences = [sentence["text"] for sentence in data["data"]["transcript"]["sentences"]]
    transcript = " ".join(sentences)
    print(transcript)
    return sentences, transcript


if __name__ == "__main__":
    get_transcript()
