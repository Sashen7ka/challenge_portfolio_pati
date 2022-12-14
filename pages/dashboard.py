import time
from pages.base_page import BasePage



class Dashboard(BasePage):
  expected_title = "Scouts panel"
  dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
  main_page_xpath = "//span[text()='Main page']"
  players_xpath = "//div[contains(@class,'MuiListItemText-root jss29 jss55')]"
  polski_xpath = "//ul[2]/div[1]/div[2]/span"
  sign_out_xpath = "//div/ul[2]/div[2]/div[2]/span"
  players_count_xpath = "//div[2]/div/div[1]"
  matches_count_xpath = "//main/div[2]/div[2]/div"
  reports_count_xpath = "//main/div[2]/div[3]/div"
  events_count_xpath = "//main/div[2]/div[4]/div"
  scouts_panel_xpath = "//main/div[3]/div[1]/div/div[2]"
  dev_team_panel_xpath = "//a[contains(@href,'://app.slack.com/client/T3X4CAKNU/C3XTEGXB6')]"
  shortcuts_xpath = "//main/div[3]/div[2]/div/div/h2"
  futbol_kolektyw_button_xpath = "//*[@title='Logo Scouts Panel']"
  add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

  def title_of_page(self):
    self.wait_for_element_to_be_clickable(self.futbol_kolektyw_button_xpath)
    assert self.get_page_title(self.dashboard_url) == self.expected_title

  def click_on_the_add_player_button(self):
    self.click_on_the_element(self.add_player_button_xpath)