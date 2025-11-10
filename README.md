# Trabajo-Practico-Integrador
Trabajo Practico Integrador de Programacion 1 - Universidad Tecnologica Nacional 

Integrantes: 
Tiffany Valle - Comision 11
Ferrario Ines - Comision 4

Profesores: 
Cinthia Rigoni - Comisión 4
Luciano Chiroli - Comisión 11


Sistema de gestión de información sobre países:

En este trabajo practico desarrollamos un sistema de gestión de información sobre países almacenados en un archivo CSV (países.csv) con una estructura principal en formato menú que permite al usuario agregar paises, actualizar datos de población y superficie, buscar, filtrar por continente, rango de población o de superficie, ordenarlos por nombre, población o superficie, y ver estadísticas. Los datos que se almacenan por país son nombre, población, superficie y continente.
Todo el menú está trabajado con módulos y cada opción del menú llama a una función distinta para realizar la acción deseada. También se utilizan las funciones para validar las entradas del usuario, lo cual asegura que el programa funcione correctamente y permita volver a ingresar una entrada no válida cuando no se ingresan datos, se ingresan números en donde solo van letras o letras donde solo van números. Además se utiliza la normalización de texto para evitar errores por mayúsculas o tildes.

Instrucciones de uso:

Al ejecutar el programa va a aparecer el menú principal que permite ingresar números del 1-7 dependiendo de la acción que se desee realizar, seleccionar uno. Tener en cuenta que si se ingresa un número diferente u otro carácter el programa lo va a tomar como una entrada inválida y volverá a solicitar una entrada.
Según la opción seleccionada el programa solicitará información (nombre del país, opciones de filtrado, etc) para realizar la acción.

Ejemplos de entrada y salida:

OPCIÓN 1:
  Entradas:
Ingrese una opcion: <1>
Ingrese el país que desea agregar: <Argentina>
Ingrese la población: <46000000>
Ingrese la superficie: <2780000>
Ingrese el continente: <America>

  Salidas:
Los datos fueron cargados correctamente.

OPCIÓN 2:
  Entradas:
Ingrese una opcion: <2>
Ingrese el país que desea actualizar: <Argentina> 
Ingrese la nueva poblacion: <47500000>
Ingrese la nueva superficie: <2500000>

  Salida:
Datos actualizados correctamente.

OPCION 3:
  Entradas:
Ingrese una opcion: <3>
Ingrese el pais a buscar: <Argentina>

  Salida:
Resultados de busqueda:
argentina - Pob: 47500000 - Sup: 2500000 - Cont: america


Participación de los integrantes: 
Se realizó una división de trabajo equitativo en el desarrollo de las 6 opciones principales, donde cada una realizó 3 de estas. Al juntarlo se probaron las validaciones y se hicieron sugerencias de cambios para obtener un código más fluido y coherente.

Links:
Repositorio GitHub: https://github.com/alexfft7/Trabajo-Practico-Integrador
Video explicativo: https://youtu.be/mH2vllWa3a0 
