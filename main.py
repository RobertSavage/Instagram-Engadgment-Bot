from selenium import webdriver
from time import sleep
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import random
import datetime as dt


class BOT():
	def __init__(self):
		mobile_emulation = { "deviceName": "iPhone 6" }
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("user-data-dir=selenium") 
		#chrome_options.add_argument("--headless") 
		chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
		self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)
		
	def login_initial(self, username, password):

		self.driver.get('https://instagram.com')
		print('LOGING IN...')
		sleep(2)
		login1 = self.driver.find_element_by_css_selector('#react-root > section > main > article > div > div > div > div:nth-child(2) > button')
		login1.click()
		user = self.driver.find_element_by_css_selector('#loginForm > div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div:nth-child(3) > div > label > input')
		user.click()
		sleep(0.5)
		user.send_keys(username)
		pswd = self.driver.find_element_by_css_selector('#loginForm > div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div:nth-child(4) > div > label > input')
		pswd.click()
		sleep(0.5)
		pswd.send_keys(password)
		login2 = self.driver.find_element_by_css_selector('#loginForm > div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div:nth-child(6)')
		login2.click()
		sleep(4)
		print('GETTING PAST POP UPS...')
		try:
			notnow = self.driver.find_element_by_css_selector('#react-root > section > main > div > div > div > button')
			notnow.click()
		except:
			pass
		sleep(5)
		try:
			cancel = self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
			cancel.click()
		except:
			pass
		sleep(2)

	def savedsession(self):
		self.driver.get('https://www.google.com')
		sleep(2.5)
		googlebar = self.driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A7Yvie.emca > div.zGVn2e > div > div.a4bIc > input')
		googlebar.click()
		sleep(2)
		googlesearch = self.driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A7Yvie.emca.emcav.Sl6fgd > div.zGVn2e > div > div.a4bIc > input')
		googlesearch.send_keys('www.instagram.com')
		sleep(2)
		#search = self.driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A7Yvie.emca.emcav.Sl6fgd > div.zGVn2e > button.Tg7LZd > div > span > svg')
		#search.click()
		sleep(2)
		clickinsta = self.driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A7Yvie.emca.Sl6fgd.emcav > div.UUbT9 > ul > li:nth-child(1)')
		clickinsta.click()
		sleep(2)
		try:
			notnow = self.driver.find_element_by_css_selector('#react-root > section > main > div > div > div > button')
			notnow.click()
		except:
			pass
		sleep(5)
		try:
			cancel = self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
			cancel.click()
		except:
			pass
		sleep(2)


	def engadge(self,hashtag,like_wait,comment_wait):
		print('SEARCHING...')
		sleep(10)
		try:
			popup = self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
			popup.click()	
		except:
			pass		
		try:
			explore = self.driver.find_element_by_css_selector('#react-root > section > nav.NXc7H.f11OC > div > div > div.KGiwt > div > div > div:nth-child(2) > a')
			explore.click()
			sleep(2)
		except:
			pass
		searchbar = self.driver.find_element_by_css_selector('#react-root > section > nav.gW4DF > div > header > div > h1 > div > div > div > div > label > input')
		searchbar.click()
		searchbar.send_keys(hashtag)
		sleep(2)
		topresult = self.driver.find_element_by_css_selector('#react-root > section > main > div > div > ul > li:nth-child(1) > a > div')
		topresult.click()
		sleep(2)
		self.driver.execute_script("window.scrollTo(0, 15000)")
		sleep(10) 

		comment_list = ['radical','love this','this is epic!','great post!','this is dope','A good one ✌','🔥🔥🔥','epic','I like your style','💯💯💯','💯','🔥','✌','👑','❤️❤️❤️','❤️']
		final_hrefs = []
		photos =[]
		inital_time = dt.datetime.now()
		counter = 1

		hrefs_in_view = self.driver.find_elements_by_tag_name('a')
		for href in hrefs_in_view:
			if href not in final_hrefs:
				final_hrefs.append(href)

		for pic in final_hrefs:
			temp = pic.get_attribute('href')
			if "/p/" in temp:
				photos.append(temp)

		photos_no_top_post = photos[9:20]
		print(len(photos_no_top_post))
		randcommenttime = comment_wait
		for photo in photos_no_top_post:
			try:
				self.driver.get(photo)
				sleep(4)
				like = self.driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')
				like.click()
				sleep(2)


				delta = dt.datetime.now()-inital_time
				if delta.seconds >= randcommenttime:  #comments every25-30min
					try:
						self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
						sleep(1.3)
						comment = self.driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button')
						comment.click()
						randcomment = comment_list[random.randrange(len(comment_list))]
						sleep(2.8)
						commentbar = self.driver.find_element_by_css_selector('#react-root > section > main > section > div > form > textarea')
						commentbar.click()
						sleep(2)
						print(randcomment)
						commentbar.send_keys(randcomment)
						sleep(4.5)
						postcomment = self.driver.find_element_by_css_selector('#react-root > section > main > section > div > form > button')
						postcomment.click()
					except:
						with open("errorlog.txt", "a", encoding='utf-8') as chkc:
							chkc.write('ERROR: could not COMMENT on post '+str(photo)+"\n")
						print('ERROR: could not comment!')
					try:
						with open("log.txt", "a", encoding='utf-8') as chkc:
							chkc.write('post comment: '+str(randcomment)+"\n")
							chkc.write('post comment time interval: '+str(randcommenttime)+"\n")
						inital_time = dt.datetime.now()
						randcommenttime = comment_wait
					except:
						with open("log.txt", "a", encoding='utf-8') as chkc:
							chkc.write('post comment: EMOJI'+"\n")
							chkc.write('post comment time interval: '+str(randcommenttime)+"\n")
				else: 
					pass

				print('DONE: ',counter,'/',len(photos_no_top_post))
				counter += 1
				sleeptime = like_wait #3-5min wait time
				sleep(sleeptime)
				with open("log.txt", "a", encoding='utf-8') as chkc:
					chkc.write('post like time interval: '+str(sleeptime)+"\n")
			except:
				with open("errorlog.txt", "a", encoding='utf-8') as chkc:
					chkc.write('ERROR: could not load post '+str(photo)+"\n")
				print('ERROR: Could not load')
				print('DONE: ',counter,'/',len(photos_no_top_post))
				counter += 1
		self.driver.get('https://www.google.com')
	def close(self):
		self.driver.quit()



