#!/usr/bin/env python3
'''
Scraper para o ficheiro de texto dos códigos postais dos CTT
Copyleft (c) 2018 Ricardo Lafuente

Usa um browser automatizado para fazer login e aceder ao ficheiro que queremos.
'''
import os
import splinter
from time import sleep
from configparser import SafeConfigParser


def init_browser(webdriver="chrome", headless=True):
    if webdriver == "chrome":
        return splinter.Browser(webdriver,
                                headless=headless,
                                service_log_path=os.path.devnull,
                                user_agent="Mozilla/5.0 ;Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; like Gecko")
    else:
        return splinter.Browser(webdriver,
                                # headless=headless,
                                user_agent="Mozilla/5.0 ;Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; like Gecko")


def run():
    config = SafeConfigParser()
    config.read('credenciais.ini')
    username = config.get('main', 'username')
    password = config.get('main', 'password')

    browser = init_browser()
    # em modo headless, temos de fazer isto para ele conseguir fazer o download
    # https://bugs.chromium.org/p/chromium/issues/detail?id=696481#c80
    browser.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': '.'}}
    browser.driver.execute("send_command", params)
    # Fazer o login
    browser.visit('https://www.ctt.pt/fecas/login')
    browser.find_by_id('username').first.fill(username)
    browser.find_by_id('password').first.fill(password)
    browser.find_by_name('submit').first.click()
    # Ir ao URL do ficheiro
    browser.visit('https://www.ctt.pt/feapl_2/app/restricted/postalCodeSearch/postalCodeDownloadFiles!downloadPostalCodeFile.jspx')
    timer = 0
    while not os.path.exists('todos_cp.zip') and timer < 30:
        sleep(1)
        timer += 1
    browser.quit()


if __name__ == '__main__':
    run()
