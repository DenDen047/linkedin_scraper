import json
from selenium import webdriver
from linkedin_scraper import actions

def test_login():
    with open('setting.json') as f:
        setting = json.load(f)
        username = setting['username']
        password = setting['password']

    driver = webdriver.Chrome()
    actions.login(driver, username, password)
