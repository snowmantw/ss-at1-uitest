#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import platform
import os
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestBasicFlows(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        def dispatch_driver_path():
            cwd = os.getcwd()
            is_64bits = sys.maxsize > 2**32
            print "is_64bit: %s" % is_64bits
            which_system = platform.system()
            if which_system == 'Darwin':
              return cwd + "/tools/chromedriver-mac"
            elif which_system == 'Linux' and is_64bits:
              os.environ["webdriver.chrome.bin"] = '/usr/lib/chromium-browser/chromium-browser'
              return cwd + "/tools/chromedriver-linux64"
            elif which_system == 'Linux' and not is_64bits:
              os.environ["webdriver.chrome.bin"] = '/usr/lib/chromium-browser/chromium-browser'
              return cwd + "/tools/chromedriver-linux32"
            else:
              raise "Not in a capatible platform: %s " % platform.system()

        chromedriver = dispatch_driver_path()
        os.environ["webdriver.chrome.driver"] = chromedriver
        print os.environ["webdriver.chrome.driver"]
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
