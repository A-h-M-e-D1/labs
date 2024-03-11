from bs4 import BeautifulSoup
import urllib.request
import os
url = input("Enter target URL => ")
page = urllib.request.urlopen(url)
html_page = page.read()

soup = BeautifulSoup(html_page, 'html.parser')
# print(soup.prettify())

# to retrieve all links
print('ALL Links is: ')
with open('links.txt', 'w', encoding='utf-8') as links_file:
    links_file.write('ALL Links is: \n')
    for link in soup.find_all('a'):
        links_file.write(link.get('href') + '\n')

print("Links saved in 'links.txt'")

# input fileds
with open('input.txt', 'w', encoding='utf-8') as input_file:
    input_file.write('Input fields are: \n')
    for field in soup.find_all('input'):
        input_type = field.get('type')
        input_name = field.get('name')
        input_file.write(
            f"Input field - Type: {input_type}, Name: {input_name}\n")
print("Fields saved in 'fields.txt'")
