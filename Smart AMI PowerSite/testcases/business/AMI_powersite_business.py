# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from time import sleep
from testcases import main

device_num1 = '000000000000'
device_num2 = '111111111111'
device_num3 = '222222222222'

def device_num(driver,num):
    driver.find_element_by_id('com.inhe.psite:id/device_reg').click()
    element = driver.find_element_by_id('com.inhe.psite:id/old_meter_text')
    element.clear()
    element.send_keys(num)
    driver.find_element_by_id('com.inhe.psite:id/enter_confirm').click()
    pass

def test_device_register(driver,device_num,):
    main.element_click(driver, 'com.inhe.psite:id/business')
    
    pass
    
def reference_num(driver,num,value):
    driver.find_element_by_id('com.inhe.psite:id/reference').click()
    driver.find_element_by_id('com.inhe.psite:id/content').send_keys(num)
    if value == 'OK':
        driver.find_element_by_id('com.inhe.psite:id/positive').click()
    elif value == 'Cancle':
        driver.find_element_by_id('com.inhe.psite:id/cancel').click()
    pass

def branch_name(driver,branch):
    driver.find_element_by_id('com.inhe.psite:id/branch').click()
    driver.find_element_by_name(branch).click()
    pass

def device_type(driver,Type):
    driver.find_element_by_id('com.inhe.psite:id/device_type').click()
    driver.find_element_by_name(Type).click()
    pass
    
def user_name(driver,name,value):
    driver.find_element_by_id('com.inhe.psite:id/user_name').click()
    element = driver.find_element_by_id('com.inhe.psite:id/text_tip')
    if not element.is_displayed():
        print 'the tips for the name is error'
        return
    element = driver.find_element_by_id('com.inhe.psite:id/content')
    element.clear()
    element.send_keys(name)
    if value == 'OK':
        driver.find_element_by_id('com.inhe.psite:id/positive').click()
    elif value == 'Cancle':
        driver.find_element_by_id('com.inhe.psite:id/cancel').click()
    pass
        
def register_date(driver,year,mounth,day):
    driver.find_element_by_id('com.inhe.psite:id/reg_date').click()
    driver.find_element_by_id('com.inhe.psite:id/yearLoop').send_keys(year)
    driver.find_element_by_id('com.inhe.psite:id/monthLoop').send_keys(mounth)
    driver.find_element_by_id('com.inhe.psite:id/dayLoop').send_keys(day)    
    driver.find_element_by_id('com.inhe.psite:id/positive').click()
    pass
    
def devices_adress(driver,address,value):
    driver.find_element_by_id('com.inhe.psite:id/device_address').click
    element = driver.find_element_by_id('com.inhe.psite:id/content')
    element.clear()
    element.send_keys(address)
    
    if value == 'OK':
        driver.find_element_by_id('com.inhe.psite:id/positive').click()
    elif value == 'Cancle':
        driver.find_element_by_id('com.inhe.psite:id/cancel').click()
    pass
        
def content_num(driver,num,value):
    driver.find_element_by_id('com.inhe.psite:id/con_no').click
    driver.find_element_by_id('com.inhe.psite:id/content').send_keys(num)
    if value == 'OK':
        driver.find_element_by_id('com.inhe.psite:id/positive').click()
    elif value == 'Cancle':
        driver.find_element_by_id('com.inhe.psite:id/cancel').click()
    pass
    
def transformer(driver,value):
    if value == 'OK':
        driver.find_element_by_id('com.inhe.psite:id/transformer').click()
    else:
        return
    pass

