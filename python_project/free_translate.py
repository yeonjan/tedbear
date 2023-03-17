from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pymysql
import sys


def translate_free(question):
    form.clear()
    form.send_keys(question)
    time.sleep(3)
    result = driver.find_element(By.CSS_SELECTOR, "div#txtTarget")
    return result.text


def init_driver():
    chrome_driver = ChromeDriverManager().install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    return driver


if __name__ == '__main__':
    conn = pymysql.connect(host='3.36.50.141', user='root', password='824b2937-79c0-4595-8ea2-e8930ed750ae',
                           database='tedbearDB',
                           autocommit=True)
    cursor = conn.cursor()
    no_start, no_end = sys.argv[1:]
    sql = f'SELECT * FROM sentence_tb where translation is null and no between {no_start} and {no_end}'
    cursor.execute(sql)
    rows = cursor.fetchall()
    driver = init_driver()
    URL = 'https://papago.naver.com/?sk=en&tk=ko'
    driver.get(URL)
    time.sleep(3)
    form = driver.find_element(By.CSS_SELECTOR, "textarea#txtSource")
    # ------------------

    for row in rows:
        start = time.time()
        no, content, *trash = row
        content = content.replace('\\', '')
        translate_content = translate_free(content.replace('\\', '')) if len(
            content) < 5000 else 'NO SCRIPT BECAUSE TOO LONG'
        sql = 'update sentence_tb set translation = %s where no = %s'
        cursor.execute(sql, (translate_content, no))
        end = time.time()
        print(f'{no} : {translate_content[:30]} ... {(end - start):.2f} sec')
    cursor.close()
    driver.close()
