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


                }

    analyzer['dateIndex'] = om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer['sightings'] = lt.newList("ARRAY_LIST")
    analyzer["cityIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer["secondsIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer["longitudeIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer["longitudeIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)


    return analyzer



# Funciones para agregar informacion al catalogo

def addHour(mapa,sight):
    arbol=mapa["secondsIndex"]
    hora = sight["datetime"][11:-3]
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
   om.put(arbol,sight["datetime"],sight)
    
    
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

def addSeconds(mapa,sight):
    arbol=mapa["secondsIndex"]
    if om.contains(arbol,sight["duration (seconds)"])==False:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,sight)
        om.put(arbol,sight["duration (seconds)"], lista)
    else:
        lista1=om.get(arbol,sight["duration (seconds)"])
        lista1=lista1["value"]
        lt.addLast(lista1,sight)
        om.put(arbol,sight["duration (seconds)"], lista1)

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
def hola(catalogo,inicio,final):
    catalogo=catalogo["secondsIndex"]
    lista=lt.newList("ARRAY_LIST")
    rango=om.values(catalogo,inicio,final)
    for i in lt.iterator(rango):
        for j in lt.iterator(i):
            lt.addLast(lista,j)
    
    ordenado=ms.sort(lista,ordenarFecha1)
    sublista=lt.subList(ordenado,ordenado["size"]-5,5)
    sublista1=lt.subList(ordenado,1,5)
    return sublista1
    
   # for i in lt.iterator(ordenado):
   #     print(i)
    
    

def requerimiento4(catalogo,inicio,final):
    
    return om.keys(catalogo,inicio,final)

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
                
    return lista

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

def ordenarHora(hora1,hora2):
    if (hora1["size"] >= hora2["size"]):
        return True
    else:
        return False