from random import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pymysql


def init_driver():
    chrome_driver = ChromeDriverManager().install()
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--single-process")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    return driver


# no_start, no_end = map(int, input().split())
no_start, no_end = 30000,40000
while True:
    conn = pymysql.connect(host='3.36.50.141', user='root', password='824b2937-79c0-4595-8ea2-e8930ed750ae',
                           database='tedbearDB',
                           autocommit=True)
    cursor = conn.cursor()
    sql = f'SELECT * FROM word_tb where mean is null and no between {no_start} and {no_end}'
    cursor.execute(sql)
    rows = list(cursor.fetchall())
    if len(rows) == 0:
        break
    driver = init_driver()
    for idx, row in enumerate(rows):
        no = row[0]
        content = row[1].replace('#', '')

        URL = 'https://en.dict.naver.com/#/search?query=' + content
        driver.get(URL)
        time.sleep(1.3)
        sql = 'update word_tb set mean = %s where no = %s'
        print(f'[{idx}/{len(rows)}] {content}')
        try:
            results = driver.find_element(By.CSS_SELECTOR,
                                          '#searchPage_entry > div > div:nth-child(1) > ul').find_elements_by_class_name(
                'mean_item')
            mean_list = []
            for result in results:
                mean_list.append(result.text.replace('\n', ' '))
            mean_str = '\n'.join(mean_list)
            print(mean_str)
            cursor.execute(sql, (mean_str, no))
        except:
            cursor.execute(sql, ('정의가 등록되지 않았습니다.', no))
            print('No Means')
        print('-' * 100)

    cursor.close()
    driver.close()
