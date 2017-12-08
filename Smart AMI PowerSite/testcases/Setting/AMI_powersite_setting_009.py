# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from time import sleep

class AMI_powersite_setting_009(unittest.TestCase):

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
        self.driver.find_element_by_id('com.inhe.psite:id/signUp').click()
        element = self.driver.find_element_by_id('com.inhe.psite:id/login_up_tip')
        if  not element.is_displayed():
            print 'the tips for the exit is error'
        else:
            self.driver.find_element_by_id('com.inhe.psite:id/login_up_no').click()
            element = self.driver.find_element_by_id('com.inhe.psite:id/user_name')
            if not element.is_displayed():
                print 'the back for the exit is error'
        
        self.driver.find_element_by_id('com.inhe.psite:id/signUp').click() 
        element = self.driver.find_element_by_id('com.inhe.psite:id/login_up_tip')
        if  not element.is_displayed():
            print 'the tips for the exit is error'
        else:
            self.driver.find_element_by_id('com.inhe.psite:id/login_up_ok').click()
            element = self.driver.find_element_by_id('com.inhe.psite:id/logo2_iv')
            if not element.is_displayed():
                print 'the exit is error'      
        
        