import requests
from bs4 import BeautifulSoup
import json

links = list()
vacancy_name = list()
requirements = list()
description = list()
company = list()
date = list()
to_json_l = list()
to_json_d = dict()

# range(a,n) - range of pages to parse from
for n in range(1, 56):
    pagen = requests.get(f"https://career.habr.com/vacancies?page={n}&type=all")
    soupn = BeautifulSoup(pagen.content, "html.parser")
    for i in soupn.find_all("a", {"class": "vacancy-card__icon-link"}):
        links.append(i["href"])

for link in links:
    page1 = requests.get("https://career.habr.com" + link)
    soup1 = BeautifulSoup(page1.content, "html.parser")
    if type(soup1.find("h1", {"class": "page-title__title"})) != type(None):

        """vacancy_name.append((soup1.find("h1", {"class": "page-title__title"})).text)
        requirements.append(soup1.find('span', {"class": "inline-list"}).text)
        description.append(soup1.find('div', {"class":"style-ugc"}).text)
        description = list(filter(lambda x: x is not None, description))
        company.append(soup1.find('div',{'class':'company_name'}).text)
        date.append(soup1.find('div',{'class':'vacancy-header__date'}).text)"""
        # description.append(soup1.find('div', {"class":"style-ugc"}).text)

        to_json_l.append({'vacancy': (soup1.find("h1", {"class": "page-title__title"})).text,
                          'company': soup1.find('div', {'class': 'company_name'}).text,
                          'requirements': soup1.find('span', {"class": "inline-list"}).text,
                          'description': soup1.find('div', {"class": "style-ugc"}).text,
                          'link': "https://career.habr.com" + link,
                          'date': soup1.find('div', {'class': 'vacancy-header__date'}).text})
    else:
        pass

to_json_d.update({"data": to_json_l})
json_object = json.dumps(to_json_d, indent=5, ensure_ascii=False)
# 'data{n}.json' - file where vacancy cards are parsed, n - arbitrary number
with open("data6.json", "w", encoding='utf8') as outfile:
    outfile.write(json_object)
