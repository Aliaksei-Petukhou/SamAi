from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CheckboxesPage:
    """
    Класс для страницы Checkboxes на the-internet.herokuapp.com.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует экземпляр страницы.
        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.url = "http://the-internet.herokuapp.com/checkboxes"
        self._checkboxes_locator = (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    def open(self):
        """
        Открывает страницу с чекбоксами.
        """
        self.driver.get(self.url)
        return self

    def get_checkboxes(self) -> list[WebElement]:
        """
        Возвращает список всех веб-элементов чекбоксов на странице.
        """
        return self.driver.find_elements(*self._checkboxes_locator)
