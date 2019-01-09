# coding: latin1
import requests
import json
from utils import dias
from flask import Flask, request
from flask_cors import CORS, cross_origin
import threading
import logging
from bs4 import BeautifulSoup
from firebase import firebase
from datetime import datetime, timedelta
import time
import codecs
import uuid

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.getLogger().setLevel(logging.INFO)

jsonArchivo = {"records": []}
cookies = {'PHPSESSID': '4ce2c39d145c4b6b556fb8f82782702f'}
token = 'eafd0b6e15d48d5119b53fe6e551ecf3'
def OA():
    logging.info("8A")
    global jsonArchivo
    global cookies
    global token

    lineasF = []

    prefijos = []

    with open('prefijos.txt', 'r') as f:
        lineas = f.readlines()
        lineas = [x.strip() for x in lineas]
        lineasF = lineas

    for x in lineasF:
        prefijos.append(x)
        
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201910&'

    for x in prefijos:
        uidx = str(uuid.uuid4())
        head = 'https://registroapps.uniandes.edu.co/'+uidx
        headers = {'Referer': head}
        logging.info(x+"8A")
        #16 Semanas
        url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?token='+str(token)+'&term=201910&'
        url = url+'ptrm=8A&prefix='+x
        r = requests.get(url, headers=headers, cookies=cookies)
        resp = r.text
        records = json.loads(resp)['records']
        for b in records:
            depto = b['class']
            curso = b['course']
            creditos = b['credits']
            tipo = b['cycle']
            cupos = b['empty']
            nrc = b['nrc']
            title = b['title']
            seccion = b['section']
            profesores = []
            coreq = []
            limit = b["limit"]
            for n in b['coreq']:
                core = {"subject": n['subject'], "number": n['number'], "title": n['title']}
                coreq.append(core)
            prereq = []
            for z in b['prereq']:
                prereq.append(z['code'])
            for c in b['instructors']:
                profesores.append(c['name'])
            compl = []
            for k in b['compl']:
                compl.append(k['nrc'])
            horarios = []
            for d in b['schedules']:
                edificio = d['building']
                salon = d['classroom']
                fechaI = d['date_ini']
                fechaF = d['date_fin']
                horaI = d['time_ini']
                horaF = d['time_fin']
                diasH = dias(d['L'], d['M'], d['I'], d['J'], d['V'], d['S'])
                jsonFin = {'edificio': edificio, 'salon': salon, 'fecha_inicio': fechaI,
                           'fecha_fin': fechaF, 'hora_inicio': horaI, 'hora_fin': horaF, 'dias': diasH}
                horarios.append(jsonFin)
            jsonFinal = {"depto": depto, "curso": curso, "creditos": creditos, "tipo": tipo,
                         "cupos": cupos, "nrc": nrc, "title": title, "seccion": seccion,
                         "profesores": profesores, "horarios": horarios, "compl": compl,
                         "coreq": coreq, "prereq": prereq, "limit": limit}
            jsonArchivo["records"].append(jsonFinal)
    

