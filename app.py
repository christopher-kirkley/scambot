from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

import time
import sys
import requests

from config import API_KEY, GOOGLE_API_KEY

def check_url(url):
    data = {
    "client": {
      "clientId": "ScamBot",
      "clientVersion": "1.0"
    },
    "threatInfo": {
      "threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING"],
      "platformTypes":    ["WINDOWS"],
      "threatEntryTypes": ["URL"],
      "threatEntries": [
        {"url": url},
      ]
    }
    }
    r = requests.post(f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={GOOGLE_API_KEY}', data = data)
    print(r.status_code)
    return True

def access_url(url, driver):
    driver.get(url)
    html = driver.page_source
    domain = driver.current_url
    return domain

def get_abuse_email(domain):
    api_url=f'https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={API_KEY}&domainName={domain}'
    xml_data = requests.get(api_url)
    time.sleep(1)
    bs_data = BeautifulSoup(xml_data.content, "xml")
    contact_email = bs_data.find('contactEmail').string
    return contact_email

def main():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    if sys.argv[1]:
        url = sys.argv[1]
        domain = access_url(url, driver)
        contact_email = get_abuse_email(domain)
        print(contact_email)


if __name__ == '__main__':
    main()
