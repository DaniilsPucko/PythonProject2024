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
    translated_list = []
    driver = webdriver.Chrome()  # You may need to specify the path to your chromedriver executable
    driver.get("https://www.bing.com/translator?to=lv&setlang=be")
    
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
            time.sleep(2)

            # Wait for the translation to appear
            try:
                find = driver.find_element(By.ID, 'tta_output_ta')
                translation = find.get_attribute("value")

                print(f"{word} (English) -> {translation} (Latvian)")
                translated_list.append(translation)

            except Exception as e:
                print(f"Translation failed for {word}: {e}")

            # Pause for a moment before translating the next word
            time.sleep(2)

    driver.quit()
    return translated_list

# Example usage:
file_path = 'english.txt'
words_to_translate = read_txt_file(file_path)

if words_to_translate is not None:
    translate_to_latvian(words_to_translate)
    
    # Save translated words to Excel
    excel_file_path = 'translated_words.xlsx'
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for i, translation in enumerate(workbook, start=1):
        sheet.cell(row=i, column=1, value=translation)

    # Save the Excel file
    workbook.save(excel_file_path)
    print(f"Translated words saved to {excel_file_path}")
else:
    print("No words found.")