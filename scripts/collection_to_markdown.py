import requests
from bs4 import BeautifulSoup

# Collection link
response = requests.get("https://steamcommunity.com/sharedfiles/filedetails/?id=3586409043")
html_doc = response.content

soup = BeautifulSoup(html_doc, 'html.parser')

addons = soup.find_all(class_="collectionItem")

for addon in addons:
	title = addon.find(class_="workshopItemTitle")
	title_str = title.string
	link = title.parent.get("href")
	print(f"- [{title_str}]({link})")
