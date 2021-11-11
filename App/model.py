"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Trees import traversal as tv
import folium
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    """ Inicializa el analizador
    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas
    Retorna el analizador inicializado.
    """
    analyzer = {
                'dateIndex': None,
                'cityIndex': None,
                "secondsIndex":None,
                "longitudeIndex": None,
                "hoursIndex": None,
                "sightings":None


                }

    analyzer['dateIndex'] = om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer['sightings'] = lt.newList("ARRAY_LIST")
    analyzer["cityIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer["secondsIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer["longitudeIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)
    
    analyzer["durationIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)


    return analyzer



# Funciones para agregar informacion al catalogo
0
def addHour(mapa,sight):
    arbol=mapa["secondsIndex"]
    hora = sight["datetime"][11:-3]
    sight["time"]=hora
    if om.contains(arbol,hora)==False:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,sight)
        om.put(arbol,hora, lista)
    else:
        lista1=om.get(arbol,hora)
        lista1=lista1["value"]
        lt.addLast(lista1,sight)
        
def addSighting(mapa,sight):
    arbol=mapa["sightings"]
    
    lt.addLast(arbol,sight)

def addSight(mapa,sight):
    arbol=mapa["dateIndex"]
    if om.contains(arbol,sight["datetime"])==False:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,sight)
        om.put(arbol,sight["datetime"], lista)
    else:
        lista1=om.get(arbol,sight["datetime"])
        lista1=lista1["value"]
        lt.addLast(lista1,sight)
    
    
def addCity(mapa,sight):
    arbol=mapa["cityIndex"]
    if om.contains(arbol,sight["city"])==False:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,sight)
        om.put(arbol,sight["city"], lista)
    else:
        lista1=om.get(arbol,sight["city"])
        lista1=lista1["value"]
        lt.addLast(lista1,sight)
        
   # print(sight["datetime"])



def addTime(mapa,sight):
    mapa=mapa["durationIndex"]
    

    duracion=float(sight["duration (seconds)"])
    if om.contains(mapa,duracion)==False:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,sight)
        om.put(mapa,duracion, lista)
    else:
        lista1=om.get(mapa,duracion)
        lista1=lista1["value"]
        lt.addLast(lista1,sight)

def addLongitude(mapa,sight):

    arbol=mapa["longitudeIndex"]
    variable1=float(sight["longitude"])
    variable1=round(variable1,2)
    if om.contains(arbol,variable1)==False:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,sight)
        om.put(arbol,float(sight["longitude"]), lista)
    else:
        lista1=om.get(arbol,variable1)
        lista1=lista1["value"]
        lt.addLast(lista1,sight)
        om.put(arbol,float(sight["longitude"]), lista1)
    
# Funciones para creacion de datos


# Funciones de consulta


def requerimiento_1(catalog,ciudad):
    catalog=catalog["cityIndex"]
    ciudades=lt.size(om.keySet(catalog))
    variable1= om.get(catalog,ciudad)
    cantidad = variable1["value"]["size"]
    listaobras=lt.newList("ARRAY_LIST")
    obras=ms.sort(variable1["value"],ordenarFecha2)
    sublistarecientes=lt.subList(obras,1,3)
    sublistaantiguas=lt.subList(obras,lt.size(obras)-2,3)

    retorno=lt.newList('ARRAY_LIST')

    lt.addLast(retorno, ciudades)
    lt.addLast(retorno, cantidad)
    lt.addLast(retorno, sublistarecientes)
    lt.addLast(retorno, sublistaantiguas)
    
    ciudadescan=lt.newList('ARRAY_LIST')
    mapa = mp.newMap(20000,
        maptype="CHAINGING", loadfactor=1)
    for i in lt.iterator(om.keySet(catalog)):
        ciudad= om.get(catalog,i)
        mp.put(mapa,i,ciudad["value"]["size"])
    llaves1=lt.newList('ARRAY_LIST')
    for i in lt.iterator(mp.keySet(mapa)):
        llaves=mp.get(mapa,i)
        lt.addLast(llaves1,llaves)

    llaves1=ms.sort(llaves1,ordenarCiudad)
    

    lt.addLast(retorno,llaves1)
    return retorno
def requerimiento_2(catalogo,inferior,superior):

    
    e=om.get(catalogo,om.maxKey(catalogo))

    max=e['key']

    cantidad=lt.size(e['value'])

    llaves=om.keys(catalogo,inferior,superior)

    lista=lt.newList('ARRAY_LIST')

    for i in lt.iterator(llaves):

        tabla=om.get(catalogo,i)

        valor=tabla['value']

        for j in lt.iterator(valor):

            lt.addLast(lista,j)



    l3_3=lt.newList('ARRAY_LIST')

    if lt.size(lista)>6:

        contador1=3

        contador2=-2

    while contador1>=1 :

            temp=lt.newList('ARRAY_LIST')

            elemento=lt.getElement(lista,contador1)

            lt.addLast(temp,elemento['datetime'])

            lt.addLast(temp,elemento['city'])

            lt.addLast(temp,elemento['country'])

            lt.addLast(temp,elemento['duration (seconds)'])

            lt.addLast(temp,elemento['shape'])



            lt.addLast(l3_3,temp)

            contador1-=1

    while contador2<=0:

            temp=lt.newList('ARRAY_LIST')

            elemento=lt.getElement(lista,contador2)

            lt.addLast(temp,elemento['datetime'])

            lt.addLast(temp,elemento['city'])

            lt.addLast(temp,elemento['country'])

            lt.addLast(temp,elemento['duration (seconds)'])

            lt.addLast(temp,elemento['shape'])



            lt.addLast(l3_3,temp)

            contador2+=1

       



    return (l3_3,(max,cantidad))


