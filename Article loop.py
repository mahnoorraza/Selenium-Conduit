from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C://Automation Drivers//Selenium Web Drivers//chromedriver_win32//chromedriver.exe")

driver.get("https://react-redux.realworld.io/#/?_k=mxozo6")
driver.maximize_window()

"""driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[2]/a").click()

driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("mahnoor123@domain.com")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("Abc123@@")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(4) """


"""#article title  [ Valid ]
articletitle = ["NewTest"]
#article about
articleabout = ["hello"]
#write your article
writearticle = ["It's my first article"]
#Enter tags
entertags = ["SQA"] """


driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("mahnoor123@domain.com")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("Abc123@@")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
time.sleep(4)

for i in range(1,11):


    # goto article
     driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[2]/a").click()
     #driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[2]/a").click()
    # article title
     driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("hello")
     time.sleep(2)
    # article about
     driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("b")
     time.sleep(2)
    # write article
     driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[3]/textarea").send_keys("no")
     time.sleep(2)
    # enter tags
     driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[4]/input").send_keys("hshs")
     time.sleep(4)
    # publish
     driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/button").click()
     time.sleep(4)

     driver.find_element_by_xpath("//*[@id='main']/div/nav/div/ul/li[2]/a").click()



