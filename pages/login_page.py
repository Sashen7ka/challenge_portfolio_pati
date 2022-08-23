from pages.base_page import BasePage


class LoginPage(BasePage):
      login_field_xpath = "//*[@id='login']"
      password_field_xpath = "//input[@name='password']"
      sign_in_button_xpath = "//span[@class='MuiButton-label']"
      login_url = ('https://scouts-test.futbolkolektyw.pl/login')
      language_button_xpath = "//div[contains(@class, 'MuiInputBase-input MuiInput-input')]"
      remind_password_hyperlink_xpath = "//child::div/a"
      scouts_panel_xpath = "//h5[text()='Scouts Panel']"
      expected_title = "Scouts panel"
      title_of_box_xpath = "//child::div/h5"
      header_of_box = "Scouts panel"

      def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath,email)

      def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

      def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

      def title_of_page(self):
          assert self.get_page_title(self.login_url) == self.expected_title

      def check_title_of_header(self):
       self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)