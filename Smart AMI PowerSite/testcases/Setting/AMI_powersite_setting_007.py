# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from time import sleep

class AMI_powersite_setting_007(unittest.TestCase):

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
        self.driver.find_element_by_id('com.inhe.psite:id/check_agreeMent').click()
        element = self.driver.find_element_by_id('com.inhe.psite:id/start_update')
        if element.is_displayed():
            if element.is_selected():
                print 'the update is error'
            
        self.driver.find_element_by_id('com.inhe.psite:id/agreement_back').click()
        element = self.driver.find_element_by_id('com.inhe.psite:id/user_name')
        if not element.is_displayed():
            print 'the back for the update is error'
        
        