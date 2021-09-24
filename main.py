from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options

CHROME_PATH = "C:/Chromedriver/chromedriver"
URL = "https://tinder.com/"
EMAIL = "EMAIL"
PASSWORD = "PASSWD"


def login():

    login_button = driver.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
    login_button.click()

    time.sleep(2)

    options = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/button')
    if options.text == "MORE OPTIONS":
        options.click()
        time.sleep(2)

    facebook_login = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
    facebook_login.click()
    time.sleep(2)

    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle
            driver.switch_to.window(login_page)


    mail_box = driver.find_element_by_name("email")
    mail_box.send_keys(EMAIL)

    passwd = driver.find_element_by_name("pass")
    passwd.send_keys(PASSWORD)

    login_btn = driver.find_element_by_name("login")
    login_btn.click()

    time.sleep(5)

    driver.switch_to.window(main_page)

def likeordislike():
    time.sleep(10)
    global n
    if n == 1:
        dislike = driver.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
        dislike.click()
        n += 1
    else:
        dislike = driver.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
        dislike.click()
    
################################################################MAIN-CODE#################################################################

option = Options()
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
driver = webdriver.Chrome(chrome_options=option, executable_path=CHROME_PATH)
driver.maximize_window()
tinter = driver.get(URL)
driver.implicitly_wait(30)


main_page = driver.current_window_handle
login()

n = 1

for z in range(0, 100):

    try:
        likeordislike()
    except ElementClickInterceptedException:
        not_interested_button = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[2]/button[2]').click()


driver.close()
