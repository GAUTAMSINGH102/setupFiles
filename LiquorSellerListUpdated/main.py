# ! pip install -r requirements.txt

import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as BS

from time import sleep

import csv
import os

import warnings
warnings.filterwarnings('ignore')


# Start the Selenium WebDriver
path = r'chromedriver.exe'
driver = webdriver.Chrome(path)

mainLink = 'https://lamp.sla.ny.gov/'

driver.get(mainLink)
sleep(35)

OKbutton = driver.find_element(By.CLASS_NAME, 'jimu-btn')
OKbutton.click()
sleep(10)



# Find the element with id 'main-page'
main_div = driver.find_element(By.ID, 'main-page')

# Find all the elements with class 'single-task'
info = main_div.find_elements(By.CLASS_NAME, 'single-task')

# Click on the first 'single-task' element
if len(info) > 0:
    info[0].click()
    sleep(10)



# Initialize WebDriverWait with a timeout of 10 seconds
wait = WebDriverWait(driver, 10)

input_field = wait.until(
    lambda driver: driver.find_element(By.ID, 'widgets_Query_Widgetwidgets_Query_Widget_41_uniqName_0_2_1')
)



# Read the lines from the input file
with open('modified_data.txt', 'r') as file:
    lines = file.readlines()

# for line in lines:
#     serial_number = line.strip()
# #     print(serial_number)

allLength = len(lines)
# print(allLength)

data = []
finalData = []
finalAllNames = ""
count = 1
checking = 0
error = []

task = driver.find_element(By.CLASS_NAME, 'query-tab-item')
task.click()
sleep(1)

file_path = 'second.csv'

if os.path.exists(file_path):
    # If the file exists, read its content using Pandas
    second = pd.read_csv(file_path)
else:
    second = pd.DataFrame(columns=['1', '2'])

coli = second.columns

# coli

startingIndex = 1
endingIndex = 100

while(startingIndex <= allLength):

    try:

        if(endingIndex > allLength):
            endingIndex = allLength
            
        finalData = []

        for line in lines[startingIndex:endingIndex]:
            
            try:
            
                data = []
                finalAllNames = ""

                idi = line.strip()

                if(count != 1):
                    # Find the task element
                    task = driver.find_element(By.CLASS_NAME, 'query-tab-item')
                    task.click()
                    sleep(1)

                # Clear the input field
                input_field.clear()

                input_field.send_keys(idi)

                # Find the button element
                button = driver.find_element(By.CLASS_NAME, 'jimu-btn')

                # Click on the button
                button.click()

                sleep(2)
                feature_div = driver.find_element(By.CLASS_NAME, 'features-result')

                # Get the page source of the feature_div
                page_source = feature_div.get_attribute('innerHTML')

                # Use BeautifulSoup to parse the page source
                soup = BS(page_source, 'html.parser')

                # Find the third table within the feature_div
                tables = soup.find_all('table')
                principalTable = tables[4]

                allNames = principalTable.find_all('tr')

                for names in allNames[1:]:
                #     print(names.text)
                    namingFirst = (names.text)
                    naming = namingFirst.strip()
                    finalAllNames = finalAllNames + str(naming) + " "

                data.append(idi)
                data.append(finalAllNames)

                finalData.append(data)

                count = count + 1
            except:
                error.append(line)

        if os.path.exists(file_path):
            # If the file exists, read its content using Pandas
            second = pd.read_csv(file_path)
        else:
            second = pd.DataFrame(columns=['1', '2'])

        finalData_df = pd.DataFrame(finalData, columns=coli)

        # Concatenate the row dataframe to the existing dataframe
        second = pd.concat([second, finalData_df], ignore_index=True)

        sleep(1)

        checking += 1

        # principalsData = pd.DataFrame(finalData)
        second.to_csv("second.csv", index=False)

        sleep(1)

        print(f"{checking} Times")

        # break
        
        startingIndex = endingIndex
        endingIndex = startingIndex + 20

    except:
        print('Error')
    


