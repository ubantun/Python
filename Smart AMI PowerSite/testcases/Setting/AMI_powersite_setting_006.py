# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from time import sleep

class AMI_powersite_setting_006(unittest.TestCase):

    def setUp(self):
        usename = 'admin'
        passwd = 'inhemeter'
        
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.inhe.psite'
        desired_caps['appActivity'] = 'com.inhe.psite.activity.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(usename)
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
        
        self.driver.find_element_by_id('com.inhe.psite:id/mine').click()
        
        sleep(4)

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def testName1(self):
        id1 = 'com.inhe.psite:id/current_distance'
        id_tenmeter = 'com.inhe.psite:id/ten_meter'
        id_hectometre = 'com.inhe.psite:id/hectometre'
        id_five_hundred_meters = 'com.inhe.psite:id/Five_hundred_meters'
        id_a_kilometre = 'com.inhe.psite:id/a_kilometre'
        id_three_kilometers = 'com.inhe.psite:id/three_kilometers'
        id_back = 'com.inhe.psite:id/distance_back'
        
        self.driver.find_element_by_id(id1).click()
        
        self.driver.find_element_by_id(id_tenmeter).click()
        self.driver.find_element_by_id(id_hectometre).click()
        
        self.driver.find_element_by_id(id1).click()
        self.driver.find_element_by_id(id_five_hundred_meters).click()
        
        self.driver.find_element_by_id(id1).click()
        self.driver.find_element_by_id(id_five_hundred_meters).click()
        
        self.driver.find_element_by_id(id1).click()
        self.driver.find_element_by_id(id_a_kilometre).click()
        
        self.driver.find_element_by_id(id1).click()
        self.driver.find_element_by_id(id_three_kilometers).click()
        
        self.driver.find_element_by_id(id1).click()
        self.driver.find_element_by_id(id_back).click()
            
        self.driver.find_element_by_id(id1).click()
        self.driver.find_element_by_id(id_five_hundred_meters)
        self.driver.find_element_by_id(id_five_hundred_meters).click()   
        