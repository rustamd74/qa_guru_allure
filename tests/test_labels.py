import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('')
    allure.dynamic.story('')
    allure.dynamic.link('https://github.com', name='Testing')
