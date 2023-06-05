from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os
from selenium.webdriver.support.ui import Select

def process_form(url, file):
    df = pd.read_excel(file, skiprows=2)
    # Specify the path of the driver file
    driver = webdriver.Chrome() 

    # Access the URL
    driver.get(url)
    div = driver.find_element(By.ID, 'paxContainer625654')
    fieldset = div.find_element(By.TAG_NAME, 'fieldset')
    all_direct_children_divs = fieldset.find_elements(By.XPATH, './*')
    passenger_rows = [div for div in all_direct_children_divs if 'row' in div.get_attribute('class')][2:]


    honorific = "Mr."
    first_name = "Awais"
    last_name = "Mazahir"
    passenger_type = "Adult"
    bags = True

    # Iterate over the rows in the DataFrame and fill the form
    for i,row in df.iterrows():

        gender = row['Gender']
        
        if gender == 'M':
            honorific = 'Mr'
        else:
            honorific = 'Ms'

        first_name = row['Firstname']
        last_name = row['Lastname']
        passenger_type = row['Passengertype']
        bags = True if row['Bags20Kgs'] == 'Yes' else False


        # Find the relevant input elements and fill them with data
        honorific_select = passenger_rows[i].find_element(By.NAME, f'PAXTitle[625654][]')
        select = Select(honorific_select)
        select.select_by_value(honorific)

        first_name_input = passenger_rows[i].find_element(By.NAME, f'PAXFirstName[625654][]')
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = passenger_rows[i].find_element(By.NAME, f'PAXLastName[625654][]')
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        passenger_type_select = passenger_rows[i].find_element(By.NAME, f'PAXPassangerType[625654][]')

        passenger_type_select.send_keys(passenger_type)

        bags_checkbox = passenger_rows[i].find_element(By.NAME, f'bag20[625654][]')
        if bags:
            # Only click the checkbox if it's not already selected
            if not bags_checkbox.is_selected():
                bags_checkbox.click()
        else:
            # Only click the checkbox if it's already selected
            if bags_checkbox.is_selected():
                bags_checkbox.click()


    # Submit the form
    submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'leadAddPax')))
    submit_button.click()

    # Pause the script for a while for the submission to be processed
    time.sleep(5)

    # Close the driver
    driver.close()

if __name__=="__main__":
    current_dir = os.getcwd()
    url = os.path.join(current_dir, 'Group Sales Ryanair website', 'Group Sales website.html')
    # Load data from Excel file
    file='Passengers list.xlsx'
    process_form(url, file)
