"""
This module contains GoogleSearchPage,
the page object for the Google search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    # URL

    URL = 'https://www.google.com/'

    # Locators

    SEARCH_INPUT = (By.NAME, 'q')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
