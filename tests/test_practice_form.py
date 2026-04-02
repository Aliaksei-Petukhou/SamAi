from pages.practice_form_page import PracticeFormPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_practice_form_submission(driver):
    """
    Проверяет успешную отправку формы Practice Form и валидацию данных в модальном окне.
    """
    # === Подготовка данных ===
    practice_form_page = PracticeFormPage(driver)
    input_data = {
        "first_name": "Alex",
        "last_name": "Petrov",
        "email": "test@example.com",
        "gender": "Male",
        "mobile": "1234567890"
    }

    # === Выполнение действий (Actions) ===
    practice_form_page.open()
    practice_form_page.fill_form(
        first_name=input_data["first_name"],
        last_name=input_data["last_name"],
        email=input_data["email"],
        mobile=input_data["mobile"]
    )
    practice_form_page.select_gender(input_data["gender"])
    practice_form_page.submit()

    # === Проверка результатов (Assertions) ===
    # Явное ожидание появления модального окна
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(practice_form_page.modal_title))
    
    # Получаем результаты из модального окна
    results = practice_form_page.get_modal_results()

    # Проверяем, что данные совпадают
    assert results["Student Name"] == f'{input_data["first_name"]} {input_data["last_name"]}'
    assert results["Student Email"] == input_data["email"]
    assert results["Gender"] == input_data["gender"]
    assert results["Mobile"] == input_data["mobile"]
