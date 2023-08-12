import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr",limit=50)        # Goes to 'tbody' and prints 50 'tr' elements with the relevant class.
count = 1
print(list)


for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text           #The title part is located within the 'td' element inside the 'tr'.
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")   # The year of the movies are in the span. And strip method deleted parantheses
    print(title,year)
    
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text

    print(f"{count}- film: {title.ljust(50)} year: {year} rating: {rating}")
    count+=1