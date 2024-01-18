import pandas
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

file_path = 'english.txt'
result = read_txt_file(file_path)

if result is not None:
    print("Words in the file:", result)
else:
    print("No words found.")