def OB():
    logging.info("8B")
    global jsonArchivo
    global cookies
    global token
    headers = {'Referer': 'https://registroapps.uniandes.edu.co/oferta_cursos/home.php'}
    lineasF = []

    prefijos = []

    with open('prefijos.txt', 'r') as f:
        lineas = f.readlines()
        lineas = [x.strip() for x in lineas]
        lineasF = lineas

    for x in lineasF:
        prefijos.append(x)
        
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201910&'

    for x in prefijos:
        logging.info(x+"8B")
        uidx = str(uuid.uuid4())
        head = 'https://registroapps.uniandes.edu.co/'+uidx
        headers = {'Referer': head}
        #8B
        url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?token='+str(token)+'&term=201910&'
        url = url+'ptrm=8B&prefix='+x
        r = requests.get(url, headers=headers, cookies=cookies)
        records = json.loads(r.text)['records']
        for b in records:
            depto = b['class']
            curso = b['course']
            creditos = b['credits']
            tipo = b['cycle']
            cupos = b['empty']
            nrc = b['nrc']
            title = b['title']
            seccion = b['section']
            profesores = []
            coreq = []
            limit = b["limit"]
            for n in b['coreq']:
                core = {"subject": n['subject'], "number": n['number'], "title": n['title']}
                coreq.append(core)
            prereq = []
            for z in b['prereq']:
                prereq.append(z['code'])
            for c in b['instructors']:
                profesores.append(c['name'])
            compl = []
            for k in b['compl']:
                compl.append(k['nrc'])
            horarios = []
            for d in b['schedules']:
                edificio = d['building']
                salon = d['classroom']
                fechaI = d['date_ini']
                fechaF = d['date_fin']
                horaI = d['time_ini']
                horaF = d['time_fin']
                diasH = dias(d['L'], d['M'], d['I'], d['J'], d['V'], d['S'])
                jsonFin = {'edificio': edificio, 'salon': salon, 'fecha_inicio': fechaI,
                           'fecha_fin': fechaF, 'hora_inicio': horaI, 'hora_fin': horaF, 'dias': diasH}
                horarios.append(jsonFin)
            jsonFinal = {"depto": depto, "curso": curso, "creditos": creditos, "tipo": tipo,
                         "cupos": cupos, "nrc": nrc, "title": title, "seccion": seccion,
                         "profesores": profesores, "horarios": horarios, "compl": compl,
                         "coreq": coreq, "prereq": prereq, "limit": limit}
            jsonArchivo["records"].append(jsonFinal)

def tres():
    logging.info("Tres")
    global jsonArchivo
    global cookies
    global token
    headers = {'Referer': 'https://registroapps.uniandes.edu.co/oferta_cursos/home.php'}
    lineasF = []

    prefijos = []

    with open('prefijos.txt', 'r') as f:
        lineas = f.readlines()
        lineas = [x.strip() for x in lineas]
        lineasF = lineas

    for x in lineasF:
        prefijos.append(x)

    
        
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201910&'
    #3
    for x in prefijos:
        logging.info(x+"3")
        url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?token='+str(token)+'&term=201910&'
        url = url+'ptrm=3&prefix='+x
        uidx = str(uuid.uuid4())
        head = 'https://registroapps.uniandes.edu.co/'+uidx
        headers = {'Referer': head}
        r = requests.get(url, headers=headers, cookies=cookies)
        records = json.loads(r.text)['records']
        for b in records:
            depto = b['class']
            curso = b['course']
            creditos = b['credits']
            tipo = b['cycle']
            cupos = b['empty']
            nrc = b['nrc']
            title = b['title']
            seccion = b['section']
            profesores = []
            coreq = []
            limit = b['limit']
            for n in b['coreq']:
                core = {"subject": n['subject'], "number": n['number'], "title": n['title']}
                coreq.append(core)
            prereq = []
            for z in b['prereq']:
                prereq.append(z['code'])
            for c in b['instructors']:
                profesores.append(c['name'])
            compl = []
            for k in b['compl']:
                compl.append(k['nrc'])
            horarios = []
            for d in b['schedules']:
                edificio = d['building']
                salon = d['classroom']
                fechaI = d['date_ini']
                fechaF = d['date_fin']
                horaI = d['time_ini']
                horaF = d['time_fin']
                diasH = dias(d['L'], d['M'], d['I'], d['J'], d['V'], d['S'])
                jsonFin = {'edificio': edificio, 'salon': salon, 'fecha_inicio': fechaI,
                           'fecha_fin': fechaF, 'hora_inicio': horaI, 'hora_fin': horaF, 'dias': diasH}
                horarios.append(jsonFin)
            jsonFinal = {"depto": depto, "curso": curso, "creditos": creditos, "tipo": tipo,
                         "cupos": cupos, "nrc": nrc, "title": title, "seccion": seccion,
                         "profesores": profesores, "horarios": horarios, "compl": compl,
                         "coreq": coreq, "prereq": prereq, "limit": limit}
            jsonArchivo["records"].append(jsonFinal)

