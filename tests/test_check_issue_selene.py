from selene import by, have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_check_issue():
    browser.open("https://github.com/")

    s('.header-search-input').click().send_keys('OlgaZtv')
    s('.header-search-input').submit()

    s(by.link_text('OlgaZtv/OlgaZtv')).click()

    s('#issues-tab').should(have.text('Issues'))
    s('#issues-tab').click()

    s(by.partial_text('#1')).should(be.visible)
