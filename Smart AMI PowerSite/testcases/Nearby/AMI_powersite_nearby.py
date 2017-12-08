# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from time import sleep
from testcases import main

class AMI_powersite_nearby(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        usename = 'admin'
        passwd = 'inhemeter'
        desired_caps = {}
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', main.app_init(desired_caps))
        
        sleep(3)
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
        element.send_keys(usename)
        
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)

        sleep(4)
        
    @classmethod
    def tearDownClass(self):
        sleep(2)
        self.driver.quit()

    def test_AMI_powersite_nearby_001(self):
        
        main.element_click(self.driver, 'com.inhe.psite:id/nearby')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/neayby_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/search_all')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/search_meter')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/search_con')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/nearby_tran')
        main.element_click(self.driver, 'com.inhe.psite:id/neayby_back')
        
        pass

    
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AMI_powersite_nearby('test_AMI_powersite_nearby_001'))
    unittest.TextTestRunner(verbosity=2).run(suite)