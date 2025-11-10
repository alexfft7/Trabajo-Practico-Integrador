# Antes de cargar datos, el programa pregunta si se debe crear un archivo CSV nuevo.
# Así, evita borrar información previa del usuario sin aviso. Si no existe el archivo, se crea automáticamente.

#  Se importa la función para normalizar texto(Con o sin tildes, o en mayúsculas o minúsculas).

import unicodedata


# Normalización de texto: convierte a minúsculas y elimina tildes.
def normalizar_texto(cadena):
    cadena = cadena.lower()
    cadena = ''.join(
        c for c in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(c) != 'Mn'
    )
    return cadena.strip()


# Crear archivo CSV según decisión del usuario.
def crear_archivo():
    print("¿Desea crear un archivo CSV nuevo y borrar los datos existentes?")
    print("Escriba 'si' para crear uno nuevo o 'no' para mantener los datos.")
    
    while True:
        decision = input("Ingrese su opción (si/no): ").strip().lower()
        if decision == "si":
            with open('paises.csv', 'w') as archivo:
                archivo.write('nombre,poblacion,superficie,continente\n')
            print("Archivo creado correctamente.\n")
            return
        elif decision == "no":
            # Si no existe, se crea igual pero vacío.
            try_open = open('paises.csv', 'a')
            try_open.close()
            print("Se mantendrán los datos existentes.\n")
            return
        else:
            print("Opción inválida. Debe escribir 'si' o 'no'.")


# Cargar países desde el CSV a una lista de diccionarios.
def cargar_paises():
    paises = []

    with open('paises.csv', 'r') as archivo:
        lineas = archivo.readlines()

    # Saltar encabezado.
    for linea in lineas[1:]:
        partes = linea.strip().split(',')
        if len(partes) == 4:
            nombre, poblacion, superficie, continente = partes
            paises.append({
                "nombre": nombre,
                "poblacion": int(poblacion),
                "superficie": int(superficie),
                "continente": continente
            })

    return paises


# Guardar lista de países nuevamente en el CSV.
def guardar_paises(paises):
    with open('paises.csv', 'w') as archivo:
        archivo.write('nombre,poblacion,superficie,continente\n')

        for pais in paises:
            archivo.write(
                f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
            )


# Comprobar existencia de país normalizado.
def comprobar_existencia(paises, pais_normalizado):
    for pais in paises:
        if normalizar_texto(pais["nombre"]) == pais_normalizado:
            return True
    return False


# Validar que una entrada contenga solo letras.
def validar_solo_letras(texto):
    if texto == "":
        return False

    for char in texto:
        if not (char.isalpha() or char == " "):
            return False

    return True


# Opción 1: agregar países.
def agregar_pais(paises):

    # Ingreso del nombre del país.
    while True:
        pais = input("Ingrese el país que desea agregar: ").strip()

        if not validar_solo_letras(pais):
            print("Error: el nombre del país debe contener solo letras.")
            continue

        pais_normalizado = normalizar_texto(pais)

        if comprobar_existencia(paises, pais_normalizado):
            print("Ese país ya existe en el archivo.")
            continue

        break

    # Ingreso de población.
    while True:
        poblacion = input("Ingrese la población: ").strip()
        if poblacion.isdigit():
            poblacion = int(poblacion)
            break
        print("Error: ingrese solo números.")

    # Ingreso de superficie.
    while True:
        superficie = input("Ingrese la superficie: ").strip()
        if superficie.isdigit():
            superficie = int(superficie)
            break
        print("Error: ingrese solo números.")

    # Ingreso de continente.
    while True:
        continente = input("Ingrese el continente: ").strip()
        if validar_solo_letras(continente):
            break
        print("Error: el continente debe contener solo letras.")

    # Guardar datos normalizados.
    paises.append({
        "nombre": normalizar_texto(pais),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": normalizar_texto(continente)
    })

    guardar_paises(paises)
    print("Los datos fueron cargados correctamente.\n")


# Opción 2: actualizar población y superficie de un país.
def actualizar_pais(paises):

    # Ingreso del país a actualizar.
    while True:
        pais = input("Ingrese el país que desea actualizar: ").strip()

        if not validar_solo_letras(pais):
            print("Error: ingrese solo letras.")
            continue

        pais_normalizado = normalizar_texto(pais)

        if not comprobar_existencia(paises, pais_normalizado):
            print("Ese país no existe.")
            continue

        break

    # Obtener país.
    for p in paises:
        if normalizar_texto(p["nombre"]) == pais_normalizado:
            pais_obj = p
            break

    # Población nueva.
    while True:
        nueva_poblacion = input("Ingrese la nueva población: ").strip()
        if nueva_poblacion.isdigit():
            nueva_poblacion = int(nueva_poblacion)
            if nueva_poblacion == pais_obj["poblacion"]:
                print("Debe ingresar un valor distinto al actual.")
            else:
                break
        else:
            print("Error: ingrese solo números.")

    # Superficie nueva.
    while True:
        nueva_superficie = input("Ingrese la nueva superficie: ").strip()
        if nueva_superficie.isdigit():
            nueva_superficie = int(nueva_superficie)
            if nueva_superficie == pais_obj["superficie"]:
                print("Debe ingresar un valor distinto al actual.")
            else:
                break
        else:
            print("Error: ingrese solo números.")

    pais_obj["poblacion"] = nueva_poblacion
    pais_obj["superficie"] = nueva_superficie

    guardar_paises(paises)
    print("Datos actualizados correctamente.\n")


