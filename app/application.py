from features.pages.book_details_page import BookDetailsPage
from features.pages.launch_page import LaunchPage

class Application:
    def __init__(self, driver):
        self.launch_page = LaunchPage(driver)
        self.book_details_page = BookDetailsPage(driver)