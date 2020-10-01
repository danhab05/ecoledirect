from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import re

class Ecoledirect_bot:
    driver = None
    matiere = []
    homework = []
    day = []
    dic = {}
    def __init__(self, username, password, hidden=True):
        self.username = username
        self.password = password
        self.hidden = hidden
        self.list = []
        self.op = None
        self.message = []

    def login(self):
        if self.hidden:
            self.op = webdriver.ChromeOptions()
            self.op.add_argument('headless')
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.op)
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.ecoledirecte.com/login')
        nameInput = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/input[1]')
        passInput = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/input[2]')
        nameInput.send_keys(self.username)
        passInput.send_keys(self.password)
        button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/button')
        button.click()
        time.sleep(2)


    def get_notes(self):
        pass

    def get_homework(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ed-menu[2]/div/a/div").click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/ed-menu[2]/div/div/ul/li[7]/a').click()
        # SEMAINE
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[2]/cahier-de-texte/div/div[1]/div[2]/div[2]/ul/li[10]/a').click()
        time.sleep(2)
        page = self.driver.page_source
        soup = BeautifulSoup(page, 'lxml')
        days = soup.find_all('div', {'class': 'encartJour'})
        currentday = ""
        currenthome = ""
        for div in days:
            currentday = ""
            currenthome = ""
            h = div.find('h3')
            currentday = h.text
            self.day.append(h.text)
            for txt in div.find_all('div', {'class': 'col-md-9'}):
                self.homework.append(txt.text)
                print(txt.text)
                currenthome = txt.text
            for h3 in div.find_all('h3', {'class': ""}):
                if h3.text.isupper():
                    self.matiere.append(h3.text)
            self.dic[currentday] = currenthome

        i = 0


        list = []

    def close(self):
        self.driver.close()
