import requests
import os

# TODO: replace this URL with a URL containing real SourceStack data
url = "https://shesharpnl.github.io/hackathon-2023.sourcestack-data/assets/junior-nl.csv"

response = requests.get(url)
response.raise_for_status()

file_path = "./assets/sourcestack-data.csv"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, "wb") as file:
    file.write(response.content)

print("CSV file saved successfully.")