# Opción 3: buscar país por nombre.
def buscar_pais(paises):

    while True:
        termino = input("Ingrese el país a buscar: ").strip()
        if termino != "":
            break
        print("Debe ingresar un texto válido.")

    termino_normalizado = normalizar_texto(termino)

    print("\nResultados de búsqueda:")
    encontrado = False

    for pais in paises:
        if termino_normalizado in normalizar_texto(pais["nombre"]):
            print(f"{pais['nombre']} - Pob: {pais['poblacion']} - Sup: {pais['superficie']} - Cont: {pais['continente']}")
            encontrado = True

    if not encontrado:
        print("No se encontraron coincidencias.")

    print()


# Opción 4: filtrar países.
def filtrar_paises(paises):

    while True:
        print("\nOpciones de filtrado:")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")

        filtro = input("Elija una opción: ").strip()

        if filtro in ("1", "2", "3"):
            break
        print("Opción inválida. Debe elegir 1, 2 o 3.")

    if filtro == "1":
        cont = input("Ingrese el continente: ").strip()
        cont_norm = normalizar_texto(cont)

        print("\nPaíses encontrados:")
        existe = False
        for pais in paises:
            if normalizar_texto(pais["continente"]) == cont_norm:
                print(pais)
                existe = True
        if not existe:
            print("No hay países que coincidan.")

    elif filtro == "2":
        while True:
            minimo = input("Población mínima: ").strip()
            maximo = input("Población máxima: ").strip()
            if minimo.isdigit() and maximo.isdigit():
                minimo = int(minimo)
                maximo = int(maximo)
                break
            print("Error: ingrese solo números.")

        print("\nPaíses encontrados:")
        existe = False
        for pais in paises:
            if minimo <= pais["poblacion"] <= maximo:
                print(pais)
                existe = True
        if not existe:
            print("No hay coincidencias.")

    elif filtro == "3":
        while True:
            minimo = input("Superficie mínima: ").strip()
            maximo = input("Superficie máxima: ").strip()
            if minimo.isdigit() and maximo.isdigit():
                minimo = int(minimo)
                maximo = int(maximo)
                break
            print("Error: ingrese solo números.")

        print("\nPaíses encontrados:")
        existe = False
        for pais in paises:
            if minimo <= pais["superficie"] <= maximo:
                print(pais)
                existe = True
        if not existe:
            print("No hay coincidencias.")

    print()


# Opción 5: ordenar países.
def ordenar_paises(paises):

    while True:
        print("\nOpciones de ordenamiento:")
        print("1. Por nombre")
        print("2. Por población")
        print("3. Por superficie")

        opcion = input("Elija una opción: ").strip()
        if opcion in ("1", "2", "3"):
            break
        print("Opción inválida. Debe elegir 1, 2 o 3.")

    if opcion == "1":
        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if normalizar_texto(paises[j]["nombre"]) < normalizar_texto(paises[i]["nombre"]):
                    paises[i], paises[j] = paises[j], paises[i]

    elif opcion == "2":
        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[j]["poblacion"] < paises[i]["poblacion"]:
                    paises[i], paises[j] = paises[j], paises[i]

    elif opcion == "3":
        for i in range(len(paises)):
            for j in range(i + 1, len(paises)):
                if paises[j]["superficie"] < paises[i]["superficie"]:
                    paises[i], paises[j] = paises[j], paises[i]

    print("\nListado ordenado:")
    for pais in paises:
        print(pais)
    print()


# Opción 6: estadísticas.
def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay datos cargados.\n")
        return

    print("\nESTADÍSTICAS GENERALES\n")
    total = len(paises)
    print(f"Cantidad total de países: {total}")

    mayor_pob = paises[0]
    menor_pob = paises[0]
    mayor_sup = paises[0]
    menor_sup = paises[0]

    suma_pob = 0
    suma_sup = 0

    for pais in paises:
        suma_pob += pais["poblacion"]
        suma_sup += pais["superficie"]

        if pais["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = pais
        if pais["poblacion"] < menor_pob["poblacion"]:
            menor_pob = pais
        if pais["superficie"] > mayor_sup["superficie"]:
            mayor_sup = pais
        if pais["superficie"] < menor_sup["superficie"]:
            menor_sup = pais

    print(f"País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']})")
    print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']})")
    print(f"País con mayor superficie: {mayor_sup['nombre']} ({mayor_sup['superficie']})")
    print(f"País con menor superficie: {menor_sup['nombre']} ({menor_sup['superficie']})")
    print(f"Promedio de población: {suma_pob / total:.2f}")
    print(f"Promedio de superficie: {suma_sup / total:.2f}")

    continentes = {}
    for pais in paises:
        cont = pais["continente"]
        if cont not in continentes:
            continentes[cont] = 1
        else:
            continentes[cont] += 1

    print("\nPaíses por continente:")
    for cont, cant in continentes.items():
        print(f"{cont}: {cant}")

    print()


# Función principal: menú.
def main():
    crear_archivo()
    paises = cargar_paises()

    opcion = ""

    while opcion != "7":
        print("MENÚ PRINCIPAL")
        print("1. Agregar país")
        print("2. Actualizar datos")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            print("Programa finalizado.")
        else:
            print("Opción inválida.\n")


# Ejecución del programa.
main()
