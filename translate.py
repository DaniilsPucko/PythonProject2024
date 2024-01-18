import pandas
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

def read_txt_file(english):
    word_list = []

    try:
        with open(english, 'r') as file:
            content = file.read()
            words = content.split(',')
            word_list.extend(word.strip() for word in words)

        return word_list

    except FileNotFoundError:
        print(f"File not found: {english}")
        return None

def translate_to_latvian(words):
    driver = webdriver.Chrome()  # You may need to specify the path to your chromedriver executable
    driver.get("https://www.bing.com/translator")
    
    # Wait for the page to load
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tta_input_ta'))
        )
    finally:
        for word in words:
            # Find the input field and type the word
            input_field = driver.find_element(By.ID, 'tta_input_ta')
            input_field.clear()
            input_field.send_keys(word)

            # Wait for the translation to appear
            try:
                translation = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'tta_output_ta'))
                ).text

                print(f"{word} (English) -> {translation} (Latvian)")

            except Exception as e:
                print(f"Translation failed for {word}: {e}")

            # Pause for a moment before translating the next word
            time.sleep(2)

    driver.quit()

# Example usage:
file_path = 'english.txt'
words_to_translate = read_txt_file(file_path)

if words_to_translate is not None:
    translate_to_latvian(words_to_translate)
else:
    print("No words found.")