
# for the business
id_device_reg = 'com.inhe.psite:id/device_reg'

#for the device register
id_device_num = 'com.inhe.psite:id/device_num'
id_reference_num = 'com.inhe.psite:id/reference'
id_branch_num = 'com.inhe.psite:id/branch'
id_device_type = 'com.inhe.psite:id/device_type'
id_user_name = 'com.inhe.psite:id/user_name'
id_register_date = 'com.inhe.psite:id/reg_date'
id_device_address = 'com.inhe.psite:id/device_address'
id_concent_num = 'com.inhe.psite:id/con_no'
id_transformer = 'com.inhe.psite:id/transformer'
        
def app_init(desired_caps):

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.inhe.psite'
    desired_caps['appActivity'] = 'com.inhe.psite.activity.SplashActivity'
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'
    return desired_caps
    pass
def element_click(driver,ID):
    driver.find_element_by_id(ID).click()
    pass
    
def element_check_byid(driver,ID):
    element = driver.find_element_by_id(ID)
    if not element.is_displayed():
        print 'the id'+ ID +' is nor exsited'
        return -1
    else:
        return 0
    pass

def element_check_byname(driver,name):
    element = driver.find_element_by_name(name)
    if not element.is_displayed():
        print 'the id'+ name +' is nor exsited'
        return -1
    else:
        return 0
    pass

def element_content_clear(driver,ID,text,value):
    element = driver.find_element_by_id(ID)
    element.clear()
    if not text == None:
        element.send_keys(text)    
    if  value == 'OK':
        driver.find_element_by_id('com.inhe.psite:id/positive').click()
    elif value == 'Cancle':
        driver.find_element_by_id('com.inhe.psite:id/cancel').click()
    pass

def element_content_noclear(driver,ID,text,value):
    element = driver.find_element_by_id(ID)
    element.send_keys(text)
    if  value == 'OK':
        driver.find_element_by_id('com.inhe.psite:id/positive').click()
    elif value == 'Cancle':
        driver.find_element_by_id('com.inhe.psite:id/cancel').click()
    pass

def element_quit_app(driver):
    element_click(driver, 'com.inhe.psite:id/mine')
    element_click(driver, 'com.inhe.psite:id/signUp')
    element_click(driver, 'com.inhe.psite:id/login_up_ok')
    pass

def error_print(error,testcase):
    if error == 1:
        print 'the element is not existed for the '+testcase
    pass