class AMI_powersite_business(unittest.TestCase):

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
        element.send_keys(usename)
        element = self.driver.find_element_by_id('com.inhe.psite:id/password')
        element.clear()
        element.send_keys(passwd)
        self.driver.find_element_by_id('com.inhe.psite:id/login_btn').click()
        sleep(4)
        
        self.driver.find_element_by_id('com.inhe.psite:id/business').click()
        pass

    @classmethod
    def tearDownClass(self):
        sleep(2)
        self.driver.quit()
        pass

    def test_AMI_powersite_business_001(self):
        main.element_check_byid(self.driver,'com.inhe.psite:id/device_reg') 
        main.element_check_byid(self.driver,'com.inhe.psite:id/device_replace')
        main.element_check_byid(self.driver,'com.inhe.psite:id/device_demolition')
        main.element_check_byid(self.driver,'com.inhe.psite:id/archives_device')
        main.element_check_byid(self.driver,'com.inhe.psite:id/exception_event')
        main.element_check_byid(self.driver,'com.inhe.psite:id/business_back')   
        main.element_click(self.driver, 'com.inhe.psite:id/business_back') 
        pass   
    
    def test_AMI_powersite_business_002(self):  
        main.element_click(self.driver, 'com.inhe.psite:id/device_reg')
        main.element_content_noclear(self.driver, '', device_num1, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/register_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/upload')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_num')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/reference')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/branch')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_type')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/user_name')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/reg_date')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_address')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/con_no')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/transformer')
        pass
     
    def test_AMI_powersite_business_003(self):
        device_num(self.driver, '000000000000')
        reference_num(self.driver,'test','OK')
        branch_name(self.driver, 'branch01')
        device_type(self.driver, 'Concentrator')
        user_name(self.driver, 'test', 'OK')
        register_date(self.driver, '2017', '11', '24')
        devices_adress(self.driver, 'test', 'OK')
        content_num(self.driver, 'test', 'OK')   
        transformer(self.driver, 'OK')
         
        main.element_click(self.driver, 'com.inhe.psite:id/upload')                
        pass
     
    def test_AMI_powersite_business_004(self):
        main.element_click(self.driver, 'com.inhe.psite:id/device_replace')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', device_num2, '')
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/replace_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/after_change')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_num')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/before_branch')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/RefCode')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_type')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/user_name')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/reg_date')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_address')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/code_enter')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/con_no')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/transformer')
        main.element_check_byname(self.driver, '变更前')
        main.element_check_byname(self.driver, '变更后')
        self.driver.find_element_by_name('变更后')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/replace_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/after_change')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_num')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/before_branch')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/RefCode')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_type')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/user_name')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/reg_date')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_address')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/code_enter')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/con_no')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/transformer')
        main.element_click(self.driver, 'com.inhe.psite:id/replace_back')
        pass
     
    def test_AMI_powersite_business_005(self):
        main.element_click(self.driver, 'com.inhe.psite:id/device_replace')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', device_num2, '')
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        main.element_click(self.driver, 'com.inhe.psite:id/device_num')
        main.element_content_clear(self.driver, 'com.inhe.psite:id/content', device_num3, 'OK')
        main.element_click(self.driver, 'com.inhe.psite:id/after_change')
        pass
     
    def test_AMI_powersite_business_006(self):
        main.element_click(self.driver, 'com.inhe.psite:id/device_demolition')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', device_num2, '')
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/demilition_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/upload')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_num')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/branch')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/RefCode')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_type')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/user_name')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/reg_date')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/device_address')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/code_enter')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/con_no')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/transformer')
        main.element_check_byname(self.driver, device_num2)
        main.element_click(self.driver, 'com.inhe.psite:id/upload')        
        pass
     
    def test_AMI_powersite_business_007(self):
        main.element_click(self.driver, 'com.inhe.psite:id/device_replace')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', device_num2, '')
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        main.element_click(self.driver, 'com.inhe.psite:id/device_num')
        main.element_content_clear(self.driver, 'com.inhe.psite:id/content', device_num3, 'OK')
        main.element_click(self.driver, 'com.inhe.psite:id/after_change')
        pass
     
    def test_AMI_powersite_business_008(self):
        main.element_click(self.driver, 'com.inhe.psite:id/archives_device')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/operational_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/upload')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/op_search')
        main.element_click(self.driver, 'com.inhe.psite:id/operational_back')        
        pass
     
    def test_AMI_powersite_business_010(self):
        main.element_click(self.driver, 'com.inhe.psite:id/exception_event')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/msg_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/msg_sys_notice')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/msg_ex_notice')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/msg_acquisition')
                 
        main.element_click(self.driver, 'com.inhe.psite:id/msg_ex_notice')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/exception_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/exception_upload')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/exception_search')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/list_mode_layout')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/statistics_mode_layout') 
        main.element_click(self.driver, 'com.inhe.psite:id/exception_back')
         
        main.element_click(self.driver, 'com.inhe.psite:id/msg_acquisition')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/acquistion_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/acquistion_search')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/undisposed_layout')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/disposed_layout')
        main.element_click(self.driver, 'com.inhe.psite:id/acquistion_back')
         
        main.element_click(self.driver, 'com.inhe.psite:id/msg_back')
        pass
     
    def test_AMI_powersite_business_011(self):
        main.element_click(self.driver, 'com.inhe.psite:id/exception_event')
        main.element_click(self.driver, 'com.inhe.psite:id/msg_sys_notice')
        main.element_check_byname(self.driver, '系统公告')
        main.element_click(self.driver, 'com.inhe.psite:id/msg_back')    
             
        main.element_click(self.driver, 'com.inhe.psite:id/msg_ex_notice')
        main.element_click(self.driver, 'com.inhe.psite:id/list_mode_layout')
        main.element_click(self.driver, 'com.inhe.psite:id/list_mode_layout')
         
        main.element_click(self.driver, 'com.inhe.psite:id/statistics_mode_layout')
        main.element_click(self.driver, 'com.inhe.psite:id/statistics_mode_layout')
        main.element_click(self.driver,'com.inhe.psite:id/exception_back')
         
        main.element_click(self.driver, 'com.inhe.psite:id/msg_acquisition')
        main.element_click(self.driver, 'com.inhe.psite:id/undisposed_layout')
        main.element_click(self.driver, 'com.inhe.psite:id/disposed_layout')
         
        main.element_click(self.driver, 'com.inhe.psite:id/acquistion_back')
        main.element_click(self.driver, 'com.inhe.psite:id/msg_back')
         
        pass
     
    def test_AMI_powersite_business_012(self):
        main.element_click(self.driver, 'com.inhe.psite:id/acquisition_event')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/acquistion_back')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/acquistion_search')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/undisposed_layout')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/disposed_layout')
         
        main.element_click(self.driver, 'com.inhe.psite:id/acquistion_back')
         
        pass
    
    def test_AMI_powersite_business_013(self):
        num = '0000000000'
        main.element_click(self.driver, 'com.inhe.psite:id/device_reg')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', num, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        
        element = main.element_check_byid(self.driver, 'com.inhe.psite:id/old_meter_text')
        if element == 0:
            self.driver.back()
        elif element == -1:
            main.error_print(1,self.test_AMI_powersite_business_013())
            self.driver.back()
        pass
    
    def test_AMI_powersite_business_014(self):
        num = '0000000000000'
        main.element_click(self.driver, 'com.inhe.psite:id/device_reg')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', num, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        main.element_click(self.driver, 'com.inhe.psite:id/register_back')
        pass
    
    def test_AMI_powersite_business_015(self):
        num = '            '
        main.element_click(self.driver, 'com.inhe.psite:id/device_reg')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', num, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        element = main.element_check_byid(self.driver, 'com.inhe.psite:id/old_meter_text')
        if element == 0:
            self.driver.back()
        elif element == -1:
            main.error_print(1,self.test_AMI_powersite_business_015())
            self.driver.back()
        pass
    
    def test_AMI_powersite_business_016(self):
        num = '\n\n\n\n\n\n'
        main.element_click(self.driver, 'com.inhe.psite:id/device_reg')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', num, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        element = main.element_check_byid(self.driver, 'com.inhe.psite:id/old_meter_text')
        if element == 0:
            self.driver.back()
        elif element == -1:
            main.error_print(1,self.test_AMI_powersite_business_016())
            self.driver.back()
        pass
    
    def test_AMI_powersite_business_017(self):
        num = '测试、测试、测试、'
        main.element_click(self.driver, 'com.inhe.psite:id/device_reg')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', num, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        element = main.element_check_byid(self.driver, 'com.inhe.psite:id/old_meter_text')
        if element == 0:
            self.driver.back()
        elif element == -1:
            main.error_print(1,self.test_AMI_powersite_business_017())
            self.driver.back()
        pass
    
    def test_AMI_powersite_business_018(self):
        num = '!@#$%^&*()_+'
        main.element_click(self.driver, 'com.inhe.psite:id/device_reg')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', num, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        element = main.element_check_byid(self.driver, 'com.inhe.psite:id/old_meter_text')
        if element == 0:
            self.driver.back()
        elif element == -1:
            main.error_print(1,self.test_AMI_powersite_business_018())
            self.driver.back()
        pass
    
    def test_AMI_powersite_business_019(self):
        num = '370000000000'
        main.element_click(self.driver, 'com.inhe.psite:id/device_reg')
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', num, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        element = main.element_check_byid(self.driver, 'com.inhe.psite:id/old_meter_text')
        if element == 0:
            self.driver.back()
        elif element == -1:
            main.error_print(1,self.test_AMI_powersite_business_019())
            self.driver.back()
        pass
    
    def test_AMI_powersite_business_020(self):
        
        main.element_click(self.driver, 'com.inhe.psite:id/device_reg')
        main.element_content_noclear(self.driver, '', device_num1, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        main.element_click(self.driver, 'com.inhe.psite:id/device_num')
        main.element_content_clear(self.driver, 'com.inhe.psite:id/content', device_num2, 'OK')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/register_back')
        pass
    
    def test_AMI_powersite_business_021(self):
        main.element_click(self.driver, main.id_device_reg)
        main.element_content_noclear(self.driver, 'com.inhe.psite:id/old_meter_text', device_num1, None)
        main.element_click(self.driver, 'com.inhe.psite:id/enter_confirm')
        main.element_click(self.driver, 'com.inhe.psite:id/device_num')
        main.element_content_clear(self.driver, 'com.inhe.psite:id/content', device_num2, 'OK')
        main.element_check_byid(self.driver, 'com.inhe.psite:id/register_back')
        pass
    
    
    pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AMI_powersite_business('test_AMI_powersite_business_014'))

    unittest.TextTestRunner(verbosity=2).run(suite)