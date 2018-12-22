import requests
import json
from utils import dias
from flask import Flask, request
from flask_cors import CORS, cross_origin
import threading
import logging
from bs4 import BeautifulSoup

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.getLogger().setLevel(logging.INFO)

def principal():
    logging.info("Inicio")
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

    jsonArchivo = {"records": []}
    for x in prefijos:
        logging.info(x)
        #16 Semanas
        url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201910&'
        url = url+'ptrm=1&prefix='+x
        r = requests.get(url, headers=headers)
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
                         "coreq": coreq, "prereq": prereq}
            jsonArchivo["records"].append(jsonFinal)
        #8A
        logging.info("8A")
        url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201910&'
        url = url+'ptrm=8A&prefix='+x
        r = requests.get(url, headers=headers)
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
                         "coreq": coreq, "prereq": prereq}
            jsonArchivo["records"].append(jsonFinal)
        #8B
        logging.info("8B")
        url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201910&'
        url = url+'ptrm=8B&prefix='+x
        r = requests.get(url, headers=headers)
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
                         "coreq": coreq, "prereq": prereq}
            jsonArchivo["records"].append(jsonFinal)
        #3
        logging.info("8A")
        url = 'https://registroapps.uniandes.edu.co/oferta_cursos/api/get_courses.php?term=201910&'
        url = url+'ptrm=8B&prefix='+x
        logging.info(url)
        r = requests.get(url, headers=headers)
        logging.info(r.text)
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
                         "coreq": coreq, "prereq": prereq}
            jsonArchivo["records"].append(jsonFinal)
    logging.info("Fin")
    with open('resultado.json', 'w') as f:
        json.dump(jsonArchivo, f, ensure_ascii=False)

@app.route("/")
@cross_origin()
def mostrar():
    with open('resultado.json', 'r', encoding="latin-1") as theFile:
        data = theFile.read()
        return str(data).replace("\'", " ")

@app.route("/profesor")
@cross_origin()
def profesor():
    retorno = ""
    profe = request.args.get('profe')
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
    return str(retorno)

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
