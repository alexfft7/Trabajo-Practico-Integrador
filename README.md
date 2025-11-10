# Trabajo-Practico-Integrador
Sistema de gestión de información sobre países:

Este programa consiste en un sistema de gestión de información sobre países almacenados en un archivo CSV (países.csv) con una estructura principal en formato menú que permite al usuario agregar paises, actualizar datos de población y superficie, buscar, filtrar por continente, rango de población o de superficie, ordenarlos por nombre, población o superficie, y ver estadísticas. Los datos que se almacenan por país son nombre, población, superficie y continente.
Todo el menú está trabajado con módulos y cada opción del menú llama a una función distinta para realizar la acción deseada. También se utilizan las funciones para validar las entradas del usuario, lo cual asegura que el programa funcione correctamente y permita volver a ingresar una entrada no válida cuando no se ingresan datos, se ingresan números en donde solo van letras o letras donde solo van números. Además se utiliza la normalización de texto para evitar errores por mayúsculas o tildes.

Instrucciones de uso:

Al ejecutar el programa va a aparecer el menú principal que permite ingresar números del 1-7 dependiendo de la acción que se desee realizar, seleccionar uno. Tener en cuenta que si se ingresa un número diferente u otro carácter el programa lo va a tomar como una entrada inválida y volverá a solicitar una entrada.
Según la opción seleccionada el programa solicitará información (nombre del país, opciones de filtrado, etc) para realizar la acción.

Ejemplos de entrada y salida:

OPCIÓN 1:

Ingrese el país que desea agregar: <Argentina>
Ingrese la población: <46000000>
Ingrese la superficie: <2780000>
Ingrese el continente: <America>

Salida esperada:
Los datos fueron cargados correctamente.

Salida si en lugar de <46000000> se hubiera ingresado <Cuarenta y seis millones>:
Error: ingrese solo números.

El archivo ‘paises.csv’ al finalizar la opción 1 se veria asi:
nombre,poblacion,superficie,continente
argentina,46000000,2780000,america

OPCIÓN 2:
Ingrese el país que desea actualizar: <Brasil> 

Salida esperada: 
Ese país no existe.
Participación de los integrantes: 
Se realizó una división de trabajo equitativo en el desarrollo de las 6 opciones principales, donde cada una realizó 3 de estas. Al juntarlo se probaron las validaciones y se hicieron sugerencias de cambios para obtener un código más fluido y coherente.
