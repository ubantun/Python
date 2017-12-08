# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from time import sleep
from testcases import main
    
class AMI_powersite_homepage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
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
        desired_caps['sessionOverride'] = 'True'; 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
        sleep(5)

        element = self.driver.find_element_by_id('com.inhe.psite:id/username')
        element.clear()
#         element.send_keys(usename)
        element.set_text(usename)
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
        
    @classmethod
    def tearDownClass(self):
        sleep(2)
        self.driver.quit()

    def test_AMI_powersite_homepage_001(self):
        main.element_check_byid(self.driver,'com.inhe.psite:id/search_tv') 
        main.element_check_byid(self.driver, 'com.inhe.psite:id/search_type_btn')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/exception_msg')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/map_controll_layout')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/zoomAdd')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/zoomDec')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/location_mine')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/nearby')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/business')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/mine')
 
        pass  
     
    def test_AMI_powersite_homepage_002(self):
        main.element_click(self.driver,'com.inhe.psite:id/zoomAdd') 
        main.element_click(self.driver,'com.inhe.psite:id/zoomAdd') 
        main.element_click(self.driver,'com.inhe.psite:id/zoomAdd') 
        
        main.element_click(self.driver, 'com.inhe.psite:id/zoomDec')
        main.element_click(self.driver, 'com.inhe.psite:id/zoomDec')
        main.element_click(self.driver, 'com.inhe.psite:id/zoomDec')
        
        main.element_click(self.driver,'com.inhe.psite:id/zoomAdd') 
        main.element_click(self.driver,'com.inhe.psite:id/zoomAdd') 
        main.element_click(self.driver,'com.inhe.psite:id/zoomAdd')
        
        main.element_click(self.driver, 'com.inhe.psite:id/zoomDec')
        main.element_click(self.driver, 'com.inhe.psite:id/zoomDec')
        main.element_click(self.driver, 'com.inhe.psite:id/zoomDec')

        pass 
    
    def test_AMI_powersite_homepage_003(self):
        main.element_click(self.driver,'com.inhe.psite:id/zoomAdd') 
        main.element_click(self.driver, 'com.inhe.psite:id/location_mine')
        main.element_click(self.driver, 'com.inhe.psite:id/zoomDec')
        main.element_click(self.driver, 'com.inhe.psite:id/location_mine')
        main.element_click(self.driver, 'com.inhe.psite:id/location_mine')
        main.element_click(self.driver, 'com.inhe.psite:id/location_mine')
        main.element_click(self.driver, 'com.inhe.psite:id/location_mine')
        main.element_click(self.driver, 'com.inhe.psite:id/location_mine')
        main.element_click(self.driver,'com.inhe.psite:id/zoomAdd') 
        main.element_click(self.driver, 'com.inhe.psite:id/zoomDec')
        
        pass 
    
    def test_AMI_powersite_homepage_004(self):
        main.element_click(self.driver, 'com.inhe.psite:id/exception_msg')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/msg_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/msg_sys_notice')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/msg_ex_notice')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/msg_acquisition')
        main.element_click(self.driver, 'com.inhe.psite:id/msg_back')
        
        main.element_click(self.driver, 'com.inhe.psite:id/exception_msg')
        main.element_click(self.driver, 'com.inhe.psite:id/msg_back')
        
        main.element_click(self.driver, 'com.inhe.psite:id/exception_msg')
        main.element_click(self.driver, 'com.inhe.psite:id/msg_back')
        
        main.element_click(self.driver, 'com.inhe.psite:id/exception_msg')
        main.element_click(self.driver, 'com.inhe.psite:id/msg_back')
        
        main.element_click(self.driver, 'com.inhe.psite:id/exception_msg')
        main.element_click(self.driver, 'com.inhe.psite:id/msg_back')
        
        pass 
    
    def test_AMI_powersite_homepage_005(self):
             
        pass 
    
    def test_AMI_powersite_homepage_006(self):
        main.element_click(self.driver, 'com.inhe.psite:id/search_tv')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/search_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/search_view')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/search_btn')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/type_meter')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/type_con')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/type_tran')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/tv_tip')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/tv_clear')
        main.element_click(self.driver, 'com.inhe.psite:id/search_back')
        
        pass 
    
    def test_AMI_powersite_homepage_007(self):
        main.element_click(self.driver, 'com.inhe.psite:id/search_tv')
        main.element_click(self.driver, 'com.inhe.psite:id/type_meter')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/nearby_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/nearby_title')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/scope_btn')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/zoomAdd')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/zoomDec')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/location_mine')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/meter_item')
        
        main.element_click(self.driver, 'com.inhe.psite:id/meter_item')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/search_tv')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/search_type_btn')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/Watch_meterbtn')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/check_bind')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/zoomAdd')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/zoomDec')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/location_mine')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/sing_concentrator_title')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/modify')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/record')
        
        self.driver.back()
        self.driver.back()
        
        pass 
    
    def test_AMI_powersite_homepage_008(self):
        main.element_click(self.driver, 'com.inhe.psite:id/search_tv')
        main.element_click(self.driver, 'com.inhe.psite:id/type_con')
        self.driver.back()
        self.driver.back()
        
        pass 
    
    def test_AMI_powersite_homepage_009(self):
        main.element_click(self.driver, 'com.inhe.psite:id/search_tv')
        main.element_click(self.driver, 'com.inhe.psite:id/type_tran')
        self.driver.back()
        self.driver.back()
        
        pass 
    
    def test_AMI_powersite_homepage_010(self):
        main.element_click(self.driver, 'com.inhe.psite:id/search_tv')
        main.element_click(self.driver, 'com.inhe.psite:id/tv_clear')
        self.driver.back()
        self.driver.back()
        
        pass 


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_001'))
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_002'))
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_003'))
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_004'))
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_005'))
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_006'))
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_007'))
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_008'))
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_009'))
    suite.addTest(AMI_powersite_homepage('test_AMI_powersite_homepage_010'))

    unittest.TextTestRunner(verbosity=2).run(suite)