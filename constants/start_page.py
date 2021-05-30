"""Locators"""

SIGN_IN_LOGIN_FIELD_XPATH = '//input[@name="login"]'
SIGN_IN_PASSWORD_FIELD_XPATH = '//input[@name="password"]'
SIGN_IN_BUTTON_XPATH = "//a[@href='javascript:void(0);']"
INVALID_LOGIN_ERROR_TEXT = "Пользователь с таким адресом и паролем не найден"

START_PAGE_URL = 'https://forum-top.ru/'


INVALID_LOGIN_ERROR_XPATH = f"//*[contains(text(), '{INVALID_LOGIN_ERROR_TEXT}')]"


SIGN_UP_BUTTON = "//a[contains(text(),'Регистрация')]"
SIGN_UP_REGISTRATION_RULES_XPATH = "//h3[contains(text(),'Правила участия в рейтинге')]"
SIGN_UP_REGISTRATION_RULES_TEXT = "Правила участия в рейтинге"
SIGN_UP_ACCEPT_RULES_BUTTON = "//a[@onclick='reg.go_step(2);']"
SIGN_UP_LOGIN_REGISTRATION_ERROR_TEXT = "Пожалуйста, введите не меньше 3 символов."
SIGN_UP_LOGIN_REGISTRATION_ERROR_XPATH = f"//*[contains(text(),'{SIGN_UP_LOGIN_REGISTRATION_ERROR_TEXT}')]"
SIGN_UP_LOGIN_REGISTRATION_XPATH = "//input[@id='name']"
SIGN_UP_EMAIL_REGISTRATION_XPATH = "//input[@id='email']"
LOG_OUT_BUTTON = "//a[@href='/logout/']"
ADD_TO_FAVORITE_BUTTON_XPATH = "//a[@onclick='forum_fav(4546);']"
PROFILE_FAVORITE_FORUM_BUTTON = "//a[@href='/favorites/']"
RATING_OF_FORUMS_BUTTON = "//img[@src='/img/logo-top2.png']"

AUTHORIZATION_MESSAGE_XPATH = "//div[@class='jGrowl-notification']"
SIGN_IN_SUCCESSFUL_MESSAGE_TEXT = "Авторизация прошла успешно"

RATING_FORUM_TO_FOLLOW_XPATH = "//a[@href='https://forum-top.ru/forum/enteros.rusff.me']"
RATING_FORUM_TO_FOLLOW_TEXT = "Энтерос"
LIST_OF_RATING_FORUMS = "//div[@class ='right-container']"
NOTIFICATION_WINDOW = "//div[@class='jGrowl-notification']"
PROFILE_FAVORITE_EMPTY_LIST_XPATH = "//div[contains(text(),'В списке нет ни одного добавленного форума.')]"
PROFILE_FAVORITE_EMPTY_LIST_TEXT = "В списке нет ни одного добавленного форума."

# "//div[@class='content-block-inner']"
# "//div[contains(text(),'В списке нет ни одного добавленного форума.')]"
ADD_COMMENT_BUTTON = "//a[@href='/forum/enteros.rusff.me/#comments']"
NEW_COMMENT_BUTTON = "//a[@class='user_comment_head']"
ENTER_FIELD_XPATH = "//textarea[@class='add_input']"
ENTER_FIELD_TEXT = "Cool"
ENTER_FIELD_ERROR_XPATH = "//label[@class='error']"
ENTER_FIELD_ERROR_TEXT = "Пожалуйста, введите не менее 5 символов."
COMMENT_BUTTON = "//a[@class='button new_comment']"
OPTION_TAB = "//ul[@class='ul-right-content']"
RATING_FORUM_TO_REMOVE = "//div[@id='forum_row_4546']"
