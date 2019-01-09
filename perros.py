import requests
import json
import uuid
import threading

def peticionA():
    uidx = str(uuid.uuid4())
    head = 'https://registroapps.uniandes.edu.co/'+uidx
    headers = {'Referer': head}
    cookies = {'PHPSESSID': '4ce2c39d145c4b6b556fb8f82782702f'}
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?token=6b34c99a1432c9bc073dbe75d2ba1860&term=201910&ptrm=1&prefix=ADMI'
    r = requests.get(url, headers=headers, cookies=cookies)
    print(r.text)
    
def peticionB():
    uidx = str(uuid.uuid4())
    head = 'https://registroapps.uniandes.edu.co/'+uidx
    headers = {'Referer': head, 'User-Agent': 'aaaaa'}
    cookies = {'PHPSESSID': '4ce2c39d145c4b6b556fb8f82782702f'}
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?token=6b34c99a1432c9bc073dbe75d2ba1860&term=201910&ptrm=1&prefix=ICYA'
    r = requests.get(url, headers=headers, cookies=cookies)
    print(r.text)
    
t1 = threading.Thread(target=peticionA)
t2 = threading.Thread(target=peticionB)

t1.start()
t1.join()

t2.start()


t2.join()
