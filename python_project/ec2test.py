from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_driver = ChromeDriverManager().install()
driver = webdriver.Chrome(chrome_driver)

URL = 'https://papago.naver.com/?sk=en&tk=ko'
driver.get(URL)
time.sleep(3)

question = input('번역할 단어를 입력하세요 : ')

form = driver.find_element(By.CSS_SELECTOR, "textarea#txtSource")
form.send_keys(question)

button = driver.find_element(By.CSS_SELECTOR, "button#btnTranslate")
button.click()

while True:
    time.sleep(2)
    result = driver.find_element(By.CSS_SELECTOR, "div#txtTarget")
    if result:
        break
print(question, "->", result.text)

driver.close()