def completoParcial(prefijos):
    global jsonArchivo
    global cookies
    global token
    time1 = time.time()
    headers = {'Referer': 'https://registroapps.uniandes.edu.co/oferta_cursos/home.php'}
    logging.info("Una mitad")
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201910&'
    #1
    for x in prefijos:
        uidx = str(uuid.uuid4())
        head = 'https://registroapps.uniandes.edu.co/'+uidx
        headers = {'Referer': head}
        logging.info(x+"1")
        url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?token='+str(token)+'&term=201910&'
        url = url+'ptrm=1&prefix='+x
        r = requests.get(url, headers=headers, cookies=cookies)
        records = json.loads(r.text)['records']
        for b in records:
            depto = b['class']
            curso = b['course']
            creditos = b['credits']
            tipo = b['cycle']
            cupos = b['empty']
            nrc = b['nrc']
            title = b['title']
            seccion = b['section']
            profesores = []
            coreq = []
            limit = b['limit']
            for n in b['coreq']:
                core = {"subject": n['subject'], "number": n['number'], "title": n['title']}
                coreq.append(core)
            prereq = []
            for z in b['prereq']:
                prereq.append(z['code'])
            for c in b['instructors']:
                profesores.append(c['name'])
            compl = []
            for k in b['compl']:
                compl.append(k['nrc'])
            horarios = []
            for d in b['schedules']:
                edificio = d['building']
                salon = d['classroom']
                fechaI = d['date_ini']
                fechaF = d['date_fin']
                horaI = d['time_ini']
                horaF = d['time_fin']
                diasH = dias(d['L'], d['M'], d['I'], d['J'], d['V'], d['S'])
                jsonFin = {'edificio': edificio, 'salon': salon, 'fecha_inicio': fechaI,
                           'fecha_fin': fechaF, 'hora_inicio': horaI, 'hora_fin': horaF, 'dias': diasH}
                horarios.append(jsonFin)
            jsonFinal = {"depto": depto, "curso": curso, "creditos": creditos, "tipo": tipo,
                         "cupos": cupos, "nrc": nrc, "title": title, "seccion": seccion,
                         "profesores": profesores, "horarios": horarios, "compl": compl,
                         "coreq": coreq, "prereq": prereq, "limit": limit}
            jsonArchivo["records"].append(jsonFinal)
            
    time2 = time.time()
    print('Function Parcial Completo took {:.3f} ms'.format((time2-time1)*1000.0))

