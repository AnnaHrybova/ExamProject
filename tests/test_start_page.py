"""Store tests for ForumTop"""
from time import sleep

import pytest
from selenium import webdriver

from conftest import BaseTest
from constants import start_page as start_page_constants
from pages.start_page import StartPage


class TestForum(BaseTest):
    """Tests for ForumTop"""

    @pytest.fixture(scope="function")
    def setup(self):
        driver = webdriver.Chrome(executable_path='C:/Users/Anita/PycharmProjects/pythonProject1/ExamProject/drivers/chromedriver.exe')
        driver.implicitly_wait(time_to_wait=20)
        # Open start page
        driver.get(start_page_constants.START_PAGE_URL)
        start_page = StartPage(driver)
        yield start_page
        self.logger.info("Open start page")
        driver.close()


    def test_empty_fields_login(self, setup):
        """
        - Open start page
        - Click on Sign In button
        - Clear password and login fields
        - Click on sign in
        - Verify error message
        """

        start_page = setup

        # Click on Sign In button
        start_page.click_sign_in_button()

        # Clear password and login fields
        start_page.fill_sign_in_fields(email="",password="")

        # Verify error message
        start_page.verify_error_message_text(error_xpath=start_page_constants.INVALID_LOGIN_ERROR_XPATH, error_text=start_page_constants.INVALID_LOGIN_ERROR_TEXT)
        self.logger.info('Error message was verified')

    def test_invalid_username_registration(self,setup):
        """
        - Open start page
        - Click on registration button
        - Verify site rules
        - Click on Accept button
        - Enter invalid username
        - Verify error message
        """

        start_page = setup

        # Click on registration button
        start_page.click_on_registration_button()

        # Verify site rules
        start_page.verify_site_rules()

        # Click on Accept button
        start_page.acceptance_button()

        # Enter invalid username
        start_page.invalid_username(username="op")

        # Verify error message
        start_page.verify_registration_error_message_text(error_xpath=start_page_constants.SIGN_UP_LOGIN_REGISTRATION_ERROR_XPATH,
                                             error_text=start_page_constants.SIGN_UP_LOGIN_REGISTRATION_ERROR_TEXT)
        self.logger.info('Error message was verified')
        sleep(2)

    def test_sign_out_user(self, setup):
        """
        - Open start page
        - Enter username and password
        - Click on Sign In button
        - Click on Sign Out button
        _ Verify that user was signed out
        """

        start_page = setup

        # Enter username and password
        start_page.fill_sign_in_fields(email="xot.bu.wo@gmail.com", password="Emely1!")

        # Verify user signed in successfully
        start_page.verify_sign_in_message_text(message_xpath=start_page_constants.AUTHORIZATION_MESSAGE_XPATH, message_text=start_page_constants.SIGN_IN_SUCCESSFUL_MESSAGE_TEXT)
        self.logger.info('Message was verified'),
        sleep(1)

        # Click on Sign Out button
        start_page.click_on_sign_out_button()

        # Verify that user was signed out
        start_page.verify_user_not_authorized()

    def test_add_to_favorite_option(self, setup):
        """
        - Open start page
        - Log in user
        - Find Forum
        - Add to favorite
        - Verify forum was added
        - Open forum rating list
        - Remove forum from list
        - Verify in profile empty forum list
        """
        start_page = setup

        # Log in user
        start_page.fill_sign_in_fields(email="xot.bu.wo@gmail.com", password="Emely1!")

        # Verify user signed in successfully
        start_page.verify_sign_in_message_text(message_xpath=start_page_constants.AUTHORIZATION_MESSAGE_XPATH,
                                               message_text=start_page_constants.SIGN_IN_SUCCESSFUL_MESSAGE_TEXT)
        self.logger.info('Message was verified'),
        sleep(1)

        # Find Forum
        start_page.find_rating_forum()

        # Add to favorite
        start_page.add_to_favorite()

        # Verify forum was added
        start_page.forum_was_added()

        # Open forum rating list
        start_page.rating_list()
        sleep(2)

        # Remove forum from list
        start_page.find_rating_forum_in_list()
        start_page.remove_from_favorite()

        # Verify in profile empty forum list
        start_page.verify_empty_forum_list()

    def test_add_comment(self,setup):
        """
        - Open start page
        - Login as user
        - Add comment on needed forum
        - Verify error message
        """
        start_page = setup

        # Login as user
        start_page.fill_sign_in_fields(email="xot.bu.wo@gmail.com", password="Emely1!")

        # Verify user signed in successfully
        start_page.verify_sign_in_message_text(message_xpath=start_page_constants.AUTHORIZATION_MESSAGE_XPATH,
                                               message_text=start_page_constants.SIGN_IN_SUCCESSFUL_MESSAGE_TEXT)
        self.logger.info("Message was verified"),
        sleep(1)

        # Add comment on needed forum
        start_page.add_comment_button()

        start_page.enter_comment()

        # Verify error message
        start_page.verify_add_comment_message(error_xpath=start_page_constants.ENTER_FIELD_ERROR_XPATH, error_text=start_page_constants.ENTER_FIELD_ERROR_TEXT)
        self.logger.info("Error message was verified")