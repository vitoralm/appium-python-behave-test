from features.pages.base_page import Page
from selenium.webdriver.common.by import By
from util.util import compare_data_with_expected


class LaunchPage(Page):
    SEARCH_BUTTON = (By.ID, "com.codepath.android.booksearch:id/search_button")
    SEARCH_INPUT = (
        By.ID, "com.codepath.android.booksearch:id/search_src_text")
    BOOK_LIST = (By.ID, "com.codepath.android.booksearch:id/lvBooks")
    BOOK_TITLE = (By.ID, "com.codepath.android.booksearch:id/tvTitle")

    def load_book_list(self):
        return self.find_elements(self.BOOK_TITLE)

    def click_search_button(self):
        self.click_on_element(self.SEARCH_BUTTON)

    def do_search(self, text):
        self.input(text, self.SEARCH_INPUT)
        self.press_keycode(66)  # stands for Enter on Android's keyboard

    def verify_list_results(self):
        book_titles_list = self.find_elements(self.BOOK_TITLE)
        compare_data_with_expected(
            expected=True, real=(len(book_titles_list) > 0))

    def click_list_first_item(self):
        book_titles_list = self.find_elements(self.BOOK_TITLE)
        book_titles_list[0].click()

    def click_exactly_book(self, text):
        book_list = self.load_book_list()

        book_found = False
        list_end = False
        book_list_last_el = self.find_element(self.BOOK_TITLE)

        while (book_found or not list_end):
            if book_list_last_el == book_list[-1]:
                list_end = True

            for book in book_list:
                if book.text == text:
                    book.click()
                    book_found = True
                    break

            if book_found:
                break

            self.scroll_down()

            book_list_size = len(book_list)
            book_list_last_el = book_list[book_list_size - 1]
            book_list = self.load_book_list()

        assert book_found
