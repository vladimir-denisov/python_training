# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_group(self):
        success = True
        wd = self.wd
        wd.get("https://www.mos.ru/")
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("alias").click()
        wd.find_element_by_id("alias").clear()
        wd.find_element_by_id("alias").send_keys("vladimir.denisov.mos")
        wd.find_element_by_id("aliaspswd").click()
        wd.find_element_by_id("aliaspswd").clear()
        wd.find_element_by_id("aliaspswd").send_keys("Ikfr5Ljcneg6")
        wd.find_element_by_id("outerlogin_button").click()
        wd.find_element_by_xpath("//div[@class='mos-header__top-bar']/ul/li[3]/div[1]/span[3]").click()
        wd.find_element_by_link_text("Выход").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