def completo():
    time1 = time.time()
    headers = {'Referer': 'https://registroapps.uniandes.edu.co/oferta_cursos/home.php'}
    global cookies
    global token
    lineasF = []

    prefijos = []

    with open('prefijos.txt', 'r') as f:
        lineas = f.readlines()
        lineas = [x.strip() for x in lineas]
        lineasF = lineas

    for x in lineasF:
        prefijos.append(x)

    uidx = str(uuid.uuid4())
    head = 'https://registroapps.uniandes.edu.co/'+uidx
    headers = {'Referer': head}
        
    primeraMitad = prefijos[:len(prefijos)//2]
    segundaMitad = prefijos[len(prefijos)//2:]

    t1 = threading.Thread(target=completoParcial, args=(primeraMitad,))
    t2 = threading.Thread(target=completoParcial, args=(segundaMitad,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    time2 = time.time()
    
    print('Function Completo took {:.3f} ms'.format((time2-time1)*1000.0))

def decidirDia(dia):
    if(dia=='Lunes'):
        return "L"
    if(dia=='Martes'):
        return "M"
    if(dia=='Miércoles'):
        return "I"
    if(dia=='Jueves'):
        return "J"
    if(dia=='Viernes'):
        return "V"
    if(dia=='Sábado'):
        return "S"

def deportes():
    logging.info("Deportes")
    global jsonArchivo
    global cookies
    global token
    headers = {'Referer': 'https://registroapps.uniandes.edu.co/oferta_cursos/home.php'}
    lineasF = []
    logging.info(token)
    logging.info(cookies)
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201910&'
    #1
    url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?token='+str(token)+'&term=201910&'
    url = url+'ptrm=D&prefix=DEPO'
    uidx = str(uuid.uuid4())
    head = 'https://registroapps.uniandes.edu.co/'+uidx
    headers = {'Referer': head}
    r = requests.get(url, headers=headers, cookies=cookies)
    records = json.loads(r.text)['records']
    for b in records:
        depto = b['class']
        curso = b['course']
        creditos = b['credits']
        tipo = b['cycle']
        cupos = b['empty']
        nrc = b['nrc']
        title = b['title']
        seccion = b['section']
        profesores = []
        coreq = []
        limit = b['limit']
        for n in b['coreq']:
            core = {"subject": n['subject'], "number": n['number'], "title": n['title']}
            coreq.append(core)
        prereq = []
        for z in b['prereq']:
            prereq.append(z['code'])
        for c in b['instructors']:
            profesores.append(c['name'])
        compl = []
        for k in b['compl']:
            compl.append(k['nrc'])
        horarios = []
        for d in b['schedules']:
            edificio = d['building']
            salon = d['classroom']
            fechaI = d['date_ini']
            fechaF = d['date_fin']
            horaI = d['time_ini']
            horaF = d['time_fin']
            diasH = dias(d['L'], d['M'], d['I'], d['J'], d['V'], d['S'])
            jsonFin = {'edificio': edificio, 'salon': salon, 'fecha_inicio': fechaI,
                       'fecha_fin': fechaF, 'hora_inicio': horaI, 'hora_fin': horaF, 'dias': diasH}
            horarios.append(jsonFin)
        jsonFinal = {"depto": depto, "curso": curso, "creditos": creditos, "tipo": tipo,
                     "cupos": cupos, "nrc": nrc, "title": title, "seccion": seccion,
                     "profesores": profesores, "horarios": horarios, "compl": compl,
                     "coreq": coreq, "prereq": prereq, "limit": limit}
        jsonArchivo["records"].append(jsonFinal)
            
            
def principal():    
    global jsonArchivo
    time1 = time.time()
    logging.info("Inicio")
    threads = list()
    t1 = threading.Thread(target=OA)
    t2 = threading.Thread(target=OB)
    t3 = threading.Thread(target=tres)
    t4 = threading.Thread(target=completo)
    t5 = threading.Thread(target=deportes)
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)
    threads.append(t5)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    logging.info("Fin")
    time2 = time.time()
    print('Function took {:.3f} ms'.format((time2-time1)*1000.0))
    with codecs.open('resultado.json', 'w', encoding="latin-1") as f:
        json.dump(jsonArchivo, f, ensure_ascii=False)
    jsonArchivo = {"records": []}

@app.route("/")
@cross_origin()
def mostrar():
    f = codecs.open('resultado.json', 'r', encoding="latin-1")
    return str(f.read()).replace("\'", " ")

def buscarEnFirebase(profe):
    app = firebase.FirebaseApplication('https://senecaio-8fe08.firebaseio.com/', None)
    buscar = '/profesores/'+str(profe)
    result = app.get(buscar, None)
    if(result==None):
        return {'resultado': 0}
    else:
        timestamp = result['timestamp']
        date = datetime.fromtimestamp(timestamp)
        if(datetime.now() - date > timedelta(1)):
            return {'resultado': 1}
        else:
            return {'resultado': 2, 'fetch': result}

def guardar(profe, datos):
    app = firebase.FirebaseApplication('https://senecaio-8fe08.firebaseio.com/', None)
    datos['timestamp'] = time.time()
    donde = '/profesores/'+str(profe)
    result = app.patch(donde, datos)

def scrapEstudiantes(profe):
    url = 'https://api.losestudiantes.co/universidades/universidad-de-los-andes/administracion/buscar/'+str(profe)
    r = requests.get(url)
    slug = darNombreSlug(r.text, profe)
    if(slug == 'No encontrado'):
        retorno = {"promedio": "No encontrado", "nota": "No encontrado", "cantidad": "No encontrado", "slug": "No encontrado"}
    else:
        url = 'https://losestudiantes.co/universidad-de-los-andes/'+slug['depto']+'/profesores/'+slug['slug']
        r = requests.get(url)
        html = BeautifulSoup(r.text, "html.parser")
        profesorPromedio = html.find(id="profesor_promedio").string
        profesorNota = html.find(id="profesor_nota").string
        profesorCantidad = html.find(id="profesor_cantidad").string
        retorno = {"promedio": profesorPromedio, "nota": profesorNota, "cantidad": profesorCantidad, "depto": slug['depto'], "prof": slug['slug']}
        guardar(profe, retorno)
    return str(retorno)

def scrapEstudiantesReemplazar(profe):
    url = 'https://api.losestudiantes.co/universidades/universidad-de-los-andes/administracion/buscar/'+str(profe)
    r = requests.get(url)
    slug = darNombreSlug(r.text, profe)
    if(slug == 'No encontrado'):
        retorno = {"promedio": "No encontrado", "nota": "No encontrado", "cantidad": "No encontrado", "slug": "No encontrado"}
    else:
        url = 'https://losestudiantes.co/universidad-de-los-andes/'+slug['depto']+'/profesores/'+slug['slug']
        r = requests.get(url)
        html = BeautifulSoup(r.text, "html.parser")
        profesorPromedio = html.find(id="profesor_promedio").string
        profesorNota = html.find(id="profesor_nota").string
        profesorCantidad = html.find(id="profesor_cantidad").string
        retorno = {"promedio": profesorPromedio, "nota": profesorNota, "cantidad": profesorCantidad, "depto": slug['depto'], "prof": slug['slug']}
        guardar(profe, retorno)
    return str(retorno)
    
@app.route("/profesor")
@cross_origin()
def profesor():
    retorno = ""
    profe = request.args.get('profe')
    resultado = buscarEnFirebase(profe)
    result = resultado['resultado']
    if(result==0):
        return str(scrapEstudiantes(profe))
    elif(result==1):
        return str(scrapEstudiantesReemplazar(profe))
    elif(result==2):
        return str(resultado['fetch'])

@app.route("/update")
@cross_origin()
def change():
    global cookies
    global token
    retorno = ""
    tokenValue = request.args.get('token')
    cookieValue = request.args.get('cookie')
    cookies = {'PHPSESSID': cookieValue}
    token = tokenValue
    retorno = "PHPSESSID Cambiado a: "+str(cookieValue)+" y token a: "+str(token)
    return str(retorno)

@app.route("/pensum")
@cross_origin()
def pensumapp():
    data = ""
    with open('materiasFinal.json', encoding='ISO-8859-1') as f:
        data = json.load(f)
    data = str(data).replace(u'\\xa0', u' ')
    return str(data).replace(u'\\xa0', u' ')

def darNombreSlug(jsonCompleto, nombreUsuario):
    nombresJson = json.loads(jsonCompleto)
    profes = nombresJson[1]
    retorno = 'No encontrado'
    for x in profes['options']:
        nombrePr = str(x['apellidos'])+' '+str(x['nombre'])
        if(nombrePr.lower().startswith(nombreUsuario.lower())):
            retorno = {'slug': x['slug'], 'depto': x['departamento_slug']}
    return retorno
        
@app.route("/escribir")
@cross_origin()
def escribir():
    logging.info("Antes")
    threads = list()
    t = threading.Thread(target=principal)
    threads.append(t)
    t.start()
    return ("OK")

if __name__ == '__main__':
    app.run(debug=True)
