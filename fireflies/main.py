from fetch import last_transcript_id
from transcript import get_transcript

def store_sentences_to_file(sentences, filename):
    """
    This function stores a list of sentences into a text file.

    Parameters:
    sentences (list): A list of sentences to be written to the file.
    filename (str): The name of the file to write the sentences to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + '\n')


if __name__ == "__main__":
    result = last_transcript_id()  # Execute the query
    sentences, transcript = get_transcript(result)
    store_sentences_to_file(sentences, "transcript.txt")
