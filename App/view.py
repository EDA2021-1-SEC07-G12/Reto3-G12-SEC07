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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

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
        print("Datos correctamente cargados mi pana")
        xd= om.keySet(catalog["secondsIndex"])
        for i in lt.iterator(xd):
            print(i)
        


        #print("El arbol tiene  " + str(om.size(mapa)) + " elementos ")
       # print("El arbol cargado tiene una altura de " + str(om.height(mapa)))
       # print( "Menor llave " + str(om.minKey(mapa)))
        #print("Mayor llave " + str(om.maxKey(mapa)))
        
    elif int(inputs[0]) == 2:
        print("Hola")
        
        variable1= om.get(catalog["cityIndex"],"las vegas")
        variable1=variable1["value"]
        variable1=lt.size(variable1)

        print("Hay " + str(variable1) + " avistamientos en la ciudad insertada")
        print("Hay " + str(lt.size(om.keySet(catalog["cityIndex"]))) + " Ciudades diferentes ")
        #print(variable)
    elif int(inputs[0]) == 3:
        print("Hola")
        print(controller.requerimiento4(catalog)) 

    elif int(inputs[0]) == 4:
        print("Hola")
        print(controller.hola(catalog)) 
        

    elif int(inputs[0]) == 5:
        print("Hola")
        print(cont)
        
    elif int(inputs[0]) == 6:
        print("Hola")
        print(cont["cityIndex"])

    elif int(inputs[0]) == 7:
        print("Hola")
        print(controller.requerimiento5(catalog))


    else:
        sys.exit(0)
sys.exit(0)
