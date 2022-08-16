# Task 1: Software configuration.
## Subtask 1: Why did I choose to participate in the challenge portfolio?
:smiley:

*Hello, my name is Oleksandra, I decided took part it that project because I want to learn something new - in our case it is basic of Automated Testing.*
- [x] It gives me more understanding of a theme Testing in general
- [x] I will create interesting project to add to my resume 
- [x] I have a hope that it helps me find new job in Ukraine

# Task 2: Selectors. 
## Subtask 1: Add a note in the README file - list 3 working selectors for each element found on the page. 

*English version of the site*

- [x] **remind_password_hyperlink_xpath**

//*[@id="__next"]/form/div/div[1]/a

//*[text()="Remind password"]

//child::div/a


- [x] **login_field_xpath**

//*[@id='login']

//*[text()='Login']

//input[@name='login']


- [x] **password_field_xpath**

//*[@id='password']

//*[text()='Password']

//input[@name='password']


- [x] **language_button_xpath**

//*[@id="__next"]/form/div/div[2]/div/div

//div[contains(@class, 'MuiInputBase-input MuiInput-input')]

//div[text()='English']

//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input']


- [x] **sign_in_button_xpath**

//*[@id="__next"]/form/div/div[2]/button/span[1]

//span[@class='MuiButton-label']

//*[text()='Sign in']


- [x] **scouts_panel_xpath**

//*[@id="__next"]/form/div/div[1]/h5

//h5[text()='Scouts Panel']

//span[@class='MuiButton-label']