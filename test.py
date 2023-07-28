import os
import requests
from bs4 import BeautifulSoup

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

def scrape_images_from_website(url, category, url_index):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_elements = soup.find_all('img')

    for index, img in enumerate(image_elements):
        image_url = img.get('src')
        if image_url:
            image_url = image_url.strip()
            if image_url.startswith('http'):
                image_filename = f"{folder_name}_{category}_{url_index}_{index}.jpg"
                image_path = os.path.join(folder_name, category, image_filename)
                download_image(image_url, image_path)
                full_path = os.path.abspath(image_path)
                print(f"Image saved at: {full_path}")

if __name__ == "__main__":
    url_input = input("Enter the url: (it is a comma seprated inputs)")
    folder_name = input("Enter the folder name:")
    website_urls = url_input.split(',')
    data = input('Enter the category name:')
    dataset_categories = data.split(',')# Customize categories

    for category in dataset_categories:
        os.makedirs(os.path.join(folder_name, category), exist_ok=True)

    for url_index, url in enumerate(website_urls):
        for category in dataset_categories:
            scrape_images_from_website(url, category, url_index)