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

                }

    analyzer['dateIndex'] = om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer["cityIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer["secondsIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)
    analyzer["longitudeIndex"]= om.newMap(omaptype="BRT", comparefunction=compareDates)
    return analyzer



# Funciones para agregar informacion al catalogo
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
    sight["longitude"]=float(sight["longitude"])
    sight["longitude"]=round(sight["longitude"],2)
    if om.contains(arbol,sight["longitude"])==False:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,sight)
        om.put(arbol,sight["longitude"], lista)
    else:
        lista1=om.get(arbol,sight["longitude"])
        lista1=lista1["value"]
        lt.addLast(lista1,sight)
        om.put(arbol,sight["longitude"], lista1)
    
# Funciones para creacion de datos


# Funciones de consulta
def hola(catalogo,inicio,final):
    lista=tv.postorder(catalogo)
    mapa=mp.newMap(150,
        maptype="CHAINING", loadfactor=1.5)
    contador=0
    retorno=lt.newList("ARRAY_LIST")
    retorno1=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista):
        hora = i["datetime"][11:-3]
        if inicio<=hora<=final:
            contador+= 1
            if mp.contains(mapa,hora)==False:
                mp.put(mapa,hora,1)
            else:
                value=mp.get(mapa,hora)["value"]
                value+=1
                mp.put(mapa,hora,value)
   
    for j in lt.iterator(mp.keySet(mapa)):
        lt.addLast(retorno,mp.get(mapa,j))
    ordenado=  ms.sort(retorno,ordenarFecha)
    ordenado=lt.subList(retorno,1,5)
    lt.addLast(retorno1,contador)
    lt.addLast(retorno1,lt.size(mp.keySet(mapa)))
    lt.addLast(retorno1,ordenado)
    return retorno1

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
            if latini<=float(j["latitude"])<=latfinal and j["state"]=="nm":
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
