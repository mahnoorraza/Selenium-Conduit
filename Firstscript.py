from selenium import webdriver
from selenium.webdriver.common.by import By
import time




driver = webdriver.Chrome(executable_path="C://Automation Drivers//Selenium Web Drivers//chromedriver_win32//chromedriver.exe")

#-------------------------SIGNUP----------------------------

driver.get("https://react-redux.realworld.io/#/?_k=3fytv1")
#capture all the cookies created by browser

driver.save_screenshot("C:\Screenshots\homepage1.png")

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
driver.maximize_window()

time.sleep(4)
driver.find_element(By.LINK_TEXT,"Sign up").click()
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("Mahnoortest")
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("mahnoor@domain.com")
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/input").send_keys("Abc123@@")
driver.find_element(By.LINK_TEXT,"Have an account?").click()

time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("mahnoor123@domain.com")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("Abc123@@")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()

#----------------------News Feed--------------------------------------

time.sleep(3)

driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[1]/ul/li[2]/a").click()
time.sleep(3)



#-------------------------New Post--------------------------------------

driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(9)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("First test")
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("About my testing")
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/textarea").send_keys("Hello world")
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[4]/input").send_keys("SQA")

driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(5)


time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/span/a").click()
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/textarea").send_keys("hi world")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div[2]/div[3]/div/div[1]/form/div[1]/textarea").send_keys("nice article")
driver.find_element_by_xpath("//*[@id='main']/div/div/div[2]/div[3]/div/div[1]/form/div[2]/button").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0,500)","")

driver.find_element_by_xpath("//*[@id='main']/div/div/div[2]/div[3]/div/div[2]/div/div[2]/span[2]/i").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/span/a").click()
print(driver.title)
driver.back()

time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/div/a").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='main']/div/div/div[2]/div/div/div[2]/div[1]/a/h1").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/span/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[1]/ul/li[2]/a").click()


time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[3]/a").click()
time.sleep(6)
#driver.find_elements_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("abc")
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("https://e7.pngegg.com/pngimages/516/431/png-clipart-female-profile-avatar-illustration-computer-icons-female-user-profile-female-girl-wife-woman-icon-miscellaneous-logo.png")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/textarea").send_keys("SQA Analyst")
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[1]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/button").click()
time.sleep(3)

driver.find_element_by_xpath("/html/body/div/div/nav/div/ul/li[4]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div[2]/div/div/div[1]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[1]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[1]/ul/li[2]/a").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0,1500)","")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[2]/nav/ul/li[6]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[2]/nav/ul/li[7]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[2]/div[10]/a/ul/li[1]").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/div/a").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/div/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[1]/ul/li[1]/a").click()
time.sleep(5)

driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[1]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[1]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[2]/div/div/a[12]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[2]/div/div/a[13]").click()
time.sleep(4)
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div[1]/div[2]/div[4]/a/h1").click()
time.sleep(7)
driver.find_element_by_xpath("/html/body/a").click()
time.sleep(4)
driver.close()
time.sleep(3)
driver.quit()















