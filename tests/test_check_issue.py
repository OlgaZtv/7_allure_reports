import allure
from allure_commons.types import Severity
from selene import have, by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from test_attachments import test_attachments

allure.dynamic.tag("web")
allure.dynamic.severity(Severity.MINOR)
allure.dynamic.feature("Задача проверки Issue")
allure.dynamic.story("Проверяем Issue в нашем репозитории")
allure.dynamic.link("https://github.com", name="OlgaZtv")


def test_check_issue_dynamic_steps():
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

    with allure.step('Проверяем наличие Issue с номером 1'):
        s(by.partial_text('#1')).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "OlgaZtv")
@allure.feature("Задача проверки Issue")
@allure.story("Проверяем Issue в нашем репозитории")
@allure.link("https://github.com", name="OlgaZtv")
def test_check_issue_decorator_steps():
    open_main_page()
    search_for_repository('OlgaZtv')
    go_to_repository('OlgaZtv/OlgaZtv')
    open_issue_tab()
    should_see_issue_with_number('1')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open("https://github.com/")


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click().send_keys(repo)
    s('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория {repo_link}')
def go_to_repository(repo_link):
    s(by.link_text(repo_link)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    s('#issues-tab').should(have.text('Issues'))
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text('#' + number)).should(be.visible)
