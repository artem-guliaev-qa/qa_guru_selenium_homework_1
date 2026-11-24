import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def homework_test_1():
    print('Тест на заполнение поля Current Address')

    driver = webdriver.Chrome()

    try:
        driver.get('https://qa-guru.github.io/one-page-form/text-box.html')
        driver.maximize_window()
        time.sleep(5)

        current_address_field = driver.find_element(By.ID, 'currentAddress')
        current_address_field.send_keys('г. Москва, ул. Пушина 2')

        submit_button = driver.find_element(By.ID, 'submit')
        submit_button.click()
        time.sleep(10)

        result_box = driver.find_element(By.ID, 'output')
        assert 'г. Москва' in result_box.text
        print('Тест 1 успешно пройден! :)')

    finally:
        driver.quit()


def homework_test_2():
    print('Тест на заполнение поля Permanent Address')

    driver = webdriver.Chrome()

    try:
        driver.get('https://qa-guru.github.io/one-page-form/text-box.html')
        driver.maximize_window()
        time.sleep(5)

        permanent_address_field = driver.find_element(By.ID,
                                                      'permanentAddress')
        permanent_address_field.send_keys('г. Самара, ул. Гагарина 81')

        submit_button = driver.find_element(By.ID, 'submit')
        submit_button.click()
        time.sleep(10)

        result_box = driver.find_element(By.ID, 'output')
        assert 'ул. Гагарина 81' in result_box.text
        print('Тест 2 успешно пройден! :)')
    finally:
        driver.quit()


homework_test_1()
homework_test_2()

