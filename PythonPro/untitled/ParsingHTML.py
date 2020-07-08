#Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.



import requests
from bs4 import BeautifulSoup
import urllib.request

# Fetch the html file
request =  urllib.request.Request('https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/icicibank/ICI02')
response = urllib.request.urlopen(request)
html_doc = response.read()
print(response.read().decode('utf-8'))
# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

# Format the parsed html file
strhtm = soup.prettify()

# Print the first few characters
print (strhtm[:225])

print (soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

for x in soup.find_all('table'): print(x.string)


