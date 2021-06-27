from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

import time
import sys
import requests

from config import API_KEY

def main():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    if sys.argv[1]:
        url = sys.argv[1]
        driver.get(url)
        html = driver.page_source
        domain = driver.current_url
        api_url=f'https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={API_KEY}&domainName={domain}'
        xml_data = requests.get(api_url)
        time.sleep(1)
        bs_data = BeautifulSoup(xml_data.content, "xml")
        contact_email = bs_data.find('contactEmail')
        print(contact_email.string)
        # tree = ET.parse(xml_data.content)
  
        # # getting the parent tag of
        # # the xml document
        # root = tree.getroot()
    
        # # printing the root (parent) tag
        # # of the xml document, along with
        # # its memory location
        # print(root.find('contactEmail'))

if __name__ == '__main__':
    main()
