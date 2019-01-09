import requests
import json
import uuid
import threading

def peticionA():
    uidx = str(uuid.uuid4())
    head = 'https://registroapps.uniandes.edu.co/'+uidx
    headers = {'Referer': head, 'User-Agent': 'aaaaa'}
    cookies = {'PHPSESSID': 'ba96414e8c79843038974893f072a007'}
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?token=f62515ff9b004a927d0e865ac54603d4&term=201910&ptrm=1&prefix=ADMI'
    r = requests.get(url, headers=headers, cookies=cookies)
    print(r.text)
    
def peticionB():
    uidx = str(uuid.uuid4())
    head = 'https://registroapps.uniandes.edu.co/'+uidx
    headers = {'Referer': head, 'User-Agent': 'aaaaa'}
    cookies = {'PHPSESSID': 'ba96414e8c79843038974893f072a007'}
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?token=f62515ff9b004a927d0e865ac54603d4&term=201910&ptrm=1&prefix=ICYA'
    r = requests.get(url, headers=headers, cookies=cookies)
    print(r.text)
    
t1 = threading.Thread(target=peticionA)
t2 = threading.Thread(target=peticionB)

t1.start()
t1.join()

t2.start()


t2.join()
