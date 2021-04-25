"""
These tests cover Google searches.
"""

import pytest

# from pages.result import GoogleResultPage
# from pages.search import GoogleSearchPage
from POM_Template.pages.result import GoogleResultPage
from POM_Template.pages.search import GoogleSearchPage


@pytest.mark.parametrize('phrase', ['selenium', 'python', 'pytest'])
def test_basic_google_search(browser, phrase):
    search_page = GoogleSearchPage(browser)
    result_page = GoogleResultPage(browser)

    # Given the Google home page is displayed
    search_page.load()

    # When the user searches for the phrase
    search_page.search(phrase)

    # Then the search result query is the phrase
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to the phrase
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains the phrase
    # (Putting this assertion last guarantees that the page title will be ready)
    assert phrase in result_page.title()
