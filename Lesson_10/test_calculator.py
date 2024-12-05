import allure
import pytest
from selenium import webdriver
from calculator_page import SlowCalculatorPage


@allure.title("Тест калькулятора")
@allure.description("Проверяет работу медленного калькулятора.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(browser: webdriver.Chrome):
    calculator_page = SlowCalculatorPage(browser)
    calculator_page.open()
    calculator_page.set_delay("45")
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")
    def get_result(self) -> str:
        try:
            result_element = self.wait.until(EC.presence_of_element_located(self.result_locator))
            # Ожидание, пока текст изменится и станет непустым
            self.wait.until(lambda driver: result_element.text.strip() and result_element.text.strip().isdigit())
            return result_element.text.strip()
        except (TimeoutException, NoSuchElementException) as e:
            return f"Ошибка получения результата: {e}"
