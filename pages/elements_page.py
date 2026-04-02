from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ElementsPage:
    """
    Класс для страницы /elements и ее разделов, например, Text Box.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://demoqa.com/elements"
        
        # Locators for the Text Box form
        self.text_box_menu_item = (By.XPATH, "//span[text()='Text Box']")
        self.full_name_input = (By.ID, "userName")
        self.email_input = (By.ID, "userEmail")
        self.current_address_input = (By.ID, "currentAddress")
        self.permanent_address_input = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")
        
        # Locators for the output
        self.output_name = (By.ID, "name")
        self.output_email = (By.ID, "email")
        self.output_current_address = (By.CSS_SELECTOR, "p#currentAddress")
        self.output_permanent_address = (By.CSS_SELECTOR, "p#permanentAddress")

    def open(self):
        """
        Открывает страницу /elements.
        """
        self.driver.get(self.url)
        return self

    def select_text_box_menu(self):
        """
        Кликает на пункт меню "Text Box".
        """
        self.driver.find_element(*self.text_box_menu_item).click()

    def fill_text_box_form(self, name: str, email: str, current_address: str, permanent_address: str):
        """
        Заполняет все поля в форме Text Box.
        """
        self.driver.find_element(*self.full_name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.current_address_input).send_keys(current_address)
        self.driver.find_element(*self.permanent_address_input).send_keys(permanent_address)

    def submit_form(self):
        """
        Нажимает на кнопку Submit.
        """
        submit_btn = self.driver.find_element(*self.submit_button)
        # Скроллим к кнопке, так как она может быть за пределами экрана
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        submit_btn.click()

    def get_output_data(self) -> dict:
        """
        Собирает данные из блока с результатами.
        Возвращает словарь с обработанными данными.
        """
        name = self.driver.find_element(*self.output_name).text.split(':')[1]
        email = self.driver.find_element(*self.output_email).text.split(':')[1]
        current_addr = self.driver.find_element(*self.output_current_address).text.split(':')[1]
        perm_addr = self.driver.find_element(*self.output_permanent_address).text.split(':')[1]
        
        return {
            "name": name,
            "email": email,
            "current_address": current_addr,
            "permanent_address": perm_addr
        }
