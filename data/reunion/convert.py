import glob
import os
from bs4 import BeautifulSoup

# Define the path to the 'reunion' folder inside the 'data' folder
folder_path = '.'

# Get all HTML files in the folder
html_files = glob.glob(os.path.join(folder_path, '*.html'))

# Process each HTML file
for html_file_path in html_files:
    # Open and read the content of the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML file with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the text from the HTML
    text = soup.get_text()

    # Get the file name without the extension
    base_name = os.path.splitext(html_file_path)[0]

    # Define the path for the new .txt file
    txt_file_path = f'{base_name}.txt'

    # Write the extracted text to the new .txt file
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f'Text extracted and saved to {txt_file_path}')