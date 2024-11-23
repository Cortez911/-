from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

  def login(self, username, password):
    username_field = self.driver.find_element(By.ID, "user-name")
    username_field.send_keys(username)
    password_field = self.driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

class ProductsPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

  def add_to_cart(self, product_id):
    add_button = self.wait.until(EC.element_to_be_clickable((By.ID, f"add-to-cart-{product_id}")))
    add_button.click()

  def go_to_cart(self):
    shopping_cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart.click()

class CartPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

  def checkout(self):
    checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

class CheckoutPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

  def fill_form(self, firstname, lastname, zipcode):
    firstname_field = self.driver.find_element(By.ID, "first-name")
    firstname_field.send_keys(firstname)
    lastname_field = self.driver.find_element(By.ID, "last-name")
    lastname_field.send_keys(lastname)
    zipcode_field = self.driver.find_element(By.ID, "postal-code")
    zipcode_field.send_keys(zipcode)
    self.driver.find_element(By.ID, "continue").click()

  def get_total(self):
    total_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    return total_element.text[7:]


def test_form():
  driver = webdriver.Chrome()
  driver.get("https://www.saucedemo.com/")

  login_page = LoginPage(driver)
  login_page.login("standard_user", "secret_sauce")

  products_page = ProductsPage(driver)
  products_page.add_to_cart("sauce-labs-backpack")
  products_page.add_to_cart("sauce-labs-bolt-t-shirt")
  products_page.add_to_cart("sauce-labs-onesie")
  products_page.go_to_cart()

  cart_page = CartPage(driver)
  cart_page.checkout()

  checkout_page = CheckoutPage(driver)
  checkout_page.fill_form("Тест", "Тестович", "010101")
  total = checkout_page.get_total()
  assert total == "$58.29"
  print(f"Итоговая стоимость: {total}")

  driver.quit()
