from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:\\Users\\donh\\Downloads\\chromedriver.exe')

def get_driver():
  # Set options
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches",["enable-automation"])

  driver = webdriver.Chrome(service=service,options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())