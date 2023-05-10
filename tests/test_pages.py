from pages.authorization_page import AuthPage
from data.locators import AuthorizationLocators, RegistrationLocators, PasswordRecoveryLocators, AgrLocators, \
    SocialLocators
import pytest
from data import invalid_data, messages, valid_data


################# 1.Тест загрузки страницы регистрации ####################

def test_load_reg_page_positive(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.link_registration)
    assert 'registration' in page.get_current_url()
    assert page.get_text_from_element(RegistrationLocators.reg_title) == 'Регистрация'


################# 2. Тест загрузки страницы авторизации ####################

def test_load_auth_page_positive(browser):
    page = AuthPage(browser)
    page.go_to_site()
    assert 'https://b2c.passport.rt.ru/' in page.get_current_url()
    assert page.get_text_from_element(AuthorizationLocators.auth_title) == 'Авторизация'


################# 3. Тест загрузки страницы восстановления пароля ####################

def test_load_forgot_pass_page_positive(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.link_forgot_pass)
    assert 'login-actions/reset-credentials' in page.get_current_url()
    assert page.get_text_from_element(PasswordRecoveryLocators.pass_title) == 'Восстановление пароля'


################# 4. Тест смены типов логина на странице авторизации ####################

@pytest.mark.parametrize('locator, expected',
                         [(AuthorizationLocators.tab_mail, 'Электронная почта'),
                          (AuthorizationLocators.tab_login, 'Логин'),
                          (AuthorizationLocators.tab_pers_account, 'Лицевой счёт'),
                          (AuthorizationLocators.tab_phone, 'Мобильный телефон')])
def test_change_tabs_auth_page_positive(browser, locator, expected):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(locator)
    assert page.get_text_from_element(AuthorizationLocators.login_placeholder) == expected


#########################################################################
################# Блок негативных тестов регистрации ####################
#########################################################################

################# 5. Тест регистрации нового пользователя без указания учетных данных ####################

def test_reg_user_without_data_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.link_registration)
    reg_url = page.get_current_url()
    page.click_reg_btn()
    assert reg_url == page.get_current_url()


################# 6. Тест регистрации нового пользователя c указанием адреса почты в неверном формате ####################

@pytest.mark.parametrize('email', invalid_data.incorrect_emails)
def test_reg_invalid_email_negative(browser, email):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.reg_login, email)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_login_message


################# 7. Тест регистрации нового пользователя c указанием пароля в неверном формате ####################

@pytest.mark.parametrize('password', invalid_data.incorrect_passwords)
def test_reg_invalid_password_negative(browser, password):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.reg_password, password)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_password_message


################# 8. Тест регистрации нового пользователя c указанием номера телефона в неверном формате ####################

@pytest.mark.parametrize('phone', invalid_data.incorrect_phones)
def test_reg_invalid_phone_negative(browser, phone):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.reg_login, phone)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_login_message


################# 9. Тест регистрации нового пользователя c указанием имени в неверном формате ####################

@pytest.mark.parametrize('name', invalid_data.incorrect_names)
def test_reg_invalid_name_negative(browser, name):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.name, name)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_name_message


################# 10. Тест регистрации нового пользователя c указанием фамилии в неверном формате ####################

@pytest.mark.parametrize('surname', invalid_data.incorrect_surnames)
def test_reg_invalid_surname_negative(browser, surname):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.surname, surname)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_surname_message


#########################################################################
###################### Блок тестов авторизации ##########################
#########################################################################

################# 11. Тест авторизации пользователя с валидными учетными данными ####################

@pytest.mark.parametrize('login', valid_data.correct_logins)
def test_auth_user_with_valid_email_positive(browser, login):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthorizationLocators.auth_login, login)
    page.enter_data(AuthorizationLocators.auth_pass, valid_data.correct_pass)
    page.click_enter_btn()


################# 12. Тест авторизации пользователя с невалидным адресом почты и валидным паролем ####################

def test_auth_user_with_invalid_mail_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthorizationLocators.auth_login, invalid_data.incorrect_email)
    page.enter_data(AuthorizationLocators.auth_pass, valid_data.correct_pass)
    page.click_enter_btn()
    assert page.get_text_from_element(
        AuthorizationLocators.auth_error) == messages.wrong_login_or_pass_message or messages.wrong_capcha_message


