import requests
from bs4 import BeautifulSoup
from time import sleep


url = "https://www.kinopoisk.ru/lists/movies/top250/"
r = requests.get(url)
sleep(10)
soup = BeautifulSoup(r.text, "lxml")

print(soup.find('div', class_="styles_main__Y8zDm styles_mainWithNotCollapsedBeforeSlot__x4cWo").find('a', class_="base-movie-main-info_link__YwtP1").get('href'))
print(soup.find('div', class_="styles_main__Y8zDm styles_mainWithNotCollapsedBeforeSlot__x4cWo").find('span', class_="styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj").text)
print(soup.find('div', class_="styles_main__Y8zDm styles_mainWithNotCollapsedBeforeSlot__x4cWo").find('span', class_="desktop-list-main-info_secondaryText__M_aus").text)
