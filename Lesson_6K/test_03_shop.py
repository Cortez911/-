from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_form():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # Авторизация
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    password_field.send_keys(Keys.ENTER)

    # Добавление товаров в корзину
    backpack = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    backpack.click()
    tshirt = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
    tshirt.click()
    onesie = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
    onesie.click()

    # Переход в корзину
    shopping_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart.click()

    # Checkout
    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

    # Заполнение формы (замените на ваши данные)
    firstname_field = driver.find_element(By.ID, "first-name")
    firstname_field.send_keys("Тест") # Имя
    lastname_field = driver.find_element(By.ID, "last-name")
    lastname_field.send_keys("Тестович") # Фамилия
    zipcode_field = driver.find_element(By.ID, "postal-code")
    zipcode_field.send_keys("010101") # Почтовый индекс
    driver.find_element(By.ID, "continue").click()

    # Проверка итоговой стоимости
    total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total = total_element.text
    total = total[7:]
    assert total == "$58.29"
    print(f" {total_element.text}") # вывод в консоль

    driver.quit()
