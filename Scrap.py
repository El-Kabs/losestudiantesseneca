import requests
import json

headers = {'Referer': 'https://registroapps.uniandes.edu.co/oferta_cursos/home.php'}

prefijos = set([])

r = requests.get('https://registroapps.uniandes.edu.co/oferta_cursos/api/get_programs.php?term=201910&ptrm=1', headers=headers)

jsonF = json.loads(r.text)
for x in jsonF['records']:
    prefijos.add(x['prefix'])

r = requests.get('https://registroapps.uniandes.edu.co/oferta_cursos/api/get_programs.php?term=201910&ptrm=8A', headers=headers)

jsonF = json.loads(r.text)
for x in jsonF['records']:
    prefijos.add(x['prefix'])

r = requests.get('https://registroapps.uniandes.edu.co/oferta_cursos/api/get_programs.php?term=201910&ptrm=8B', headers=headers)

jsonF = json.loads(r.text)
for x in jsonF['records']:
    prefijos.add(x['prefix'])

prefijos = sorted(prefijos)

for x in prefijos:
    with open('prefijos.txt', 'a') as f:
        f.write(x+'\n')
