import json
# empleados = [
#     {
#         "Nombre": "Pedro",
#         "Apellido": "Suarez",
#         "Cargo": "ABAP",
#         "Activo": "True",
#     },
#     {
#         "Nombre": "Carlos",
#         "Apellido": "Lopez",
#         "Cargo": "ABAP",
#         "Activo": "True",
#     },
#     {
#         "Nombre": "Camilo",
#         "Apellido": "Martinez",
#         "Cargo": "BASIS",
#         "Activo": "True",
#     },
#     {
#          "Nombre": "Edgar",
#         "Apellido": "Santos",
#         "Cargo": "SOPORTE",
#         "Activo": "False",
#     }
# ]

# empleados_act = [i for i in empleados if i["Cargo"] == "ABAP" and i["Nombre"] == "Carlos"]
# for i in empleados_act:
#     print(i)

archivo = open("db/db.json", "+r")
archivo_f = json.load(archivo)
archivo_i = json.dumps(archivo_f, indent=4)
print(archivo_i)