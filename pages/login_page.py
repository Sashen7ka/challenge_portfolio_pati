from pages.base_page import BasePage


class LoginPage(BasePage):
      login_url = ('https://scouts-test.futbolkolektyw.pl/en')
      login_field_xpath = "//*[@id='login']"
      password_field_xpath = "//input[@name='password']"
      sign_in_button_xpath = "//form/div/div[2]/button/span[1]"
      expected_title = "Scouts panel - sign in"
      title_of_box_xpath = "//*[@id='__next']/div[1]/header/div/h6"
      header_of_box = "Scouts Panel"
      incorrect_login_message_xpath = "//div[1]/div[3]/span"
      expected_invalid_login_message = "Identifier or password invalid."
      remind_password_hyperlink_xpath = "//div[1]/a"
      remind_password_header_xpath = "//div[1]/h5"
      expected_remind_page_header = "Remind password"
      language_dropdown_xpath = "//div[2]/div/div"
      polish_language_xpath = "//div[3]/ul/li[1]"
      english_language_xpath = "//div[3]/ul/li[2]"
      user_login = "user01@getnada.com"

      def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

      def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

      def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

      def do_login(self, email, password):
        self.type_in_email(email)
        self.type_in_password(password)
        self.click_on_the_sign_in_button()

      def title_of_page(self):
          assert self.get_page_title(self.login_url) == self.expected_title

      def check_title_of_header(self):
         self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

      def incorrect_login_check_message(self, incorrect_login_message_xpath="//div[1]/div[3]/span"):
         self.assert_element_text(self.driver, incorrect_login_message_xpath, self.expected_invalid_login_message)

      def click_on_remind_password(self):
          self.click_on_the_element(self.remind_password_hyperlink_xpath)

      def check_remind_page_title(self):
          self.assert_element_text(self.driver, self.remind_password_header_xpath, self.expected_remind_page_header)

