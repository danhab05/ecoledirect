# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import re

class EcoleDirect:
    driver = None

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

        i = 0
        while i != 6:
            if i == 5:
                pass
            else:

                self.message.append(re.sub(r"\n+", "", days[i].text.replace('Contenu de la séance', '').replace('Effectué', '').replace('Donné le ', ' ').replace('par', ' ').replace('Mme', '').replace('M.', '').replace('.', '. ').strip()))
            i+=1

        list = []
        return self.message

    def close(self):
        self.driver.close()
