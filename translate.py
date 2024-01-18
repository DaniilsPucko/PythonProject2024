import pandas
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import openpyxl

def read_txt_file(english):
    # Initialize an empty list to store words
    word_list = []

    try:
        # Open the file in read mode
        with open(english, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Split the content into words using commas as separators
            words = content.split(',')

            # Add each word to the list (remove leading/trailing whitespaces)
            word_list.extend(word.strip() for word in words)

        return word_list  # This return statement should be inside the function

    except FileNotFoundError:
        print(f"File not found: {english}")
        return None

