#Test that you can read a file , using lab1.html file tht we mde last week 

from bs4 import BeautifulSoup

with open("../lab1.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print(soup.prettify())