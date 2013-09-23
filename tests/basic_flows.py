#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestBasicFlows(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print os.getcwd()
        chromedriver = os.getcwd() + "/tools/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        cls.chromedriver = chromedriver

    def setUp(self):
        self.driver = webdriver.Chrome(TestBasicFlows.chromedriver)
        self.siteurl = "http://wa.nccu.edu.tw/QryTor"
        self.driver.get(self.siteurl)

    def tearDown(self):
        self.driver.close()

    def test_coursesPage(self):
        btn = self.driver.find_element_by_css_selector('#searchc')
        btn.click()
        self.driver.implicitly_wait(3)
        check = 0 < len(self.driver.find_elements_by_css_selector('#FilterDiv'))
        assert check, "Can't navigaate to the query result page."

    def test_plugin(self):
        btn = self.driver.find_element_by_css_selector('#searchc')
        btn.click()
        self.driver.implicitly_wait(3)
        check = 0 < len(self.driver.find_elements_by_css_selector('#FilterDiv'))
        assert check, "Can't navigaate to the query result page."
        link = self.driver.find_element_by_css_selector('.btn.social-course')[0]
        link.click()
        self.driver.implicitly_wait(3)
        #TODO: Check if data sent


if __name__ == "__main__":
      unittest.main()