def requerimiento_3(catalogo,inicio,final):
    retorno=lt.newList('ARRAY_LIST')
    catalogo=catalogo["secondsIndex"]
    lista=lt.newList("ARRAY_LIST")
    cantidad=lt.size(om.keySet(catalogo))
    rango=om.values(catalogo,inicio,final)
    for i in lt.iterator(rango):
        for j in lt.iterator(i):
            
            lt.addLast(lista,j)
    lista1=lt.newList("ARRAY_LIST")
    ordenado=ms.sort(lista,ordenarFecha2)
   # sublista=lt.subList(ordenado,ordenado["size"]-2,3)
  #  sublista1=lt.subList(ordenado,1,3)
    
    for i in lt.iterator(om.keys(catalogo,inicio,final)):
        lt.addLast(lista1,om.get(catalogo,i))

    lista2=ms.sort(lista1,ordenarFecha)

    lt.addLast(retorno,lt.subList(lista2,1,5))
    #lt.addLast(retorno,lt.size(lista))
    #lt.addLast(retorno,cantidad)
    #lt.addLast(retorno,lt.subList(ordenado,1,5))
    lt.addLast(retorno,ordenado)
    return retorno
   # for i in lt.iterator(ordenado):
   #     print(i)
    
    

def requerimiento4(catalogo,inicio,final):
    catalogo=catalogo["dateIndex"]
    contador=0
    lista=lt.newList("ARRAY_LIST")
    rango= om.keys(catalogo,inicio,final)
    rango1= om.values(catalogo,inicio,final)
   ## tamano=lt.size(rango)
    listar=lt.newList("ARRAY_LIST")
    
   
    for i in lt.iterator(rango):
        
        valor=om.get(catalogo,i)
        lt.addLast(lista,valor)

    for i in lt.iterator(rango1):
        for j in lt.iterator(i):
            
            lt.addLast(listar,j)
        
    listar=ms.sort(listar,ordenarFecha2)
    
    retorno=lt.newList("ARRAY_LIST")
    lt.addLast(retorno,lt.size(rango) )
    lt.addLast(retorno,lt.size(om.keySet(catalogo)))
    lt.addLast(retorno,lt.subList(lista,1,5))
    lt.addLast(retorno,lt.subList(lista,lt.size(lista)-4,5))
    lt.addLast(retorno,om.get(catalogo,lt.getElement(rango,1)))
    lt.addLast(retorno,lt.subList(listar,1,3))
    lt.addLast(retorno,lt.subList(listar,lt.size(listar)-2,3))
    return retorno


def requerimiento5(catalogo,lonini,lonfinal,latini,latfinal):
    catalogo=catalogo["longitudeIndex"]
    lista=lt.newList("ARRAY_LIST")
    longitudes=om.keys(catalogo,lonini,lonfinal)    
    for i in lt.iterator(longitudes):
        variable= om.get(catalogo,i)
        variable=variable["value"]
        for j in lt.iterator(variable):
            if latini<=float(j["latitude"])<=latfinal :
                lt.addLast(lista,j)
    lista=ms.sort(lista,ordenarFecha2)
    retorno=lt.newList("ARRAY_LIST")
    lt.addLast(retorno,lt.size(lista))         
    lt.addLast(retorno,lt.subList(lista,1,5))   
    lt.addLast(retorno,lt.subList(lista,lt.size(lista)-4,5)) 
    return retorno

def bono(catalogo,lonini,lonfinal,latini,latfinal):
    catalogo=catalogo["longitudeIndex"]
    promediolon=(lonini+lonfinal)/2
    promediolat=(latfinal+latini)/2
    m = folium.Map(location=[promediolat, promediolon], zoom_start=10)
    lista=lt.newList("ARRAY_LIST")
    longitudes=om.keys(catalogo,lonini,lonfinal)    
    for i in lt.iterator(longitudes):
        variable= om.get(catalogo,i)
        variable=variable["value"]
        for j in lt.iterator(variable):
            if latini<=float(j["latitude"])<=latfinal :
                folium.Marker(
    [j["latitude"], j["longitude"]], popup="Datetime : " + j["datetime"]).add_to(m)
    
    
    m.save("file:///C:/Users/User/Reto3-G12-SEC07-5/App/index.html")
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def ordenarFecha(date1, date2):
    
    if (date1["key"] >= date2["key"]):
        return 1
    else:
        return 0


def ordenarFecha1(date1, date2):
    
    if (date1["datetime"] >= date2["datetime"]):
        return 1
    else:
        return 0
def ordenarFecha2(date1, date2):
    
    if (date1["datetime"] >= date2["datetime"]):
        return 1
    else:
        return 0
def ordenarHora(hora1,hora2):
    if (hora1["size"] >= hora2["size"]):
        return True
    else:
        return False

def ordenarCiudad(ciudad1,ciudad2):
    if (ciudad1["value"] >= ciudad2["value"]):
        return True
    else:
        return False

def ordenarTiempo(tiempo1,tiempo2):
    if (tiempo1["time"] >= tiempo1["time"]):
        return True
    else:
        return False

