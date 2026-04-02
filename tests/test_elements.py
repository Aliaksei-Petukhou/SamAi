from pages.elements_page import ElementsPage

def test_text_box_form_submission(driver):
    """
    Проверяет полный цикл работы с формой Text Box:
    1. Открывает страницу /elements
    2. Выбирает меню Text Box
    3. Заполняет все поля формы
    4. Нажимает Submit
    5. Проверяет, что в итоговом блоке отображаются верные данные.
    """
    # === Подготовка данных ===
    elements_page = ElementsPage(driver)
    input_data = {
        "name": "John Doe",
        "email": "test@example.com",
        "current_address": "123 Main St",
        "permanent_address": "456 Other St"
    }

    # === Выполнение действий (Actions) ===
    elements_page.open()
    elements_page.select_text_box_menu()
    elements_page.fill_text_box_form(
        name=input_data["name"],
        email=input_data["email"],
        current_address=input_data["current_address"],
        permanent_address=input_data["permanent_address"]
    )
    elements_page.submit_form()
    
    # === Проверка результатов (Assertions) ===
    output_data = elements_page.get_output_data()

    assert output_data["name"] == input_data["name"]
    assert output_data["email"] == input_data["email"]
    assert output_data["current_address"] == input_data["current_address"]
    assert output_data["permanent_address"] == input_data["permanent_address"]
