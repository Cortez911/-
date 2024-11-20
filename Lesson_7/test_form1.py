import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
  def __init__(self, driver):
    self.driver = driver
    self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    self.first_name_field = (By.ID, "first-name")
    self.last_name_field = (By.ID, "last-name")
    self.address_field = (By.ID, "address")
    self.email_field = (By.ID, "email")
    self.phone_field = (By.ID, "phone")
    self.zip_code_field = (By.ID, "zip-code")
    self.city_field = (By.ID, "city")
    self.country_field = (By.ID, "country")
    self.job_position_field = (By.ID, "job-position")
    self.company_field = (By.ID, "company")
    self.submit_button = (By.XPATH, "//button[@type='submit']")


  def open(self):
    self.driver.get(self.url)

  def fill_form(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position, company):
    self.driver.find_element(*self.first_name_field).send_keys(first_name)
    self.driver.find_element(*self.last_name_field).send_keys(last_name)
    self.driver.find_element(*self.address_field).send_keys(address)
    self.driver.find_element(*self.email_field).send_keys(email)
    self.driver.find_element(*self.phone_field).send_keys(phone)
    if zip_code:
      self.driver.find_element(*self.zip_code_field).send_keys(zip_code)
    self.driver.find_element(*self.city_field).send_keys(city)
    self.driver.find_element(*self.country_field).send_keys(country)
    self.driver.find_element(*self.job_position_field).send_keys(job_position)
    self.driver.find_element(*self.company_field).send_keys(company)

  def submit(self):
    self.driver.find_element(*self.submit_button).click()


@pytest.fixture
def driver():
  driver = webdriver.Chrome() # Или другой браузер
  yield driver
  driver.quit()


def test_fill_form(driver):
  page = FormPage(driver)
  page.open()
  page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")
  page.submit()


def test_check_colors(driver):
  page = FormPage(driver)
  page.open()
  page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")
  page.submit()

  zip_code_color = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.zip_code_field)).value_of_css_property("border-color")
  assert "red" in zip_code_color, f"Zip code field border color is not red. Actual color: {zip_code_color}"

  for field in [page.first_name_field, page.last_name_field, page.address_field, page.email_field, page.phone_field, page.city_field, page.country_field, page.job_position_field, page.company_field]:
    color = WebDriverWait(driver, 10).until(EC.presence_of_element_located(field)).value_of_css_property("border-color")
    assert "green" in color, f"{field[1]} field border color is not green. Actual color: {color}"
