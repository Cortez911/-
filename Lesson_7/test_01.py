from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
  def __init__(self, driver):
    self.driver = driver

class FormPage(BasePage):
  def fill_form(self, first_name, last_name, address, email, phone, city, country, job_position, company):
    self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(1) > label > input").send_keys(first_name)
    self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(2) > label > input").send_keys(last_name)
    self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div.col-md-4.py-2 > label > input").send_keys(address)
    self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(1) > label > input").send_keys(email)
    self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input").send_keys(phone)
    self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(3) > label > input").send_keys(city)
    self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(4) > label > input").send_keys(country)
    self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(1) > label > input").send_keys(job_position)
    self.driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(2) > label > input").send_keys(company)
    self.driver.find_element(By.CSS_SELECTOR, "div.col-md-4.py-2 > button").click()

  def get_zip_code_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

  def get_first_name_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name")))

  def get_last_name_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#last-name")))

  def get_address_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#address")))

  def get_city_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#city")))

  def get_country_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#country")))

  def get_email_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#e-mail")))

  def get_phone_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#phone")))

  def get_job_position_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#job-position")))

  def get_company_element(self):
    wait = WebDriverWait(self.driver, 20)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#company")))




import pytest

def test_form():
  driver = webdriver.Chrome()
  driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
  form_page = FormPage(driver)
  form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
  zip_code_element = form_page.get_zip_code_element()
  first_name_element = form_page.get_first_name_element()
  last_name_element = form_page.get_last_name_element()
  address_element = form_page.get_address_element()
  city_element = form_page.get_city_element()
  country_element = form_page.get_country_element()
  email_element = form_page.get_email_element()
  phone_element = form_page.get_phone_element()
  job_position_element = form_page.get_job_position_element()
  company_element = form_page.get_company_element()

  assert zip_code_element.get_attribute("class") == "alert py-2 alert-danger"
  assert first_name_element.get_attribute("class") == "alert py-2 alert-success"
  assert last_name_element.get_attribute("class") == "alert py-2 alert-success"
  assert address_element.get_attribute("class") == "alert py-2 alert-success"
  assert city_element.get_attribute("class") == "alert py-2 alert-success"
  assert country_element.get_attribute("class") == "alert py-2 alert-success"
  assert email_element.get_attribute("class") == "alert py-2 alert-success"
  assert phone_element.get_attribute("class") == "alert py-2 alert-success"
  assert job_position_element.get_attribute("class") == "alert py-2 alert-success"
  assert company_element.get_attribute("class") == "alert py-2 alert-success"

  driver.quit()
