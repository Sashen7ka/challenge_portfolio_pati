from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@name='password']"
    sign_in_button_xpath = "//span[@class='MuiButton-label']"
    language_button_xpath = "//div[contains(@class, 'MuiInputBase-input MuiInput-input')]"
    remind_password_hyperlink_xpath = "//child::div/a"
    scouts_panel_xpath = "//h5[text()='Scouts Panel']"
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
