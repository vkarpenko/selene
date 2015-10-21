from selenium.webdriver.common.by import By

__author__ = 'ayia'


def by(css_selector):
    return by_css(css_selector)


def by_css(css_selector):
    return (By.CSS_SELECTOR, css_selector)


def by_xpath(xpath):
    print xpath
    return (By.XPATH, xpath)


def by_text(element_text):
    print escape_text_quotes_for_xpath(element_text)
    return by_xpath('.//*/text()[normalize-space(.) = '
                    + escape_text_quotes_for_xpath(element_text)
                    + ']/parent::*')


def with_text(element_text):
    return by_xpath('.//*/text()[contains(normalize-space(.), '
                    + escape_text_quotes_for_xpath(element_text)
                    + ')]/parent::*')


def escape_text_quotes_for_xpath(text):
    return 'concat("%s")' % (
        str(
            "\", '\"', \"".join(
                text.split('"'))))
