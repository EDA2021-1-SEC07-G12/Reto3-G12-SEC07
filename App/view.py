"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Trees import traversal as tv
assert cf
from DISClib.ADT import map as mp

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Cargar avistamientos por ciudad insertada")
    print("3- Contar los avistamientos por duración")
    print("4- Contar los avistamientos por Hora/Minutos")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una Zona Geográfica")
catalog= controller.initCatalog()
cont=controller.initCatalog()
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        
        controller.loadData(catalog)
        #print("Se cargaron " + str(lt.size(om.keySet(catalog["dateIndex"]))))
        print("Datos correctamente cargados ")
        print("Se cargaron " + str(lt.size(catalog["sightings"])) + " datos  ")
        
        print("Hay " + str(lt.size(om.keySet(catalog["cityIndex"]))) + " Ciudades diferentes ")
        print("El avistamiento mas antiguo " +  str(om.minKey(catalog["dateIndex"])))
        print("El avistamiento mas reciente " +  str(om.maxKey(catalog["dateIndex"])))


        #print("El arbol tiene  " + str(om.size(mapa)) + " elementos ")
       # print("El arbol cargado tiene una altura de " + str(om.height(mapa)))
       # print( "Menor llave " + str(om.minKey(mapa)))
        #print("Mayor llave " + str(om.maxKey(mapa)))
        
    elif int(inputs[0]) == 2:
        
        
        resp=controller.requerimiento1(catalog)

        mapa=lt.getElement(resp,5)

        mapa=lt.subList(mapa,1,5)
        print("Las 5 ciudades con mas avistamientos son : ")
        for i in lt.iterator(mapa):

            print("Ciudad: " + str(i["key"] + " Avistamientos " + str(i["value"])))
        print("Existen " + str(lt.getElement(resp,1)) + " ciudades con algún tipo de avistamiento")
        print("Existen " + str(lt.getElement(resp,2)) + " avistamientos en la ciudad insertada")
        print("Los avistamientos mas recientes en la ciudad insertada : ")
        for i in lt.iterator(lt.getElement(resp,3)):
            print("Fecha y hora: " + str(i["datetime"])+ " ciudad: " + str(i["city"]) + " país: " + str(i["country"]) + " duración:" + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) )) 
        print("Los avistamientos mas antiguos en la ciudad insertada : ")
        for i in lt.iterator(lt.getElement(resp,4)):
            print("Fecha y hora: " + str(i["datetime"]) + " país: " + str(i["country"]) + " duración: " + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) )) 
        
            
        #print("Hay " + str(variable1) + " avistamientos en la ciudad insertada")
        

        
        #print(variable)
    elif int(inputs[0]) == 3:

        resp=controller.req_2(catalog["durationIndex"])

        #resp=catalog["durationIndex"]
        #resp=controller.req_2(resp)
        
        print(resp)
        print('\n')

        print("Los avistamientos con mayor duracion fueron: ")

        print(('Duración: {} - Cantidad: {}').format(resp[1][0],resp[1][1]))

        print('\n')

        print('Los avistamientos con menor y mayor duración en el intervalo insertado son: ')

        for i in lt.iterator(resp[0]):

            print (i['elements'])

    elif int(inputs[0]) == 4:
        print("Hola")
        resp= controller.requerimiento_3(catalog)
        #print(resp)
        print("Las horas mas tardías con su numero de avistamientos son: ")

        for i in lt.iterator(lt.getElement(resp,1)):
            print("Ciudad: " + str(i["key"]) + " Avistamientos: " + str(i["value"]["size"]))
        
        avistamientos= lt.getElement(resp,2)
        avistamientos1= lt.subList(avistamientos,1,3)

        avistamientos2= lt.subList(avistamientos,lt.size(avistamientos)-2,3)
        

        for i in lt.iterator(avistamientos1):
            print("Fecha y hora: " + str(i["datetime"])+ " ciudad: " + str(i["city"]) + " país: " + str(i["country"]) + " duración:" + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) )) 
        print("Los avistamientos mas antiguos en la ciudad insertada : ")
        for i in lt.iterator(avistamientos2):
            print("Fecha y hora: " + str(i["datetime"]) + " país: " + str(i["country"]) + " duración: " + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) )) 
    elif int(inputs[0]) == 5:
        resp= controller.requerimiento4(catalog)
       
        print("Hay " + str(lt.getElement(resp,2)) + " Fechas diferentes con avistamientos")
        print("Los avistamientos mas recientes en el intervalo insertado ")
        print("Fecha " + str(lt.getElement(resp,5)['key']) + " avistamientos " +str(lt.getElement(resp,5)['value']["size"]))

        for i in lt.iterator(lt.getElement(resp,6)):
            print("Fecha y hora: " + str(i["datetime"])+ " ciudad: " + str(i["city"]) + " país: " + str(i["country"]) + " duración:" + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) )) 
        print("Los avistamientos mas antiguos en el intervalo insertado : ")
        for i in lt.iterator(lt.getElement(resp,7)):
            print("Fecha y hora: " + str(i["datetime"]) + " país: " + str(i["country"]) + " duración: " + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) )) 
        
        

        
    

    elif int(inputs[0]) == 6:
        print("Hola")
        resp= controller.requerimiento5(catalog)
        print("Hay una cantidad de " + str(lt.getElement(resp,1)) + " avistamientos en la zona geografica insertada")
        print("Intervalos de los avistamientos mas recientes en la zona insertada")

        for i in lt.iterator(lt.getElement(resp,2)):
            print("Fecha y hora: " + str(i["datetime"])+ " ciudad: " + str(i["city"]) + " país: " + str(i["country"]) + " duración:" + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) + " latitud: " + str(i["latitude"]) + " longitud: " + str(i["longitude"]))) 
        print("Los avistamientos mas antiguos en el intervalo insertado : ")
        for i in lt.iterator(lt.getElement(resp,3)):
            print("Fecha y hora: " + str(i["datetime"]) + " país: " + str(i["country"]) + " duración: " + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) + " latitud: " + str(i["latitude"]) + " longitud: " + str(i["longitude"])))
        
        

    elif int(inputs[0]) == 7:
        print("Hola")
        resp= controller.requerimiento5(catalog)
        print("Hay una cantidad de " + str(lt.getElement(resp,1)) + " avistamientos en la zona geografica insertada")
        
        print("Los avistamientos mas recientes en la zona insertada son")
        for i in lt.iterator(lt.getElement(resp,2)):
            print("Fecha y hora: " + str(i["datetime"])+ " ciudad: " + str(i["city"]) + " país: " + str(i["country"]) + " duración:" + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) + " latitud: " + str(i["latitude"]) + " longitud: " + str(i["longitude"]))) 
        print("Los avistamientos mas antiguos en el intervalo insertado : ")
        for i in lt.iterator(lt.getElement(resp,3)):
            print("Fecha y hora: " + str(i["datetime"]) + " país: " + str(i["country"]) + " duración: " + str(i["duration (seconds)"] + " forma: " + str(i["shape"]) + " latitud: " + str(i["latitude"]) + " longitud: " + str(i["longitude"])))
        
        controller.bono(catalog)

    else:
        sys.exit(0)
sys.exit(0)
