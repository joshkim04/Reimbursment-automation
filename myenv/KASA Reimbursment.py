from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
import csv
import time



# Set up Firefox WebDriver
options = webdriver.FirefoxOptions()
#options.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://sabo.studentlife.northeastern.edu/sabo-expense-reimbursement-voucher/")








class reimbursment:
    def __init__(self, name, id, address, email, number, reason):
        self.name = name
        self.id = id
        self.address = address
        self.email = email
        self.number = number
        self.reason = reason

#Variable of name reimbursments
reimbursments = []
print("test")


def read_reimbursments(filename,reimbursments):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            row = row[0].split("	")
            temp = reimbursment(row[0], row[1], row[2], row[3], row[4], row[5])
            reimbursments.append(temp)



read_reimbursments("Reimbursments.csv",reimbursments)


#function to enter reimbursment data
def enterinfo(data):
    # Click boxes
    choice = "choice_2_155_"
    for x in range(7):
        driver.find_element(By.ID, choice + str(x+1)).click()

    # Wait for main dashboard to load
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "input_2_2_3")))

    #First Name and Last name
    driver.find_element(By.ID, "input_2_2_3").send_keys(data.name.split()[0])
    driver.find_element(By.ID, "input_2_2_6").send_keys(data.name.split()[1])
    #NUID
    driver.find_element(By.ID, "input_2_76").send_keys(data.id)
    #Address
    driver.find_element(By.ID, "input_2_97").send_keys(data.address)
    #Click "I made a non travel purchase"
    driver.find_element(By.ID, "choice_2_13_0").click()

    #Expense description
    driver.find_element(By.ID, "input_2_142").send_keys(data.reason)

    #Certify I am making only non travel purchases 
    driver.find_element(By.ID, "choice_2_156_1").click()
    #Budget index
    driver.find_element(By.ID, "input_2_16").send_keys("800162")

    driver.find_element(By.ID, "input_2_142").send_keys("800162")

    #First and Last name in approvals
    driver.find_element(By.ID, "input_2_81_3").send_keys(data.name.split()[0])
    driver.find_element(By.ID, "input_2_81_6").send_keys(data.name.split()[1])
    #NuEmail
    driver.find_element(By.ID, "input_2_98").send_keys(data.email)


    #Student group treasurer name and email
    driver.find_element(By.ID, "input_2_165_3").send_keys("Joshua")
    driver.find_element(By.ID, "input_2_165_6").send_keys("Kim")
    driver.find_element(By.ID, "input_2_166").send_keys("kim.joshua1@northeastern.edu")

    #Phone number
    driver.find_element(By.ID, "input_2_153").send_keys(data.number)
    #Click certify that this report is true and accurate
    driver.find_element(By.ID, "choice_2_99_1").click()
    #Advisor name
    driver.find_element(By.ID, "input_2_64_3").send_keys("John")
    driver.find_element(By.ID, "input_2_64_6").send_keys("Park")
    #Advisor Email
    driver.find_element(By.ID, "input_2_65").clear()
    driver.find_element(By.ID, "input_2_65").send_keys("john.park@northeastern.edu")

    #City, also warps back up to the top
    driver.find_element(By.ID, "input_2_94").send_keys("Boston")
    #Zip code
    driver.find_element(By.ID, "input_2_96").send_keys("02120")

count = 0
print(len(reimbursments))

while count < len(reimbursments):
    # Wait for page to load
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.ID, "choice_2_155_1")))
    enterinfo(reimbursments[count])
    count += 1
    driver.execute_script("window.open('about:blank', '_blank');")
    driver.switch_to.window(driver.window_handles[count])  # Switch to the new tab
    driver.get("https://sabo.studentlife.northeastern.edu/sabo-expense-reimbursement-voucher/")



# Close the browser
#driver.quit()

