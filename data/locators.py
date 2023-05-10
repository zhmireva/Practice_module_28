# Классы локаторов

from selenium.webdriver.common.by import By

class RegistrationLocators:
    name = (By.NAME, 'firstName')
    surname = (By.NAME, 'lastName')
    reg_title = (By.TAG_NAME, 'h1')
    reg_login = (By.ID, 'address')
    reg_password = (By.ID, 'password')
    reg_password_confirm = (By.ID, 'password-confirm')
    reg_btn = (By.NAME, 'register')
    reg_error = (By.XPATH, '//span[contains(@class, "rt-input-container__meta--error")]')

class AuthorizationLocators:
    auth_title = (By.TAG_NAME, 'h1')
    auth_login = (By.ID, 'username')
    auth_pass = (By.ID, 'password')
    btn_enter = (By.ID, "kc-login")
    login_placeholder = (
    By.XPATH, '//div[contains(@class, "tabs-input-container__login")]//span[@class="rt-input__placeholder"]')
    tab_phone = (By.ID, 't-btn-tab-phone')
    tab_mail = (By.ID, "t-btn-tab-mail")
    tab_login = (By.ID, "t-btn-tab-login")
    tab_pers_account = (By.ID, "t-btn-tab-ls")
    link_forgot_pass = (By.ID, "forgot_password")
    link_registration = (By.ID, "kc-register")
    link_agreement = (By.ID, "rt-footer-agreement-link")
    icon_vk = (By.ID, "oidc_vk")
    icon_ok = (By.ID, "oidc_ok")
    icon_male = (By.ID, "oidc_mail")
    icon_google = (By.ID, "oidc_google")
    icon_yandex = (By.ID, "oidc_ya")
    auth_error = (By.ID, 'form-error-message')

class AgrLocators:
    agr_title = (By.CLASS_NAME, 'offer-title')

class SocialLocators:
    vk_login = (By.NAME, 'email')
    vk_pass = (By.NAME, 'pass')
    vk_submit_btn = (By.ID, 'install_allow')
    vk_error_message = (By.CLASS_NAME, 'box_error')
    ok_login = (By.ID, 'field_email')
    ok_pass = (By.ID, 'field_password')
    ok_submit_btn = (By.CLASS_NAME, 'form-actions_yes')
    ok_error_message = (By.CLASS_NAME, 'input-e')
    mail_login = (By.ID, 'login')
    mail_pass = (By.ID, 'password')
    mail_submit_btn = (By.CLASS_NAME, 'ui-button-main')
    mail_error_message = (By.CLASS_NAME, 'login-form__error')
    google_login = (By.ID, 'identifierId')
    google_submit_btn = (By.XPATH, '//button[contains(@class, "AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b")]')
    google_error_message = (By.CLASS_NAME, 'o6cuMc')
    yandex_login = (By.ID, 'passp-field-login')
    yandex_submit_btn = (By.ID, 'passp:sign-in')
    yandex_error_message = (By.ID, 'field:input-login:hint')

class PasswordRecoveryLocators:
    pass_title = (By.TAG_NAME, 'h1')
    pass_login = (By.ID, 'username')
    pass_btn = (By.ID, 'reset')
    pass_error = (By.ID, 'form-error-message')
