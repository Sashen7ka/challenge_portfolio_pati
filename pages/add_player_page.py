    from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    add_player_page_url = ('https://scouts-test.futbolkolektyw.pl/en/players')
    player_name_field_xpath = "//div[1]/div/div/input"
    player_surname_field_xpath = "//div[3]/div/div/input"
    main_position_field_xpath = "//div[11]/div/div/input"
    player_age_field_xpath = "//div[7]/div/div/input"
    edit_player_header_xpath = "Add player"
    submit_button_xpath =  "//form/div[3]/button[1]"


    def type_to_name(self,name):
        self.field_send_keys(self.player_name_field_xpath, name)

    def type_to_surname(self, surname):
        self.field_send_keys(self.player_surname_field_xpath, surname)

    def type_to_main_position(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def click_on_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def select_age(self):
        self.field_send_keys(self.player_age_field_xpath, 07.07.2007)