op_counter = 0
BOTGO = True


with open("log.txt", "a") as chkc:
	chkc.write('-----START TIME: '+str(dt.datetime.now())+'-----'+"\n")
with open("errorlog.txt", "a") as chkc:
	chkc.write('-----START TIME: '+str(dt.datetime.now())+'-----'+"\n")

driver = BOT()
#driver.savedsession()
now = dt.datetime.now()







tags = ['#gaming','#life']
like_wait = random.randrange(480,900)
comment_wait = random.randrange(800,1100)
Cycle_wait = random.randrange(1500,3800)

while BOTGO == True:
	for hashtag in tags:
		if now.hour >= 1 and now.hour < 7:
			print('sleeping... ',dt.datetime.now())
			sleep(1800)
		else:
			driver.savedsession()
			driver.engadge(hashtag,like_wait,comment_wait)

	op_counter += 1
	with open("log.txt", "a", encoding='utf-8') as chkc:
		chkc.write('Cycle wait(cycle#/randtime): '+str(op_counter)+str(Cycle_wait)+"\n")
	print('CYCLE COMLETE COUNT: ', op_counter)
	sleep(Cycle_wait) #60 min wait
	Cycle_wait = random.randrange(3600,5300)


		#except:
		#	with open("errorlog.txt", "a", encoding='utf-8') as chkc:
		#		chkc.write('-----ENTIRE BOT FAILED-----'+str(dt.datetime.now())+"\n")
		#	driver.close()
		#	BOTGO = False
'''
CURRENT SETTINGS

	~36 pics per round

	liking pictures: 3-5min wait
	comment: every 25-30min wait
	every: 60min wait

	likes /day: 254
	comments/day: 30
'''

#add nightime sleep
