from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# PATH=r'C:\Users\kazee\Desktop\Python\Crawler\chromedriver.exe'

class Principal(webdriver.Chrome):
    def __int__(self):
        options = webdriver.ChromeOptions().add_experimental_option \
            ('excludeSwitches', ['enable-logging'])
        service = Service(ChromeDriverManager().install())
        super(Principal, self).__init__(service=service, options=options)

    def login(self):
        self.maximize_window()
        self.get('https://www.demo.guru99.com/test/newtours/')

        usuario=self.find_element(By.NAME,'userName').send_keys('mercury')
        senha=self.find_element(By.NAME,'password').send_keys('mercury')
        submit = self.find_element(By.NAME,'submit').click()

        time.sleep(3)


if __name__ == '__main__':
    bot = Principal()
    bot.login()
