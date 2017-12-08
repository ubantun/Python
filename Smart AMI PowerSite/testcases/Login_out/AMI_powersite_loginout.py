# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from time import sleep
from testcases import main

class AMI_powersite_loginout(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
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
        pass
    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        pass
    
    def test_AMI_powersite_loginout_001(self):
        
        usename = 'admin'
        passwd = 'inhemeter'
        main.element_content_clear(self.driver, 'com.inhe.psite:id/username', usename, 'OK')
        main.element_content_clear(self.driver, 'com.inhe.psite:id/password', passwd, 'OK')
        
        sleep(4)
        main.element_check_byid(self.driver, 'com.inhe.psite:id/nearby')            
        main.element_quit_app(self.driver)
        pass
            
    def test_AMI_powersite_loginout_002(self):
        
        passwd = 'inhemeter'
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
        
        pass
    
    def test_AMI_powersite_loginout_003(self):
#         username = '���Ϻ�'
        passwd = 'inhemeter'
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys('早上好')     #failed to input the chinese
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
            
        pass
    
    def test_AMI_powersite_loginout_004(self):
        username = ' '
        passwd = 'inhemeter'
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(username)    
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
                    
        pass
    
    def test_AMI_powersite_loginout_005(self):
        username = '123'
        passwd = 'inhemeter'
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(username)    
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
    
        pass
    
    def test_AMI_powersite_loginout_006(self):
        username = '\n'
        passwd = 'inhemeter'
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(username)    
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
            
        pass
    
    def test_AMI_powersite_loginout_007(self):
        username = 'admin'
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(username)    
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()

        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
                
        pass
    
    def test_AMI_powersite_loginout_008(self):
        username = 'admin'
        passwd = '早上好'
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(username)     
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)       #failed to input the chinese
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
            
        pass
    
    def test_AMI_powersite_loginout_009(self):
        usename = 'admin'
        passwd = ' '
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(usename)
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)

        pass
    
    def test_AMI_powersite_loginout_010(self):
        usename = 'admin'
        passwd = '123'
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(usename)
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)

        pass
    
    def test_AMI_powersite_loginout_011(self):
        usename = 'admin'
        passwd = '\n'
        
        sleep(3)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(usename)
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)

        pass
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AMI_powersite_loginout('test_AMI_powersite_loginout_001'))
    unittest.main()