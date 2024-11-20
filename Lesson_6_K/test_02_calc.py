from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Chrome()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Введите значение 45 в поле ввода
    wait = WebDriverWait(driver, 10)
    delay_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
    delay_field.clear()
    delay_field.send_keys("45")

    # Нажмите кнопки 7 + 8 =
    driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click() # 7
    driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click() # +
    driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click() # 8
    driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click() # =

    # Ожидание результата с помощью WebDriverWait
    wait = WebDriverWait(driver, 60)
    result_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='calculator']//div[@class='top']//div[@class='screen']")))

    wait.until(lambda driver: result_element.text == "15")

    result_text = result_element.text
    assert result_text == "15"
    print("Тест пройден!")

    driver.quit()
