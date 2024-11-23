from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
  def __init__(self, driver): # Исправлено: __init__
    self.driver = driver
    self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    self.delay_field_locator = (By.CSS_SELECTOR, "#delay")
    self.button_7_locator = (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)")
    self.button_plus_locator = (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)")
    self.button_8_locator = (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)")
    self.button_equals_locator = (By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning")
    self.result_locator = (By.XPATH, "//div[@id='calculator']//div[@class='top']//div[@class='screen']")

  def open(self):
    self.driver.get(self.url)

  def set_delay(self, value):
    delay_field = self.driver.find_element(*self.delay_field_locator)
    delay_field.clear()
    delay_field.send_keys(value)

  def click_button_7(self):
    self.driver.find_element(*self.button_7_locator).click()

  def click_button_plus(self):
    self.driver.find_element(*self.button_plus_locator).click()

  def click_button_8(self):
    self.driver.find_element(*self.button_8_locator).click()

  def click_button_equals(self):
    self.driver.find_element(*self.button_equals_locator).click()

  def get_result_element(self):
    return self.driver.find_element(*self.result_locator)

def test_form():
    driver = webdriver.Chrome()
    page = SlowCalculatorPage(driver)
    page.open()

    wait = WebDriverWait(driver, 60)
    wait.until(EC.presence_of_element_located((By.ID, "calculator")))

    page.set_delay("45")
    page.click_button_7()
    page.click_button_plus()
    page.click_button_8()
    page.click_button_equals()

    result_element = wait.until(EC.presence_of_element_located(page.result_locator))
    wait.until(lambda driver: result_element.text != "")
    wait.until(lambda driver: result_element.text == "15")
    result = result_element.text
    assert result == "15"
    print("Тест пройден!")
    driver.quit()
