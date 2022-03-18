from features.pages.base_page import Page
from selenium.webdriver.common.by import By
from util.util import compare_data_with_expected


class LaunchPage(Page):
    SEARCH_BUTTON = (By.ID, "com.codepath.android.booksearch:id/search_button")
    SEARCH_INPUT = (
        By.ID, "com.codepath.android.booksearch:id/search_src_text")
    BOOK_LIST = (By.ID, "com.codepath.android.booksearch:id/lvBooks")
    BOOK_TITLE = (By.ID, "com.codepath.android.booksearch:id/tvTitle")

    def click_search_button(self):
        self.click_on_element(self.SEARCH_BUTTON)

    def do_search(self, text):
        self.input(text, self.SEARCH_INPUT)
        self.press_keycode(66)  # stands for Enter on Android's keyboard

    def verify_list_results(self):
        book_titles_list = self.find_elements(self.BOOK_TITLE)
        compare_data_with_expected(expected=8, real=len(book_titles_list))

    def click_list_first_item(self):
        book_titles_list = self.find_elements(self.BOOK_TITLE)
        book_titles_list[0].click()

    def click_exactly_book(self, text):
        books_list = self.find_elements(self.BOOK_TITLE)
        for book in books_list:
            if book.text == text:
                book.click()
                break


