import requests
import json
import uuid
import threading

def peticionA():
    uidx = str(uuid.uuid4())
    head = 'https://registroapps.uniandes.edu.co/'+uidx
    headers = {'Referer': head, 'User-Agent': 'aaaaa'}
    cookies = {'PHPSESSID': '4aad3900e1b430911bff3100037b8498'}
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?1f76d6492f1e1cbd95732a6b50e9b613&term=201910&ptrm=1&prefix=ADMI'
    r = requests.get(url, headers=headers, cookies=cookies)
    print(r.text)
    
def peticionB():
    uidx = str(uuid.uuid4())
    head = 'https://registroapps.uniandes.edu.co/'+uidx
    headers = {'Referer': head, 'User-Agent': 'aaaaa'}
    cookies = {'PHPSESSID': '4aad3900e1b430911bff3100037b8498'}
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?1f76d6492f1e1cbd95732a6b50e9b613&term=201910&ptrm=1&prefix=ICYA'
    r = requests.get(url, headers=headers, cookies=cookies)
    print(r.text)
    
t1 = threading.Thread(target=peticionA)
t2 = threading.Thread(target=peticionB)

t1.start()
t1.join()

t2.start()


t2.join()
