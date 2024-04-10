import csv
import json
import os
import random
from time import sleep

#import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""Handler Answer based on LIST Answers"""
def random_answer_list(element, index, list: list):
    list_random = list[random.randrange(0, len(list))]
    for i in range(4):
        question = element.find_element(By.XPATH, f"div[{index + i}]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
        if question:
            question[list_random[i] - 1].click()

def random_answer(element, index):
    for i in range(4):
        question = element.find_element(By.XPATH, f"div[{index + i}]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
        if question:
            question[random.randrange(0, 5)].click()

def random_answer_weight_option(element, index, weight_option: dict):
    """
        list_input: random input from file
        list_weight: list probability of choices
        option_random: question to use weight from 1 to 4(0->3 for index array)
        list_weight_1 = [[0,0,0.3,0.5,0.2],[0,0,0.2,0.45,0.35]]
        option_apply_weight = [1,4]
        1 0 0 0.3 0.5 0.2
        2 0 0 0.3 0.5 0.2
        3 0 0 0.3 0.5 0.2
        4 0 0 0.3 0.5 0.2
        {
            1: [0,0,0.3,0.7,0],
            4: [0,0,0.6,0.4,0]
        }
    """

    for i in range(4):
        question = element.find_element(By.XPATH, f"div[{index + i}]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

        if i + 1 in weight_option.keys():
            if question:
                weight = weight_option[i+1]
                choose_weight = random.choices([1,2,3,4,5],weight, k=1)[0] - 1
                question[choose_weight].click()

def random_answer_weight(element, index, list_weight: list):
    """
        list_input: random input from file
        list_weight: list probability of choices
        option_random: question to use weight from 1 to 4(0->3 for index array)
        list_weight_1 = [0.3,0.5,0.2]
        option_apply_weight = [1]
        1 0 0 0.3 0.5 0.2
        2 0 0 0.3 0.5 0.2
        3 0 0 0.3 0.5 0.2
        4 0 0 0.3 0.5 0.2
    """

    for i in range(4):
        question = element.find_element(By.XPATH, f"div[{index + i}]")\
                        .find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")

        if question:
            weight = list_weight[i]
            choose_weight = random.choices([1,2,3,4,5],weight, k=1)[0] - 1
            question[choose_weight].click()

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
        optSex[random.choices([0,1],[0.276, 0.724], k=1)[0]].click()

    if optAge:
        age = random.choices([18,19,20,21,22,23,24,25,26,27],[0.08, 0.09, 0.23, 0.222, 0.243, 0.027, 0.027, 0.027, 0.027, 0.027], k=1)[0]

        optAge.send_keys(age)

        if age >= 18 and age <= 22:
            optJob[0].click()
            # optSalary[random.randrange(1,6)].click()
            optSalary[random.choices([0,1],[0.81, 0.19], k=1)[0]].click()

        else:
            optJob[random.choices([1,2],[0.57, 0.43], k=1)[0]].click()
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



def get_data_file_path(dir, filename):
        # Get the path to the data directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, dir)
        # Return the path to the data.json file
        return os.path.join(data_dir, filename)

if __name__ == "__main__":
    config = load_dotenv()

    driver = webdriver.Chrome()
    # driver = webdriver.Edge(service=Service(get_data_file_path('webdriver','msedgedriver.exe')))

    # """Load Case From Files"""
    # file1 = open(get_data_file_path('file','list_one.txt'))
    # reader = csv.reader(file1, delimiter=',')
    # list_random_1 = []
    # for row in reader:
    #     temp = []
    #     temp.append(int(row[0]))
    #     temp.append(int(row[1]))
    #     temp.append(int(row[2]))
    #     temp.append(int(row[3]))
    #     list_random_1.append(temp)

    # file2 = open(get_data_file_path('file','list_two.txt'))
    # reader = csv.reader(file2, delimiter=',')
    # list_random_2 = []
    # for row in reader:
    #     temp = []
    #     temp.append(int(row[0]))
    #     temp.append(int(row[1]))
    #     temp.append(int(row[2]))
    #     temp.append(int(row[3]))
    #     list_random_2.append(temp)
    # """End load file"""

    docs_link = os.environ.get("LINK_MAIN")

    time = 0
    while(time < 1):
        print(f"Tried From : {time + 1}")
        driver.get(docs_link)

        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div")
            )
        )

        sleep(0.5)

        """Handle First Page"""
        try:
            first_page = element.find_element(By.XPATH, "div[2]/div[2]")
            print("Current session is {}".format(driver.session_id))
            click_first_page = first_page.find_elements(By.CLASS_NAME, "Od2TWd.hYsg7c")
            if click_first_page:
                click_first_page[0].click()

            next = element.find_element(By.XPATH, "div[3]/div/div[1]/div")
            next.click()
            sleep(0.5)
        except Exception as e:
            print(e.message)


        """Handle Second Page"""
        element = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div")
            )
        )

        second_page = element.find_element(By.XPATH, "div[2]")

        list_weight_fgc = [[0,0,0.3,0.5,0.2],
                            [0,0,0.3,0.5,0.2],
                            [0,0,0.3,0.5,0.2],
                            [0,0,0.2,0.5,0.3]]

        random_answer_weight(second_page,5,list_weight_fgc)
        #
        list_weight_ugc = [[0,0,0.3,0.5,0.2],
                            [0,0,0.2,0.5,0.3],
                            [0,0,0.3,0.5,0.2],
                            [0,0,0.2,0.5,0.3]]

        random_answer_weight(second_page,10,list_weight_ugc)


        next = element.find_element(By.XPATH, "div[3]/div/div[1]/div[2]")
        next.click()

        sleep(0.5)

        """Handle Third Page"""
        element = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div")
            )
        )

        third_page = element.find_element(By.XPATH, "div[2]")

        list_weight_ba = [[0,0,0.1,0.4,0.5],
                            [0,0,0.2,0.3,0.5],
                            [0,0,0.1,0.35,0.55],
                            [0,0,0.05,0.30,0.65]]

        random_answer_weight(third_page, 5, list_weight_ba)

        list_weight_bas = [[0,0,0.22,0.33,0.45],
                            [0,0,0.26,0.29,0.45],
                            [0,0,0.21,0.37,0.42],
                            [0,0,0.42,0.38,0.2]]
        random_answer_weight(third_page, 10, list_weight_bas)

        list_weight_loyalty = [[0,0,0.42,0.34,0.24],
                            [0,0,0.42,0.34,0.24],
                            [0,0,0.22,0.445,0.335],
                            [0,0,0.414,0.386,0.2]]
        random_answer_weight(third_page, 15,list_weight_loyalty)

        list_weight_trust = [[0,0,0.2,0.5,0.3],
                            [0,0,0.2,0.44,0.36],
                            [0,0,0.332,0.406,0.262],
                            [0,0,0.281,0.502,0.217]]

        random_answer_weight(third_page, 20,list_weight_trust)


        next = element.find_element(By.XPATH, "div[3]/div/div[1]/div[2]")
        next.click()

        sleep(0.5)
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

        sleep(0.5)
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
