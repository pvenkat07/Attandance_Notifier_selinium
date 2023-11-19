from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re
import os.path
from os import path
import sqlite3
import schedule
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import discord_webhook

driver = None
URL = "url"

#put your portal login credentials here
CREDS = {'email' : 'your@mail','passwd':'yourpassword'}



def login():
	global driver
	global percent 
	#login required
	print("logging in")
	emailField = driver.find_element_by_xpath('//*[@id="txtuserid"]')
	emailField.click()
	emailField.send_keys(CREDS['email'])
	time.sleep(1)
	passwordField = driver.find_element_by_xpath('//*[@id="txtpassword"]')
	passwordField.click()
	passwordField.send_keys(CREDS['passwd'])
	driver.find_element_by_xpath('//*[@id="Button2"]').click()
	print("logged in")
	time.sleep(3)
	driver.find_element_by_partial_link_text("Attendance").click()
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="MainContent_Button5"]').click()
	time.sleep(3)
	# driver.find_element_by_xpath('//*[@id="MainContent_lbltotal"]')
	percent = driver.find_element_by_id('MainContent_lbltotal').text
	




def send_message():
    	
	print("Sending Message")

	discord_webhook.send_msg(percent)





def start_browser():

	global driver
	driver = webdriver.Firefox() 

	driver.get(URL)

	WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

	if("url" in driver.current_url):
		login()


def begin():
	start_browser()
	send_message()
	driver.quit()
	time.sleep(15)
	begin()




if __name__=="__main__":	
	print("Starting Attandance update bot")
	begin()
		
		
		
