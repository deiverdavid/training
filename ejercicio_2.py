empleados = [
    {
        "Nombre": "Pedro",
        "Apellido": "Suarez",
        "Cargo": "ABAP",
        "Activo": "True",
    },
    {
        "Nombre": "Carlos",
        "Apellido": "Lopez",
        "Cargo": "ABAP",
        "Activo": "True",
    },
    {
        "Nombre": "Camilo",
        "Apellido": "Martinez",
        "Cargo": "BASIS",
        "Activo": "True",
    },
    {
         "Nombre": "Edgar",
        "Apellido": "Santos",
        "Cargo": "SOPORTE",
        "Activo": "False",
    },
    {
        "Nombre": "Pedro",
        "Apellido": "Suarez",
        "Cargo": "ABAP",
        "Activo": "True",
    },
    {
        "Nombre": "Carlos",
        "Apellido": "Lopez",
        "Cargo": "ABAP",
        "Activo": "True",
    },
    {
        "Nombre": "Camilo",
        "Apellido": "Martinez",
        "Cargo": "BASIS",
        "Activo": "True",
    },
    {
         "Nombre": "Edgar",
        "Apellido": "Santos",
        "Cargo": "SOPORTE",
        "Activo": "False",
    },
    {
        "Nombre": "Pedro",
        "Apellido": "Suarez",
        "Cargo": "ABAP",
        "Activo": "True",
    },
    {
        "Nombre": "Carlos",
        "Apellido": "Lopez",
        "Cargo": "ABAP",
        "Activo": "True",
    },
    {
        "Nombre": "Camilo",
        "Apellido": "Martinez",
        "Cargo": "BASIS",
        "Activo": "True",
    },
    {
        "Nombre": "Edgar",
        "Apellido": "Santos",
        "Cargo": "SOPORTE",
        "Activo": "False",
    }
]
# Hacer un filtro por la entrada del usuario en base a los datos de los empleados

bienvenida = """
------------- Buenos dias ---------
Escoge una de las opciones de este menú
1 - Filtrar
0 - Salir
"""

menu = """
1 - Nombre
2 - Apellido
3 - Cargo
4 - Activo
0 - Salir
"""

opcion = ""

while opcion != 0:
    print(bienvenida)
    opcion = int(input("Ingrese la opción, por favor: "))

    if opcion == 1:
        opcion_fil = ""
        while opcion_fil != "0":
            print(menu)
            opcion_fil = input("Ingrese la opción: ")
            if opcion_fil == "1":
                clave = "Nombre"
                filtro = input("Ingrese el nombre del empleado: ")

            elif opcion_fil == "2":
                clave = "Apellido"
                filtro = input("Ingrese el apellido del empleado: ")    

            elif opcion_fil == "3":
                clave = "Cargo"
                filtro = input("Ingrese el cargo del empleado: ")    

            elif opcion_fil == "4":
                clave = "Activo"
                filtro = input("Ingrese la actividad del empleado: ")    

            filtro_list = [i for i in empleados if i[clave] == filtro]
            for i in filtro_list:
                print(i)
        

