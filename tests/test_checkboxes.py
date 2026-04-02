from pages.checkboxes_page import CheckboxesPage

def test_checkbox_interaction(driver):
    """
    Проверяет взаимодействие с чекбоксами:
    1. Убеждается, что первый чекбокс не отмечен, и отмечает его.
    2. Убеждается, что второй чекбокс отмечен, и снимает с него отметку.
    """
    # Given: Открываем страницу с чекбоксами
    checkboxes_page = CheckboxesPage(driver).open()
    
    # When: Получаем список чекбоксов
    checkboxes = checkboxes_page.get_checkboxes()
    assert len(checkboxes) == 2, "На странице должно быть два чекбокса"

    checkbox1, checkbox2 = checkboxes[0], checkboxes[1]

    # Then: Проверяем и меняем состояние первого чекбокса
    assert not checkbox1.is_selected(), "Чекбокс 1 изначально должен быть не отмечен"
    checkbox1.click()
    assert checkbox1.is_selected(), "Чекбокс 1 должен был стать отмеченным"

    # And: Проверяем и меняем состояние второго чекбокса
    assert checkbox2.is_selected(), "Чекбокс 2 изначально должен быть отмечен"
    checkbox2.click()
    assert not checkbox2.is_selected(), "Чекбокс 2 должен был стать не отмеченным"
