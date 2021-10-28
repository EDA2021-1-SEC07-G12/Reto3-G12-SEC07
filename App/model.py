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
                'dateIndex': None
                }

    analyzer['dateIndex'] = om.newMap(omaptype="BRT", comparefunction=compareDates)
    return analyzer



# Funciones para agregar informacion al catalogo
def addSight(mapa,sight):
   
    
    om.put(mapa,sight["datetime"],sight)
    nodos= om.size(mapa)
    
   # print(sight["datetime"])
    
# Funciones para creacion de datos


# Funciones de consulta
def hola(catalogo,inicio,final):
    lista=tv.postorder(catalogo)
    mapa=mp.newMap(150,
        maptype="CHAINING", loadfactor=1.5)
    contador=0
    retorno=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista):
        hora = i["datetime"][11:-3]
        #if hora=="00:00":
            #hora="24:00"
        if inicio<=hora<=final:
            if mp.contains(mapa,hora)==False:
                mp.put(mapa,hora,1)
            else:
                value=mp.get(mapa,hora)["value"]
                value+=1
                mp.put(mapa,hora,value)
    print(contador)
            #if hora!= "00:00":
               # lt.addLast(retorno,i)
    for j in lt.iterator(mp.keySet(mapa)):
        lt.addLast(retorno,mp.get(mapa,j))
    ordenado=  ms.sort(retorno,ordenarFecha)
    print(ordenado)
def hola1(catalogo,inicio,final):
    lista=tv.postorder(catalogo)
    mapa=mp.newMap(150,
        maptype="CHAINING", loadfactor=1.5)
    contador=0
    retorno=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista):
        hora = i["datetime"][11:-3]
        if hora=="00:00":
            hora="24:00"
            print(hora)
    
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
    
    if (date1["value"] >= date2["value"]):
        return 1
    else:
        return 0


