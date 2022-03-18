from time import sleep
from behave import given, when, then


@given("I am at the launch page and click in the search bar")
def click_search_bar(context):
    context.app.launch_page.click_search_button()


@when('I search for "{text}" books')
def search_for_books(context, text):
    context.app.launch_page.do_search(text)


@then("I should see a list of books")
def verify_book_list(context):
    context.app.launch_page.verify_list_results()


@when("click for the first result")
def click_list_first_item(context):
    context.app.launch_page.click_list_first_item()


@then('I should see the publisher name "{text}"')
def verify_publisher_name(context, text):
    context.app.book_details_page.verify_publisher_name(text)


@then('I should see the book title "{text}"')
def verify_book_title(context, text):
    context.app.book_details_page.verify_book_title(text)


@when("I use the backpress button")
def back_from_details_to_list(context):
    context.app.book_details_page.back()


@then('click exaclty the book named "{text}"')
def click_exactly_book(context, text):
    context.app.launch_page.click_exactly_book(text)


@when("I click the share icon up-right the screen")
def click_details_page_share_icon(context):
    context.app.book_details_page.share_image()


@then("I should see the Android default share tray")
def verify_android_share_tray(context):
    context.app.book_details_page.verify_android_share_tray()
