#Creacion de archivo csv

with open ('paises.csv','w') as archivo:
    archivo.write('Nombre,Poblacion,Superficie,Continente\n')


def comprobar_existencia(pais):
    existe = False
    with open('paises.csv','r') as archivo:
        lineas = archivo.readlines()
        for elemento in lineas:
            nombre,poblacion,superficie,continente = elemento.strip().split(',')
            if nombre == pais:
                existe = True
    return existe

def actualizar_archivo(nombre,poblacion,superficie,continente):
    if comprobar_existencia(pais):
        archivo_actualizado = []
        with open('paises.csv','r') as archivo:
            lineas = archivo.readlines()
                    
        for linea in lineas:
            nombre,poblacion,superficie,continente = linea.strip().split(",")
            if nombre == pais:
                archivo_actualizado.append(f"{pais},{nueva_poblacion},{nueva_superficie},{continente}\n")
            else:
                archivo_actualizado.append(linea)

        with open('paises.csv', 'w') as archivo:
            archivo.writelines(archivo_actualizado)
    
    else:
        with open('paises.csv','a') as archivo:
            archivo.write(f"{nombre},{poblacion},{superficie},{continente}\n")

    with open('paises.csv','r') as archivo:
        contenido = archivo.read()
        print(contenido)

def comprobar_vacio(entrada):
    vacio = False
    if entrada == "":
        vacio = True
    return vacio


#Generacion del menu

opcion = ""

while opcion != "7":
    print("Eliga el numero correspondiente a la opcion requerida: ")
    print("1. Agregar pais y sus datos.")
    print("2. Actualizar datos de Poblacion y Superficie de un pais.")
    print("3. Buscar pais por nombre.")
    print("4. Buscar paises por filtrado.")
    print("5. Ordenar paises.")
    print("6. Mostrar estadisticas.")
    opcion = input().strip()

#desarrollo de las opciones
    match opcion:
        case "1":
            while True:
                pais = input("¿Que pais desea agregar? ").lower().strip()
                if comprobar_existencia(pais) == True or comprobar_vacio(pais) == True:
                    print("Error. Intente de nuevo.")    
                else:
                    break
                    
            while True:
                poblacion = input(f"Ingrese la poblacion de {pais}: ").strip()
                if poblacion.isdigit() and poblacion != "":
                    break
                else:
                    print("Error. Intente de nuevo.")

            while True:
                superficie = input(f"Ingrese la superficie de {pais}: ").strip()
                if superficie.isdigit() and superficie != "":
                    break
                else:
                    print("Error.Intente de nuevo.")
            
            while True:
                continente = input(f"¿A que continente pertenece {pais}? ").lower().strip()
                if comprobar_vacio(continente) == True:
                    pass
                else:
                    break

            actualizar_archivo(pais,poblacion,superficie,continente)
            print("El archivo se ha actualizado con exito.")

        case "2":
            while True: 
                pais = input("¿Que pais desea actualizar? ").lower().strip()
                if comprobar_existencia(pais) == False or comprobar_vacio(pais) == True:
                    pass
                else: 
                    break
            
            while True:
                nueva_poblacion = input("Ingrese la nueva poblacion: ").strip()
                print(nueva_poblacion.isdigit())
                if nueva_poblacion.isdigit():
                    break
                else:
                    print("La entrada debe ser un numero.")

            while True:
                nueva_superficie = input("Ingrese la nueva superficie: ").strip()
                if nueva_superficie.isdigit():
                    break
                else:
                    print("La entrada debe ser un numero.")

            with open('paises.csv','r') as archivo:
                lineas = archivo.readlines()
                for elemento in lineas:
                    nombre,poblacion,superficie,continente = elemento.strip().split(',')
                    if nombre == pais:
                        continente = continente

            actualizar_archivo(pais,nueva_poblacion,nueva_superficie,continente)      

        case "3":
            pais = input("Buscar: ").lower().strip()
            with open('paises.csv','r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas[1:]:
                    nombres,poblaciones,superficies,continentes = linea.strip().split(',')
                    
                    if pais.lower() in nombres.lower():
                        print(linea)

        case "4":
            while True:
                filtro = input("Eliga como desea filtrar el archivo:\n1.Por continente.\n2.Por rango de poblacion.\n3.Por rango de superficie.\n").strip()
                filtro_existe = False
                
                if filtro == "1":
                    continente = input("Ingrese el continente: ").lower().strip()
                    with open('paises.csv','r') as archivo:
                        lineas = archivo.readlines()
                        for linea in lineas:
                            nombres,poblaciones,superficies,continentes = linea.strip().split(',')
                            if continentes == continente:
                                filtro_existe = True
                                print(linea)
                            if filtro_existe == False:
                                print("No existen paises que pertenezcan a ese continente en el archivo.")
                    break
                
                elif filtro == "2":
                    minimo = input("Introduzca el numero minimo de poblacion: ")
                    maximo = input("Introduzca el numero maximo de poblacion: ")
                    with open('paises.csv','r') as archivo:
                        lineas = archivo.readlines()
                        for linea in lineas:
                            nombres,poblaciones,superficies,continentes = linea.strip().split(',')

                            if poblaciones > minimo and poblaciones < maximo:
                                filtro_existe = True
                                print(linea)
                            if filtro_existe == False: 
                                print("No existen paises en el archivo con esos criterios.")
                    break

                elif filtro == "3":
                    minimo = input("Introduzca el numero minimo de la superficie: ")
                    maximo = input("Introduzca el numero maximo de la superficie: ")
                    with open('paises.csv','r') as archivo:
                        lineas = archivo.readlines()
                        for linea in lineas:
                            nombres,poblaciones,superficies,continentes = linea.strip().split(',')

                            if superficies > minimo and superficies < maximo:
                                filtro_existe = True
                                print(linea)
                            if filtro_existe == False: 
                                print("No existen paises en el archivo con esos criterios.")
                    break

                else:
                    print("Error. Intente de nuevo.")
                
        case "5":
            print("opcion 5")
        case "6":
            print("opcion 6")
        case _:
            print("error")