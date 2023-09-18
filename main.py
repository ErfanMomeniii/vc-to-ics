from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json


class Course:
    def __init__(self, title, time, teacher):
        self.title = title
        self.time = time
        self.teacher = teacher


f = open("secret.json")
data = json.load(f)
username = data["username"]
password = data["password"]
term = data["term"]

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://vc%s.kntu.ac.ir/login/index.php" % term)
driver.find_element(by=By.ID, value="username").send_keys(username)
driver.find_element(by=By.ID, value="password").send_keys(password)
driver.find_element(by=By.ID, value="loginbtn").click()

rows = driver.find_element(by=By.CLASS_NAME, value="frontpage-course-list-enrolled").find_elements(by=By.CLASS_NAME,
                                                                                                   value="container-fluid")
cs = []

for _, row in enumerate(rows):
    courses = row.find_elements(by=By.CLASS_NAME, value="coursevisible")
    for _, item in enumerate(courses):
        title = item.find_element(by=By.TAG_NAME, value="a").get_attribute("data-original-title")
        time = item.find_element(by=By.CLASS_NAME, value="text_to_html").text
        teacher = item.find_elements(by=By.TAG_NAME, value="li")[0].text
        c = Course(title, time, teacher)
        cs.append(c)
print(cs)
driver.close()
