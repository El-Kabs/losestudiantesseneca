def dias(lunes, martes, miercoles, jueves, viernes, sabado):
    dias = []
    if(lunes != None):
        dias.append('L')
    if(martes != None):
        dias.append('M')
    if(miercoles != None):
        dias.append('I')
    if(jueves != None):
        dias.append('J')
    if(viernes != None):
        dias.append('V')
    if(sabado != None):
        dias.append('S')
    return dias

