import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import AttachmentType


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('yashaka/selene')
        s('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('yashaka/selene')).click()

    with allure.step('Открываем таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с номером 444'):
        s(by.partial_text('#444')).should(be.visible)

    with allure.step('Скриншот'):
        allure.attach(browser.driver.get_screenshot_as_png(), name='OK test 1', attachment_type=AttachmentType.PNG)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dzhafarovro")
@allure.feature("Задачи в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository()
    go_to_repository()
    open_issue()
    should_see_issue_with_number()
    allure_attach()


@ allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')


@ allure.step('Ищем репозиторий eroshenkoam/allure-example')
def search_for_repository():
    s('.header-search-input').click()
    s('.header-search-input').send_keys('eroshenkoam/allure-example')
    s('.header-search-input').submit()


@ allure.step('Переходим по ссылке репозитория eroshenkoam/allure-example')
def go_to_repository():
    s(by.link_text('eroshenkoam/allure-example')).click()


@ allure.step('Открываем таб Issues')
def open_issue():
    s('#issues-tab').click()


@ allure.step('Проверяем наличие Issue с номером 76')
def should_see_issue_with_number():
    s(by.partial_text('#76')).should(be.visible)


@ allure.step('Скиншот')
def allure_attach():
    allure.attach(browser.driver.get_screenshot_as_png(), name='OK test 2', attachment_type=AttachmentType.PNG)
