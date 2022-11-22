# Crear listado de musicos ingresados por la terminal 
# que permita crearlos y eliminarlos 1 - crear 2 - eliminar 0 - salir

musicos = []

bienvenida = """ Hola, bienvenido a tu programa de música
Escoge una de las opciones

1 - Registrar un músico 
2 - Eliminar un músico 
0 - Salir 
"""

opcion = ""

while opcion != 0:
    print(bienvenida)
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del cantante: ")
        genero = input("Ingrese el nombre del genero: ")
        edad = int(input("Ingrese el nombre del edad: "))
        musico = {
            "nombre": nombre,
            "genero": genero,
            "edad": edad,
        }

        musicos.append(musico)
        print(f"Se creo el músico {musico['nombre']}")

    elif opcion == 2:
        posicion = 1
        for i in musicos:
            print("{} - {} - {} - {}".format(posicion, i["nombre"], i["genero"], i["edad"]))
            posicion += 1

        eliminar = int(input("Ingrese el id del cantante: ")) - 1

        musicos.pop(eliminar)

 
