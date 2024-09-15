

import requests
from bs4 import BeautifulSoup
import csv
import os

url = "https://www.patpat.lk/property"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find_all('h4')

    # Extract content (p tags)
    topic_content = soup.find_all('p')

    # Prepare the list of data to write to CSV
    data = []

    for i, title in enumerate(title):
        if i < len(topic_content):  # Ensure content exists for the topic
            if i+3 < len(topic_content):  # Check if i+3 is within the valid range
                topic = topic_content[i].text.strip()
                features = topic_content[i+1].text.strip()
                location = topic_content[i+2].text.strip()
                create_date = topic_content[i+3].text.strip()
                data.append({
                    'Topic': title.text.strip(),
                    'Features': features,
                    'Content': topic,
                    'Location': location,
                    'CreateDate': create_date
                })
    filename = 'patpat1.csv'
    # Open CSV file for writing
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Topic', 'Features', 'Content', 'Location', 'CreateDate'])
        writer.writeheader()

        # Write each row to CSV
        for row in data:
            writer.writerow(row)

    print(f"Data has been written to {filename}")

else:
    print("Failed to retrieve the page")