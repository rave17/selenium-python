import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from utils.config_reader import get_browser


# Define la fixture del webdriver


def get_driver(browser_name: str) -> webdriver:
    # Obtiene la configuración del navegador desde el archivo config.py
    config = get_browser()
    chrome_path = config["webdrivers"]["chrome_path"]
    firefox_path = config["webdrivers"]["firefox_path"]

    # Configura las opciones de cada navegador
    chrome_service = Service(chrome_path)
    firefox_service = Service(executable_path=firefox_path)

    chrome_options = ChromeOptions()
    firefox_options = FirefoxOptions()
    if browser_name == "chrome":
        # Configuración de opciones para Chrome
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    elif browser_name == "firefox":
        # Configuración de opciones para Firefox
        firefox_options.add_argument("start-maximized")
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    else:
        raise ValueError(f'Unsupported browser: {browser_name}')

    return driver
