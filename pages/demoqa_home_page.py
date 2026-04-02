from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoQaHomePage:
    """
    Класс для главной страницы https://demoqa.com/
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует экземпляр страницы.
        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.url = "https://demoqa.com/"
        self._category_card_locator = "//div[contains(@class, 'card')][.//h5[text()='{}']]"

    def open(self):
        """
        Открывает главную страницу.
        """
        self.driver.get(self.url)
        return self

    def click_category_card(self, category_name: str):
        """
        Кликает на карточку категории по ее названию.

        :param category_name: Название категории (Elements, Forms, и т.д.)
        """
        locator = (By.XPATH, self._category_card_locator.format(category_name))
        wait = WebDriverWait(self.driver, 10)
        card = wait.until(EC.element_to_be_clickable(locator))
        # Скроллим к элементу перед кликом, чтобы он точно был в зоне видимости
        self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
        card.click()

    def wait_for_url_to_contain(self, path: str) -> bool:
        """
        Ждет, пока URL не будет содержать ожидаемый путь.
        :param path: Часть URL, которую мы ожидаем (например, '/elements')
        :return: True, если URL изменился, иначе False (по таймауту).
        """
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.url_contains(path))
            return True
        except TimeoutException:
            return False

