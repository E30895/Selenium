from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from workalendar.america import Brazil
import time
from datetime import date, timedelta
import numpy as np
import pandas as pd

def add_business_days(start_date, num_days, calendar):
    current_date = start_date
    while num_days > 0:
        current_date += timedelta(days=1)
        # Verifica se é um dia útil (não é fim de semana nem feriado)
        if calendar.is_working_day(current_date):
            num_days -= 1
    return current_date

future_date = add_business_days(date.today(), 8, Brazil())
future_date = future_date.strftime("%d/%m/%Y")

browser = webdriver.Edge()

#caminho para o deskbee
browser.get('')

time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="q-app"]/div/div/main/form/div/div/div[2]/div/div/button/span[2]').click()

time.sleep(5)
browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[2]/button[2]/span[2]').click()

time.sleep(5)
browser.get('')

browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/main/form/div[1]/div/label/div/div[1]/div[2]/input').send_keys(future_date)
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/main/form/div[2]/div[1]/label/div[1]/div[1]/div/input').send_keys("09:00")
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/main/form/div[2]/div[2]/label/div[1]/div[1]/div/input').send_keys("18:00")
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/main/form/div[3]/div[1]/label/div/div[1]/div[2]/div[1]/input').send_keys("CAS Assis Brasil › Torre C")

time.sleep(2)
browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div[2]/span').click()

browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/main/form/div[3]/div[2]/label/div/div[1]/div[2]/div[1]/input').send_keys("10º Andar")

time.sleep(2)
browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/span').click()

browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/main/form/div[4]/div/div[1]/button/span[2]').click()

time.sleep(1)
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/main/div[2]/div[2]/div[1]/label/div/div/div[2]/input').send_keys('10.011')

time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/main/div[3]/div/div/div[1]/div/div/div[2]/div[4]/div[2]/button/span[2]/div/span').click()

time.sleep(1)
browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[3]/div[2]/div/button/span[2]/div/span').click()
