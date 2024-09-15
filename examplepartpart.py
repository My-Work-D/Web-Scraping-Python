

import requests
from bs4 import BeautifulSoup
import csv
import time

def slicetext(text, start, end):
    try:
        return text.split(start)[1].split(end)[0]
    except IndexError:
        return ""

csv_file_path = 'patpat5.csv'

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Land Size', 'Location', 'Total Price', 'Monthly Payment', 'Image URL'])  # Added 'Image URL' column

for i in range(100):
    url = f'https://www.patpat.lk/property?page={i}&city=&sub_category=&sub_category_name=&category=property&search_txt=&sort_by='

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        cards = soup.find_all(class_='result-item')

        for card in cards:
            title = card.find(class_='result-title').text.strip()

            # Extracting land size and location
            size_info = card.find_all('p', class_='clearfix')  # Adjust this based on the correct class
            if len(size_info) >= 2:
                size = size_info[0].text.strip()  # Assume the first is the size
                location = size_info[1].text.strip()  # Assume the second is the location
            else:
                size = "Size not available"
                location = "Location not available"

            total = slicetext(str(card), "Total Price", "</p>")
            total = slicetext(total, "<span class=\"money\">", "</span>")
            mon = slicetext(str(card), "Monthly Payment", "</p>")
            mon = slicetext(mon, "<span class=\"money\">", "</span>")

            # Extract image URL
            image_tag = card.find('img')  # Find the image tag
            image_url = image_tag['src'] if image_tag else 'No Image'  # Extract the src attribute or 'No Image' if not available

            print("Title : ", title)
            print("Location : ", location)
            print("Size : ", size)
            print("Total : Rs.", total)
            print("Monthly : Rs.", mon)
            print("Image URL : ", image_url)  # Print the image URL
            print("*" * 10)

            # Write the data into the CSV
            arr = [title, size, location, total, mon, image_url]  # Added image URL to the array
            with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(arr)
    else:
        print("Error: Failed to fetch data from the website.")

    time.sleep(1)  # Delay between requests
