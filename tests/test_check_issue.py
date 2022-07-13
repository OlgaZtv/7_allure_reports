import allure
from selene import have, by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_check_issue():
    with allure.step('Открываем главную страницу'):
        browser.open("https://github.com/")

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click().send_keys('OlgaZtv')
        s('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('OlgaZtv/OlgaZtv')).click()

    with allure.step('Открываем таб Issues'):
        s('#issues-tab').should(have.text('Issues'))
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с номером {id}'):
        s(by.partial_text('1').should(be.visible))
