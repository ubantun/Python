# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from time import sleep

class AMI_powersite_setting(unittest.TestCase):
    
    @classmethod
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
    @classmethod
    def tearDown(self):
        
        sleep(2)
        self.driver.quit()
        pass

    def AMI_powersite_setting_001(self):
         
        element = self.driver.find_element_by_id('com.inhe.psite:id/user_name')
        if element.is_displayed() == False:
            print 'the setting is failed'
             
    def AMI_powersite_setting_002(self):
         
        self.driver.find_element_by_id('com.inhe.psite:id/language_set').click()
        self.driver.find_element_by_id('com.inhe.psite:id/chinese').click()
        self.driver.find_element_by_id('com.inhe.psite:id/language_ok').click()
         
        self.driver.find_element_by_id('com.inhe.psite:id/mine').click()
        self.driver.find_element_by_id('com.inhe.psite:id/chinese').click()
        self.driver.find_element_by_id('com.inhe.psite:id/language_ok').click()
         
    def AMI_powersite_setting_003(self):
        self.driver.find_element_by_id('com.inhe.psite:id/language_set').click()
        element = self.driver.find_element_by_id('com.inhe.psite:id/chinese')
        if element.is_selected():
            print 'test_AMI_powersite_setting_003 the language is chinese'
            self.driver.find_element_by_id('com.inhe.psite:id/english').click()
            self.driver.find_element_by_id('com.inhe.psite:id/language_ok').click()
        else:
            print 'test_AMI_powersite_setting_003 the language is english'
          
    def AMI_powersite_setting_004(self):
        self.driver.find_element_by_id('com.inhe.psite:id/language_set').click()
        element = self.driver.find_element_by_id('com.inhe.psite:id/chinese')
        if element.is_selected():
            print 'test_AMI_powersite_setting_004 the language is chinese'
            self.driver.find_element_by_id('com.inhe.psite:id/english').click()
            self.driver.find_element_by_id('com.inhe.psite:id/language_ok').click()
            self.driver.find_element_by_id('com.inhe.psite:id/chinese').click()
            self.driver.find_element_by_id('com.inhe.psite:id/language_ok').click()
        else:
            print 'test_AMI_powersite_setting_004 the language is english'
            self.driver.find_element_by_id('com.inhe.psite:id/chinese').click()
            self.driver.find_element_by_id('com.inhe.psite:id/language_ok').click()
            
    def AMI_powersite_setting_005(self):
        self.driver.find_element_by_id('com.inhe.psite:id/language_set').click()
        element = self.driver.find_element_by_id('com.inhe.psite:id/chinese')
        if element.is_selected():
            print 'test_AMI_powersite_setting_005 the language is chinese'
            self.driver.find_element_by_id('com.inhe.psite:id/english').click()
            self.driver.find_element_by_id('com.inhe.psite:id/language_ok').click()
            self.driver.find_element_by_id('com.inhe.psite:id/language_set').click()
            self.driver.find_element_by_id('com.inhe.psite:id/english').click()
            self.driver.find_element_by_id('com.inhe.psite:id/language_ok').click()
        else:
            print 'test_AMI_powersite_setting_005 the language is english'
            self.driver.find_element_by_id('com.inhe.psite:id/english').click()
            self.driver.find_element_by_id('com.inhe.psite:id/language_ok').click()
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    
    suite = unittest.TestSuite()
    suite.addTest(AMI_powersite_setting('test_AMI_powersite_setting_005'))
    unittest.main()   