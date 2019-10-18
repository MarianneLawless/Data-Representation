from bs4 import BeautifulSoup

with open("../lab1.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())