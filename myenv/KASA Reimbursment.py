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

# Wait for page to load
WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.ID, "choice_2_155_1")))

# Click boxes
choice = "choice_2_155_"
for x in range(7):
    driver.find_element(By.ID, choice + str(x+1)).click()


class reimbursment:
    def __init__(self, name, id, address, email, number):
        self.name = name
        self.id = id
        self.address = address
        self.email = email
        self.number = number

reimbursments = reimbursment


def read_reimbursments(filename,reimbursments):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            reimbursments.name = row[0]
            reimbursments.id = "00" + row[1]
            reimbursments.address = row[2]
            reimbursments.email = row[3]
            reimbursments.number = row[4]


read_reimbursments("Reimbursments.csv",reimbursments)

# Wait for main dashboard to load
WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "input_2_2_3")))


#First Name and Last name
driver.find_element(By.ID, "input_2_2_3").send_keys(reimbursments.name.split()[0])
driver.find_element(By.ID, "input_2_2_6").send_keys(reimbursments.name.split()[1])
#NUID
driver.find_element(By.ID, "input_2_76").send_keys(reimbursments.id)
#Address
driver.find_element(By.ID, "input_2_97").send_keys(reimbursments.address)
#Click "I made a non travel purchase"
driver.find_element(By.ID, "choice_2_13_0").click()






#Certify I am making only non travel purchases 
driver.find_element(By.ID, "choice_2_156_1").click()
#Budget index
driver.find_element(By.ID, "input_2_16").send_keys("800162")



#First and Last name in approvals
driver.find_element(By.ID, "input_2_81_3").send_keys(reimbursments.name.split()[0])
driver.find_element(By.ID, "input_2_81_6").send_keys(reimbursments.name.split()[1])
#NuEmail
driver.find_element(By.ID, "input_2_98").send_keys(reimbursments.email)

#Student group treasurer name and email
driver.find_element(By.ID, "input_2_165_3").send_keys("Joshua")
driver.find_element(By.ID, "input_2_165_6").send_keys("Kim")
driver.find_element(By.ID, "input_2_166").send_keys("kim.joshua1@northeastern.edu")

#Phone number
driver.find_element(By.ID, "input_2_153").send_keys(reimbursments.number)
#Click certify that this report is true and accurate
driver.find_element(By.ID, "choice_2_99_1").click()
#Advisor name
driver.find_element(By.ID, "input_2_64_3").send_keys("John")
driver.find_element(By.ID, "input_2_64_6").send_keys("Park")
#Advisor Email
driver.find_element(By.ID, "input_2_65").clear()
driver.find_element(By.ID, "input_2_65").send_keys("john.park@northeastern.edu")


# Close the browser
#driver.quit()

