'''simple selenium crawler'''

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Crawler(object):
    '''A selenium crawler'''
    def init_browser(self):
        '''Turn on Firefox'''
        self.browser = webdriver.Firefox()
        self.browser.wait = WebDriverWait(self.browser, 5)
        return self.browser

    def getContent(self, url):
        '''Fetch and render the page to return html'''
        self.browser.get(url)
        time.sleep(4)
        return self.browser.page_source

    def exit(self):
        '''Be tidy and exit Firefox'''
        return self.browser.quit()