################# 13. Тест авторизации пользователя с невалидным невалидным номером телефона и валидным паролем ####################

def test_auth_user_with_invalid_phone_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthorizationLocators.auth_login, invalid_data.incorrect_phone)
    page.enter_data(AuthorizationLocators.auth_pass, valid_data.correct_pass)
    page.click_enter_btn()
    assert page.get_text_from_element(
        AuthorizationLocators.auth_error) == messages.wrong_login_or_pass_message or messages.wrong_capcha_message


################# 14. Тест авторизации пользователя с валидным логином и невалидным паролем ####################

@pytest.mark.parametrize('login', valid_data.correct_logins)
def test_auth_user_with_invalid_pass_negative(browser, login):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthorizationLocators.auth_login, login)
    page.enter_data(AuthorizationLocators.auth_pass, invalid_data.incorrect_pass)
    page.click_enter_btn()
    assert page.get_text_from_element(
        AuthorizationLocators.auth_error) == messages.wrong_login_or_pass_message or messages.wrong_capcha_message


#########################################################################
###################### Блок тестов авторизации с помошью социальных сетей ##########################
#########################################################################


################# 15. Тест авторизации пользователя при помощи учетной записи yandex с указанием невалидных учетных данных ####################

def test_auth_with_yandex_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.icon_yandex)
    page.enter_data(SocialLocators.yandex_login, invalid_data.incorrect_login_yandex)
    page.click_link(SocialLocators.yandex_submit_btn)
    assert page.get_text_from_element(SocialLocators.yandex_error_message) == messages.yandex_wrong_message
    assert 'passport.yandex.ru' in page.get_current_url()

################# 16. Тест авторизации пользователя при помощи учетной записи google с указанием невалидных учетных данных ####################

def test_auth_with_google_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.icon_google)
    page.enter_data(SocialLocators.google_login, invalid_data.incorrect_email)
    page.click_link(SocialLocators.google_submit_btn)
    assert page.get_text_from_element(SocialLocators.google_error_message) == messages.google_wrong_message
    assert 'accounts.google.com' in page.get_current_url()

################# 17. Тест авторизации пользователя при помощи учетной записи mail.ru с указанием невалидных учетных данных ####################

def test_auth_with_mail_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.icon_male)
    page.enter_data(SocialLocators.mail_login, invalid_data.incorrect_email)
    page.enter_data(SocialLocators.mail_pass, invalid_data.incorrect_pass)
    page.click_link(SocialLocators.mail_submit_btn)
    assert page.get_text_from_element(SocialLocators.mail_error_message) == messages.mail_wrong_message
    assert 'connect.mail.ru' in page.get_current_url()

################# 18. Тест авторизации пользователя при помощи учетной записи ok с указанием невалидных учетных данных ####################

def test_auth_with_ok_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.icon_ok)
    page.enter_data(SocialLocators.ok_login, invalid_data.incorrect_email)
    page.enter_data(SocialLocators.ok_pass, invalid_data.incorrect_pass)
    page.click_link(SocialLocators.ok_submit_btn)
    assert page.get_text_from_element(SocialLocators.ok_error_message) == messages.ok_wrong_message
    assert 'connect.ok.ru' in page.get_current_url()

################# 19. Тест авторизации пользователя при помощи учетной записи vk с указанием невалидных учетных данных ####################

def test_auth_with_vk_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthorizationLocators.icon_vk)
    page.enter_data(SocialLocators.vk_login, invalid_data.incorrect_email)
    page.enter_data(SocialLocators.vk_pass, invalid_data.incorrect_pass)
    page.click_link(SocialLocators.vk_submit_btn)
    assert page.get_text_from_element(SocialLocators.vk_error_message) == messages.vk_wrong_message
    assert 'oauth.vk.com' in page.get_current_url()


#==============================================================================================

################# 20. Тест работоспособности ссылки на пользовательское соглашение и политику конфиденциальности ####################

def test_agreement_link_positive(browser):
    page = AuthPage(browser)
    page.get(valid_data.agreement_url)
    assert page.get_text_from_element(AgrLocators.agr_title) == valid_data.agreement_title
