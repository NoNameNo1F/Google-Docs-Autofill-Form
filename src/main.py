import csv
import json
import os
import random
from time import sleep

#import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def random_answer(element, index, list: list):
    list_random = list[random.randrange(0, len(list))]
    for i in range(4):
        question = element.find_element(By.XPATH, f"div[{index + i}]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
        if question:
            question[list_random[i] - 1].click()

def random_answer_weight(element, index, list_input: list, list_weight: list, option_random: int):
    """
        list_input: random input from file
        list_weight: list probability of choices
        option_random: question to use weight from 1 to 4(0->3 for index array)
    """
    list_random = list_input[random.randrange(0, len(list_input))]
    for i in range(4):
        question = element.find_element(By.XPATH, f"div[{index + i}]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

        if question:
            if i == option_random - 1:
                choose_weight = random.choices([3,4,5],list_weight, k=1)[0] - 1
                question[choose_weight].click()
            else:
                question[list_random[i] - 1].click()

def random_page2_FGC(element):
    options = []
    """Random option 3,4,5 to pick up"""
    for i in range(4):
        options.append(random.randrange(2,5))

    question1 = element.find_element(By.XPATH, "div[5]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question2 = element.find_element(By.XPATH, "div[6]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question3 = element.find_element(By.XPATH, "div[7]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question4 = element.find_element(By.XPATH, "div[8]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

    if question1:
        question1[options[0]].click()
    if question2:
        question2[options[1]].click()
    if question3:
        question3[options[2]].click()
    if question4:
        question4[options[3]].click()

def random_page2_UGC(element):
    options = []
    """Random option 3,4,5 to pick up"""
    for i in range(4):
        options.append(random.randrange(2,5))

    question1 = element.find_element(By.XPATH, "div[10]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question2 = element.find_element(By.XPATH, "div[11]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question3 = element.find_element(By.XPATH, "div[12]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question4 = element.find_element(By.XPATH, "div[13]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

    if question1:
        question1[options[0]].click()
    if question2:
        question2[options[1]].click()
    if question3:
        question3[options[2]].click()
    if question4:
        question4[options[3]].click()

def random_page3_BA(element):
    options = []
    """Random option 3,4,5 to pick up"""
    for i in range(4):
        options.append(random.randrange(2,5))

    question1 = element.find_element(By.XPATH, "div[5]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question2 = element.find_element(By.XPATH, "div[6]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question3 = element.find_element(By.XPATH, "div[7]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question4 = element.find_element(By.XPATH, "div[8]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

    if question1:
        question1[options[0]].click()
    if question2:
        question2[options[1]].click()
    if question3:
        question3[options[2]].click()
    if question4:
        question4[options[3]].click()

def random_page3_BAS(element):
    options = []
    """Random option 3,4,5 to pick up"""
    for i in range(4):
        options.append(random.randrange(2,5))

    question1 = element.find_element(By.XPATH, "div[10]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question2 = element.find_element(By.XPATH, "div[11]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question3 = element.find_element(By.XPATH, "div[12]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question4 = element.find_element(By.XPATH, "div[13]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

    if question1:
        question1[options[0]].click()
    if question2:
        question2[options[1]].click()
    if question3:
        question3[options[2]].click()
    if question4:
        question4[options[3]].click()

def random_page3_LOYALTY(element):
    options = []
    """Random option 3,4,5 to pick up"""
    for i in range(4):
        options.append(random.randrange(2,5))

    question1 = element.find_element(By.XPATH, "div[15]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question2 = element.find_element(By.XPATH, "div[16]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question3 = element.find_element(By.XPATH, "div[17]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question4 = element.find_element(By.XPATH, "div[18]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

    if question1:
        question1[options[0]].click()
    if question2:
        question2[options[1]].click()
    if question3:
        question3[options[2]].click()
    if question4:
        question4[options[3]].click()

def random_page3_TRUST(element):
    options = []
    """Random option 3,4,5 to pick up"""
    for i in range(4):
        options.append(random.randrange(2,5))

    question1 = element.find_element(By.XPATH, "div[20]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question2 = element.find_element(By.XPATH, "div[21]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question3 = element.find_element(By.XPATH, "div[22]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    question4 = element.find_element(By.XPATH, "div[23]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

    if question1:
        question1[options[0]].click()
    if question2:
        question2[options[1]].click()
    if question3:
        question3[options[2]].click()
    if question4:
        question4[options[3]].click()

def random_page4_info(element):
    options = []

    for i in range(4):
        options.append(random.randrange(2,5))

    optSex = element.find_element(By.XPATH, "div[2]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    optAge = element.find_element(By.XPATH, "div[3]")\
                        .find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
    optJob = element.find_element(By.XPATH, "div[4]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
    optSalary = element.find_element(By.XPATH, "div[5]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

    optPlfs = element.find_element(By.XPATH, "div[6]")\
                        .find_elements(By.CLASS_NAME, "uVccjd.aiSeRd.FXLARc.wGQFbe.BJHAP.oLlshd")
    optEcoms = element.find_element(By.XPATH, "div[7]")\
                        .find_elements(By.CLASS_NAME, "uVccjd.aiSeRd.FXLARc.wGQFbe.BJHAP.oLlshd")
    optRegular = element.find_element(By.XPATH, "div[8]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

    optPurpose = element.find_element(By.XPATH, "div[9]")\
                        .find_elements(By.CLASS_NAME, "uVccjd.aiSeRd.FXLARc.wGQFbe.BJHAP.oLlshd")

    if optSex:
        optSex[random.choices([0,1],[0.667, 0.333], k=1)[0]].click()

    if optAge:
        age = random.choices([18,19,20,21,22,23,24,25,26,27],[0.18, 0.18, 0.18, 0.18, 0.18, 0.02, 0.02, 0.02, 0.02, 0.02], k=1)[0]

        optAge.send_keys(age)

        if age >= 18 and age <= 22:
            optJob[0].click()
            optSalary[0].click()

        else:
            optJob[random.randrange(1,3)].click()
            optSalary[random.randrange(1,6)].click()

    if optPlfs:
        optPlfs[0].click()
        optPlfs[1].click()
        for i in range(2,4):
            if random.choice([True, False]):
                optPlfs[i].click()

    if optEcoms:
        optEcoms[0].click()
        for i in range(1, 6):
            if random.choice([True, False]):
                optEcoms[i].click()

    if optRegular:
        optRegular[random.choices([0,1,2,3,4],[0.027,0.289,0.421,0.263,0], k=1)[0]].click()

    if optPurpose:
        optPurpose[0].click()
        for i in range(1,3):
            if random.choice([True, False]):
                optPurpose[i].click()



def get_data_file_path(filename):
        # Get the path to the data directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, 'file')
        # Return the path to the data.json file
        return os.path.join(data_dir, filename)

if __name__ == "__main__":
    config = load_dotenv()

    driver = webdriver.Chrome()
    """Load Case From Files"""
    file1 = open(get_data_file_path('list_one.txt'))
    reader = csv.reader(file1, delimiter=',')
    list_random_1 = []
    for row in reader:
        temp = []
        temp.append(int(row[0]))
        temp.append(int(row[1]))
        temp.append(int(row[2]))
        temp.append(int(row[3]))
        list_random_1.append(temp)

    file2 = open(get_data_file_path('list_two.txt'))
    reader = csv.reader(file2, delimiter=',')
    list_random_2 = []
    for row in reader:
        temp = []
        temp.append(int(row[0]))
        temp.append(int(row[1]))
        temp.append(int(row[2]))
        temp.append(int(row[3]))
        list_random_2.append(temp)

    docs_link = os.environ.get("LINK_TEST2")

    time = 0
    while(time < 100):
        print(f"Tried From : {time + 1}")
        driver.get(docs_link)

        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div")
            )
        )

        """Handle First Page"""
        first_page = element.find_element(By.XPATH, "div[2]/div[2]")

        click_first_page = first_page.find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
        if click_first_page:
            click_first_page[0].click()

        next = element.find_element(By.XPATH, "div[3]/div/div[1]/div")
        next.click()

        """Handle Second Page"""
        element = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div")
            )
        )

        second_page = element.find_element(By.XPATH, "div[2]")

        list_weight_1 = [0.4,0.4,0.2]
        option_apply_weight = 1
        random_answer_weight(second_page,5,list_random_1,list_weight_1,option_apply_weight)


        list_weight_2 = [0.25,0.5,0.25]
        random_answer_weight(second_page,10,list_random_1,list_weight_2,option_apply_weight)


        next = element.find_element(By.XPATH, "div[3]/div/div[1]/div[2]")
        next.click()


        """Handle Third Page"""
        element = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div")
            )
        )

        third_page = element.find_element(By.XPATH, "div[2]")
        random_answer(third_page, 5,list_random_1)
        random_answer(third_page, 10,list_random_1)
        random_answer(third_page, 15,list_random_2)
        random_answer(third_page, 20,list_random_2)


        next = element.find_element(By.XPATH, "div[3]/div/div[1]/div[2]")
        next.click()


        """Handle Fourth Page"""
        element = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div")
            )
        )

        fourth_page = element.find_element(By.XPATH, "div[2]")
        random_page4_info(fourth_page)

        next = element.find_element(By.XPATH, "div[3]/div/div[1]/div[2]")
        next.click()

        """Submit Page"""
        element = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div")
            )
        )

        submit = element.find_element(By.XPATH, "div[3]/div/div[1]/div[2]")
        submit.click()
        time += 1

    driver.quit()
