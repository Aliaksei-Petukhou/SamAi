from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class PracticeFormPage:
    """
    Класс для страницы automation-practice-form
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
        
        # Form locators
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")
        self.gender_radio = "//label[text()='{}']"  # Male, Female, Other
        self.mobile_input = (By.ID, "userNumber")
        self.submit_button = (By.ID, "submit")
        
        # Modal locators
        self.modal_title = (By.ID, "example-modal-sizes-title-lg")
        self.modal_table_rows = (By.XPATH, "//div[@class='modal-body']//tbody/tr")

    def open(self):
        self.driver.get(self.url)
        # Убираем рекламу и футер, которые могут перекрывать кнопку
        self.driver.execute_script("document.getElementById('fixedban')?.remove(); document.querySelector('footer')?.remove();")
        return self

    def fill_form(self, first_name: str, last_name: str, email: str, mobile: str):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.mobile_input).send_keys(mobile)

    def select_gender(self, gender: str):
        gender_locator = (By.XPATH, self.gender_radio.format(gender))
        self.driver.find_element(*gender_locator).click()

    def submit(self):
        submit_btn = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        submit_btn.click()

    def get_modal_results(self) -> dict:
        """
        Собирает данные из таблицы в модальном окне.
        """
        results = {}
        rows = self.driver.find_elements(*self.modal_table_rows)
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                key = cells[0].text
                value = cells[1].text
                results[key] = value
        return results
