import pytest
from pages.demoqa_home_page import DemoQaHomePage

# Список из 6 категорий, которые мы будем проверять.
CATEGORIES = [
    "Elements",
    "Forms",
    "Alerts, Frame & Windows",
    "Widgets",
    "Interactions",
    "Book Store Application"
]

# Словарь для сопоставления названий категорий и ожидаемых путей в URL
URL_PATHS = {
    "Elements": "/elements",
    "Forms": "/forms",
    "Alerts, Frame & Windows": "/alertsWindows",
    "Widgets": "/widgets",
    "Interactions": "/interaction",
    "Book Store Application": "/books"
}

@pytest.mark.xfail(reason="This test is flaky due to website instability")
@pytest.mark.parametrize("category_name", CATEGORIES)
def test_category_card_navigation(driver, category_name):
    """
    Параметризованный тест для проверки навигации по карточкам категорий.
    Проверяет, что URL изменяется корректно после клика.
    """
    # Given
    home_page = DemoQaHomePage(driver).open()

    # When
    home_page.click_category_card(category_name)

    # Then
    expected_path = URL_PATHS[category_name]
    assert home_page.wait_for_url_to_contain(expected_path), f"URL не содержит '{expected_path}' для категории '{category_name}'"

