from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C://Automation Drivers//Selenium Web Drivers//chromedriver_win32//chromedriver.exe")

driver.get("https://react-redux.realworld.io/#/?_k=3fytv1")
driver.maximize_window()

#------------------------------------Sign Up--------------------------------------
""" time.sleep(4)
driver.find_element(By.LINK_TEXT,"Sign up").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("hdhdhdhdhdhdhdhhdhhdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("mahnoor@domain.com")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/input").send_keys("oooo")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").clear()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("Mahnoorr")
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/input").clear()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/input").send_keys("noori786")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").clear()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("Mahnoorr2")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[3]/a").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[3]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("Mahnoorr")
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("mahnoor@domainn.com")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/input").send_keys("noori786")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").clear()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("noor")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").clear()
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("mahnoor@domaii.com")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click() """




#--------------------------------Sign In-------------------------------------------

#email  [ Valid , Invalid, Empty, Invalid]
email = ["abc@domain.com", " ", "mahnoor123@domain.com"]
#password  [ Valid , Invalid, Empty, Valid]
password = ["123456789", " ", "Abc123@@"]
for a,b in zip(email,password):
    driver.refresh()
    # goto sign in
    driver.find_element_by_xpath('/html/body/div/div/nav/div/ul/li[2]/a').click()
    time.sleep(1)
    # Email
    driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys(a)
    time.sleep(1)
    # Password
    driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys(b)
    time.sleep(1)
    # Click Signin button
    driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/form/fieldset/button').click()
    time.sleep(4)
    try:
        if(driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/ul').is_displayed()==True):
            print("Sign In was Unsuccessful")
        else:
            pass
    except:
        driver.find_element_by_xpath('//*[@id="main"]/div/nav/div/ul/li[3]/a').click()
        print("Sign in was successful")
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/button').click()
time.sleep(6) 
#driver.close()

#-------------------------------------------Sign up------------------------------

#username [Valid , Invalid, Empty, Invalid]
username = ["Mahnoor12", " ", "Mahnoorzz"]

#email  [ Valid , Invalid, Empty, Invalid]
email = ["abc@domain.com", " ", "mahnoor97@domainn.com"]

#password  [ Valid , Invalid, Empty, Valid]
password = ["123456789", " ", "Abc1233@@"]

for a,b,c in zip(username, email, password):
    driver.refresh()
    # goto sign up
    driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[3]/a").click()
    time.sleep(1)
    # username
    driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys(a)
    time.sleep(1)
    # Email
    driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys(b)
    time.sleep(1)
    # Password
    driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/input").send_keys(c)

    # Click Signup button
    driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
    time.sleep(4)
    try:
        if(driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/ul').is_displayed()==True):
            print("Sign In was Unsuccessful")
        else:
            pass
    except:
        driver.find_element_by_xpath('//*[@id="main"]/div/nav/div/ul/li[3]/a').click()
        print("Sign in was successful")
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/button').click()
time.sleep(6)
driver.close()





















