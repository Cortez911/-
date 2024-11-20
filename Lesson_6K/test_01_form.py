from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def test_form():
    driver = webdriver.Chrome()

    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем форму
    first_name_input = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(1) > label > input")
    first_name_input.send_keys("Иван")

    last_name_input = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(2) > label > input")
    last_name_input.send_keys("Петров")

    address_input = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div.col-md-4.py-2 > label > input")
    address_input.send_keys("Ленина, 55-3")

    email_input = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(1) > label > input")
    email_input.send_keys("test@skypro.com")

    phone_input = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input")
    phone_input.send_keys("+7985899998787")

    city_input = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(3) > label > input")
    city_input.send_keys("Москва")

    country_select = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(4) > label > input")
    country_select.send_keys("Россия")

    job_position_input = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(1) > label > input")
    job_position_input.send_keys("QA")

    company_input = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(2) > label > input")
    company_input.send_keys("SkyPro")

    # Нажмите кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "div.col-md-4.py-2 > button").click()

    # Ожидайте элемент "Zip code"
    wait = WebDriverWait(driver, 20)
    zip_code_element = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    # Проверяем, что поле Zip code подсвечено красным
    zip_code_input = driver.find_element(By.ID, "zip-code")

    # Проверяем класс элемента:
    actual_class = zip_code_input.get_attribute("class")
    print(f"Фактический класс элемента zip-code: {actual_class}") # вывод в консоль

    assert zip_code_input.get_attribute("class") == "alert py-2 alert-danger"

    # Проверьте, что остальные поля подсвечены зеленым
    # first-name
    wait = WebDriverWait(driver, 20)
    first_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name"))) 
    actual_class = first_name_element.get_attribute("class")
    print(f"Status first-name: {actual_class}") # вывод в консоль

    assert actual_class

    # last-name
    wait = WebDriverWait(driver, 20)
    last_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#last-name")))
    actual_class = last_name_element.get_attribute("class")
    print(f"Status last-name: {actual_class}") # вывод в консоль

    assert actual_class

    # address
    wait = WebDriverWait(driver, 20)
    address_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#address")))
    actual_class = address_element.get_attribute("class")
    print(f"Status address: {actual_class}") # вывод в консоль

    assert actual_class

    # city
    wait = WebDriverWait(driver, 20)
    city_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#city")))
    actual_class = city_element.get_attribute("class")
    print(f"Status city: {actual_class}") # вывод в консоль

    assert actual_class

    # country
    wait = WebDriverWait(driver, 20)
    country_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#country")))
    actual_class = country_element.get_attribute("class")
    print(f"Status country: {actual_class}") # вывод в консоль

    assert actual_class

    # e-mail
    wait = WebDriverWait(driver, 20)
    e_mail_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#e-mail")))
    actual_class = e_mail_element.get_attribute("class")
    print(f"Status e-mail: {actual_class}") # вывод в консоль

    assert actual_class

    # phone
    wait = WebDriverWait(driver, 20)
    phone_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#phone")))
    actual_class = phone_element.get_attribute("class")
    print(f"Status phone: {actual_class}") # вывод в консоль

    assert actual_class

    # job-position
    wait = WebDriverWait(driver, 20)
    job_position_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#job-position")))
    actual_class = job_position_element.get_attribute("class")
    print(f"Status job-position: {actual_class}") # вывод в консоль

    assert actual_class

    # company
    wait = WebDriverWait(driver, 20)
    company_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#company")))
    actual_class = company_element.get_attribute("class")
    print(f"Status company: {actual_class}") # вывод в консоль

    assert actual_class

    # Закройте браузер
    driver.quit()
