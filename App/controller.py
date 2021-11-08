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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog= model.newAnalyzer()

    return catalog
# Funciones para la carga de datos

def loadData(catalog):
    loadArtist(catalog)
    #loadArtWork(catalog)
    
def loadArtist(catalog):
    booksfile = cf.data_dir + 'UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for Sight in input_file:
        model.addSight(catalog, Sight)
        model.addCity(catalog, Sight)
        model.addLongitude(catalog, Sight)
        model.addSighting(catalog, Sight)
        model.addHour(catalog, Sight)
        model.addTime(catalog, Sight)
def hola(catalogo):
    inicio=input("Introduce hora inicial en formato HH:MM: ")
    final=input("Introduce hora final en formato HH:MM: ")
    return model.hola(catalogo,inicio,final)

def requerimiento4(catalogo):
    inicio=input("Introduce hora inicial en formato AA-MM-DD ")
    final=input("Introduce hora final en formato AA-MM-DD ")
    return model.requerimiento4(catalogo,inicio,final)
def requerimiento5(catalogo):
    loninit=float(input("Introduce longitud incial: "))
    lonfinal=float(input("Introduce longitud final: "))
    latinit=float(input("Introduce latitud incial: "))
    latfinal=float(input("Introduce latitud incial: "))
    return model.requerimiento5(catalogo,loninit,lonfinal,latinit,latfinal)

def bono(catalogo):
    loninit=float(input("Introduce longitud incial: "))
    lonfinal=float(input("Introduce longitud final: "))
    latinit=float(input("Introduce latitud incial: "))
    latfinal=float(input("Introduce latitud incial: "))
    return model.bono(catalogo,loninit,lonfinal,latinit,latfinal)

def req_2(catalogo):

    inferior=float(input("Introduce limite inferior en segundos: "))

    superior=float(input("Introduce limite superior en segundos: "))

    return model.requerimiento_2(catalogo,inferior,superior)


# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
