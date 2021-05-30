"""Encapsulate actions related to start page"""

import logging
from time import sleep

from selenium.webdriver.common.by import By
from constants import start_page
from helpers.base import wait_until_ok
from pages.base import BasePage


class StartPage(BasePage):
    """Class stores actions and verification related to start page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def click_sign_in_button(self):
        """Click on Sign In button"""
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.SIGN_IN_BUTTON_XPATH)
        self.logger.info("Button was clicked")

    def fill_sign_in_fields(self, email, password):
        """Fill specified fields using passed values"""
        # self.wait_until_find(locator_type=By.XPATH, locator=start_page.SIGN_IN_LOGIN_FIELD_XPATH)
        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SIGN_IN_LOGIN_FIELD_XPATH, data=email)
        self.logger.info("Set login value: '%s'", email)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SIGN_IN_PASSWORD_FIELD_XPATH, data=password)
        self.logger.info("Set password value: '%s'", password)

        # Click on Sign In
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.SIGN_IN_BUTTON_XPATH)
        self.logger.info("Sign In button was clicked")

    def verify_error_message_text(self, error_xpath, error_text):
        """Find error and verify message"""
        self.wait_for_text(locator_type=By.XPATH, locator=error_xpath, text=error_text)
        sleep(1)
        message = self.wait_until_find(locator_type=By.XPATH, locator=error_xpath).text
        assert message == error_text, f"Actual message: {message}"
        self.logger.info("Error message was verified")

    def click_on_registration_button(self):
        """Enter invalid username and verify error message"""
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.SIGN_UP_BUTTON)
        self.logger.info("Registration button was clicked")

    def verify_site_rules(self):
        self.wait_for_text(locator_type=By.XPATH, locator=start_page.SIGN_UP_REGISTRATION_RULES_XPATH,text=start_page.SIGN_UP_REGISTRATION_RULES_TEXT)
        self.logger.info("Registration rules appeared on start page")
        sleep(2)

    def acceptance_button(self):
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.SIGN_UP_ACCEPT_RULES_BUTTON)
        self.logger.info("Acceptance button was clicked")
        sleep(2)

    def invalid_username(self, username):
        """Enter invalid username"""
        self.wait_until_find(locator_type=By.XPATH, locator=start_page.SIGN_UP_LOGIN_REGISTRATION_XPATH)
        self.logger.info("Login field was found")
        sleep(2)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SIGN_UP_LOGIN_REGISTRATION_XPATH, data=username)
        self.logger.info("Set login value: '%s'", username)
        sleep(1)
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.SIGN_UP_EMAIL_REGISTRATION_XPATH)
        self.logger.info("Email field was clicked")

    def verify_registration_error_message_text(self, error_xpath, error_text):
        """Find error and verify message"""
        self.wait_for_text(locator_type=By.XPATH, locator=error_xpath, text=error_text)
        sleep(2)
        message = self.wait_until_find(locator_type=By.XPATH, locator=error_xpath).text
        assert message == error_text, f"Actual message: {message}"
        self.logger.info("Error message was verified")

    def verify_sign_in_message_text(self, message_xpath, message_text):
        """Find error and verify message"""
        self.wait_until_find(locator_type=By.XPATH, locator=start_page.AUTHORIZATION_MESSAGE_XPATH)
        self.logger.info("Pop up window was opened")

    @wait_until_ok(timeout=30)
    def click_on_sign_out_button(self):
        """Click on sign out button"""
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.LOG_OUT_BUTTON)
        self.logger.info("Sign out button was clicked")

    @wait_until_ok(timeout=30)
    def verify_user_not_authorized(self):
        """Click on Add to favorite button"""
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.ADD_TO_FAVORITE_BUTTON_XPATH)
        self.logger.info("Button Add to favorite was clicked")
        sleep(2)

        self.wait_until_find(locator_type=By.XPATH, locator=start_page.AUTHORIZATION_MESSAGE_XPATH)
        self.logger.info("Pop up window was opened")

    def find_rating_forum(self):
        """Find rating forum"""
        self.wait_until_find(locator_type=By.XPATH, locator=start_page.LIST_OF_RATING_FORUMS)
        self.wait_for_text(locator_type=By.XPATH, locator=start_page.RATING_FORUM_TO_FOLLOW_XPATH, text=start_page.RATING_FORUM_TO_FOLLOW_TEXT)
        self.logger.info("Forum was found")
        sleep(2)

    def add_to_favorite(self):
        """Click on Add to favorite"""
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.ADD_TO_FAVORITE_BUTTON_XPATH)
        self.logger.info("Button Add to favorite was clicked")
        sleep(2)
        self.wait_until_find(locator_type=By.XPATH, locator=start_page.NOTIFICATION_WINDOW)
        self.logger.info("Pop up window was opened")
        sleep(3)

    def forum_was_added(self):
        """Click on profile and verify"""
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.PROFILE_FAVORITE_FORUM_BUTTON)
        self.logger.info("Button in profile was clicked")

        self.wait_until_find(locator_type=By.XPATH, locator=start_page.RATING_FORUM_TO_FOLLOW_XPATH)
        self.logger.info("Forum was added to profile favorite")

    def rating_list(self):
        """Click on forum list button"""
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.RATING_OF_FORUMS_BUTTON)
        self.logger.info("Forum button was clicked")

    def find_rating_forum_in_list(self):
        """Find rating forum"""
        self.wait_until_find(locator_type=By.XPATH, locator=start_page.LIST_OF_RATING_FORUMS)
        # return StartPage(self.driver)
        self.logger.info("List of forums was found and opened")
        sleep(2)

    @wait_until_ok(timeout=55)
    def remove_from_favorite(self):
        """Click on add to favorite"""
        self.wait_until_find(locator_type=By.XPATH, locator=start_page.RATING_FORUM_TO_REMOVE)
        self.logger.info("Forum for removing was found")
        sleep(5)

        self.wait_until_find(locator_type=By.XPATH, locator=start_page.ADD_TO_FAVORITE_BUTTON_XPATH)
        self.logger.info("Tab was found")
        sleep(5)
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.ADD_TO_FAVORITE_BUTTON_XPATH)
        self.logger.info("Button remove from favorite was clicked")

        self.wait_until_find(locator_type=By.XPATH, locator=start_page.NOTIFICATION_WINDOW)
        self.logger.info("Pop up window was opened")

    @wait_until_ok(timeout=50)
    def verify_empty_forum_list(self):
        """Open profile and verify it is empty"""
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.PROFILE_FAVORITE_FORUM_BUTTON)
        self.logger.info("Button in profile was clicked")

        forum_list = self.wait_until_find(locator_type=By.XPATH, locator=start_page.PROFILE_FAVORITE_EMPTY_LIST_XPATH).text
        assert forum_list == start_page.PROFILE_FAVORITE_EMPTY_LIST_TEXT, f"Actual message: {forum_list}"
        self.logger.info("Empty forum list was verified")

    def add_comment_button(self):
        """Find forum and click on add comment button"""
        self.wait_until_find(locator_type=By.XPATH, locator=start_page.LIST_OF_RATING_FORUMS)
        self.wait_for_text(locator_type=By.XPATH, locator=start_page.RATING_FORUM_TO_FOLLOW_XPATH,
                           text=start_page.RATING_FORUM_TO_FOLLOW_TEXT)
        self.logger.info("List of forums was found and opened")

        self.wait_until_click(locator_type=By.XPATH, locator=start_page.ADD_COMMENT_BUTTON)
        self.logger.info("Button add comment was clicked")

    def enter_comment(self):
        """Enter comment """
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.NEW_COMMENT_BUTTON)
        self.logger.info("New comment button was clicked")

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.ENTER_FIELD_XPATH, data=start_page.ENTER_FIELD_TEXT)
        self.logger.info("Text was entered")

        self.wait_until_click(locator_type=By.XPATH, locator=start_page.COMMENT_BUTTON)
        self.logger.info("Comment button was clicked")

    def verify_add_comment_message(self, error_xpath, error_text):
        """Verify error message"""
        self.wait_for_text(locator_type=By.XPATH, locator=error_xpath, text=error_text)
        message = self.wait_until_find(locator_type=By.XPATH, locator=error_xpath).text
        assert message == error_text, f"Actual message: {message}"
        self.logger.debug("Error message was verified")
