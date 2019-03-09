import requests
page = requests.get('https://www.google.com/')
print(page.text())