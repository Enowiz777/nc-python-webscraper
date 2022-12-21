from requests import get
from requests import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

response = get("https://www.indeed.com/jobs?q=python&limit=50")

print(response.status_code)
print(response.text)
