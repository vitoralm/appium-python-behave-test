from cmath import exp
import pdb
from features.pages.base_page import Page
from selenium.webdriver.common.by import By
from util.util import compare_data_with_expected


class BookDetailsPage(Page):
    PUBLISHER_NAME = (By.ID, "com.codepath.android.booksearch:id/tvPublisher")
    BOOK_TITLE = (By.ID, "com.codepath.android.booksearch:id/tvTitle")
    ANDROID_SHARE_ICON = (
        By.ID, "com.codepath.android.booksearch:id/action_share")
    ANDROID_SHARE_TRAY = (By.ID, "android:id/resolver_list")
    ANDROID_SHARE_LABEL = (By.ID, "android:id/title")

    def verify_publisher_name(self, name):
        publisher = self.find_element(self.PUBLISHER_NAME)
        compare_data_with_expected(expected=name, real=publisher.text)

    def verify_book_title(self, name):
        book_title = self.find_element(self.BOOK_TITLE)
        compare_data_with_expected(expected=name, real=book_title.text)

    def share_image(self):
        share_button = self.find_element(self.ANDROID_SHARE_ICON)
        share_button.click()

    def verify_android_share_tray(self):
        share_label = self.find_element(self.ANDROID_SHARE_LABEL)
        compare_data_with_expected(
            expected="Share Image", real=share_label.text)
        
        share_tray = self.find_element(self.ANDROID_SHARE_TRAY)
        compare_data_with_expected(expected=True, real=bool(share_tray.is_displayed()))

    def back_press(self):
        self.driver.back()
