from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pymysql


def translate_free(question):
    form.clear()
    form.send_keys(question)
    button = driver.find_element(By.CSS_SELECTOR, "button#btnTranslate")
    button.click()

    while True:
        time.sleep(2)
        result = driver.find_element(By.CSS_SELECTOR, "div#txtTarget")
        if result:
            break
    print(question, "->", result.text)


if __name__ == '__main__':
    conn = pymysql.connect(host='3.36.50.141', user='root', password='824b2937-79c0-4595-8ea2-e8930ed750ae',
                           database='tedbearDB',
                           autocommit=True)
    cursor = conn.cursor()
    sql = 'SELECT * FROM word_tb;'
    cursor.execute(sql)
    rows = cursor.fetchall()

    chrome_driver = ChromeDriverManager().install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)

    URL = 'https://papago.naver.com/?sk=en&tk=ko'
    driver.get(URL)
    time.sleep(3)
    form = driver.find_element(By.CSS_SELECTOR, "textarea#txtSource")

    # ------------------

    for row in rows:
        no, content, _, _ = row
        translate_free(content)
    driver.close()
