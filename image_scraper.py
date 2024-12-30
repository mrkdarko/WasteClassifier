import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO


# Function to download images
def download_images(image_urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            img_format = img.format.lower()
            file_path = os.path.join(save_dir, f"image_{i + 1}.{img_format}")
            img.save(file_path)
            print(f"Downloaded: {file_path}")
        except Exception as e:
            print(f"Failed to download image {i + 1}: {e}")


# Function to scrape image URLs
def scrape_google_images(search_query, num_images=10):
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()  # Update with your webdriver's path if necessary
    driver.get("https://images.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    image_urls = set()
    last_height = driver.execute_script("return document.body.scrollHeight")

    while len(image_urls) < num_images:
        # Scroll down and load more images
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new images to load

        images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i")
        for img in images:
            try:
                src = img.get_attribute("src") or img.get_attribute("data-src")
                if src and src not in image_urls:
                    image_urls.add(src)
                    print(f"Found image: {src}")
                    if len(image_urls) >= num_images:
                        break
            except Exception as e:
                print(f"Error retrieving image source: {e}")

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # End of page
            break
        last_height = new_height

    driver.quit()
    return list(image_urls)


# Main script
if __name__ == "__main__":
    query = "hazardous waste"  # Replace with your search term
    save_directory = './waste dataset/train/hazardous'
    num_images_to_download = 30  # Adjust the number of images you want

    urls = scrape_google_images(query, num_images_to_download)
    download_images(urls, save_directory)
    ######################################################

    query = "liquid waste"  # Replace with your search term
    save_directory = "./waste dataset/train/liquid"
    num_images_to_download = 30  # Adjust the number of images you want

    urls = scrape_google_images(query, num_images_to_download)
    download_images(urls, save_directory)
    ################################################################

    query = "organic waste"  # Replace with your search term
    save_directory = "./waste dataset/train/organic"
    num_images_to_download = 30  # Adjust the number of images you want

    urls = scrape_google_images(query, num_images_to_download)
    download_images(urls, save_directory)
    #############################################################


    query = "recyclable waste"  # Replace with your search term
    save_directory = "./waste dataset/train/recyclable"
    num_images_to_download = 30  # Adjust the number of images you want

    urls = scrape_google_images(query, num_images_to_download)
    download_images(urls, save_directory)
    ###################################################################

    query = "solid waste"  # Replace with your search term
    save_directory = "./waste dataset/train/solid"
    num_images_to_download = 10  # Adjust the number of images you want

    urls = scrape_google_images(query, num_images_to_download)
    download_images(urls, save_directory)
    ###################################################################