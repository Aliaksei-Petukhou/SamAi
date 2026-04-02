import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания и закрытия экземпляра WebDriver для каждого теста.

    Эта фикстура будет автоматически вызываться для каждого теста,
    который принимает 'driver' в качестве аргумента.
    """
    # Given: Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()  # Открываем окно на весь экран
    driver.implicitly_wait(5)
    
    # Yield предоставляет драйвер тесту
    yield driver
    
    # Finally: Закрытие браузера после выполнения теста
    driver.quit()

