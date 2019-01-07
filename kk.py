from bs4 import BeautifulSoup
import requests

url = 'https://decanaturadeestudiantes.uniandes.edu.co/index.php/es/cursos'
r = requests.get(url)
html = BeautifulSoup(r.text, "html.parser")
table = html.find('table')
td = table.find('td')
tbody = td.find('tbody')
tdd = tbody.findAll('td', style="text-align: center;")
for x in tdd:
    print(x.string)
    
