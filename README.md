# Simulador de Red Social
### Proyecto final de Estructuras de Datos y Algoritmos II

Esta es simulación de red social utiliza las estructuras de datos y algoritmos que se crearon en clase a lo largo del semestre.

Las estructuras utilizadas son:
* Hash Map
* Hash Set
* Priority Queue (a base de heaps)
* Linked List
* Queue \
El codigo de todas ellas esta en la carpeta data_structures y es necesario para el funcionamiento del programa.

En cuanto a los algoritmos:
* Las bases de datos fueron generadas en archivos txt de manera similar a algunas creadas en clase. Estas son escritas al generarlas con `database_generator.txt`. Esta carpeta ya incluye bases de datos generadas, pero se incluye el generador para mostrar los algoritmos y en caso de quere alterar los datos. 
* El programa usa busqueda secuencial en cadenas, asi como el algoritmo de busqueda KMP. Ambos se utilizan en `classes.py`.

## Para usar el programa
Este proyecto se abre a partir del archivo `gui.py`. La interfaz está hecha con TKinter, que forma parte de las librerias estándar de Python, por lo que no es necesaria la instalación de otros paquetes a menos que, por alguna razón, TKinter no funcionara. 

Al iniciar el programa, se solicitará un inicio de sesión. Se puede crear un nuevo usuario, dando click en el botón de Sign up, o ingresar los datos de un usuario ya existente. En el archivo `users_database.txt` cada linea comienza con el username del usuario y termina con la contraseña del mismo. Si no se alteran las bases de datos que están actualmente en el proyecto, un usuario de prueba puede ser:

Username: JosephH462 \
Password: cj6m79vxj7ka 

Recomiendo usar algun usuario existente, pues ya está cargado con publicaciones propias, seguidores, seguidos, likes y comentarios, por lo que se muestra mas claramente el funcionamiento del proyecto.
