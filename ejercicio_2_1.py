import json

menu = """Bienvenido
Escoge una de las opciones
1 - Redactar carta
0 - Salir
"""
opcion = ""

while opcion != "0":
    print(menu)
    opcion = input("Ingrese una opción: ")
    
    # Crear carta
    if opcion == "1":
        fecha = input("Ingresa la fecha en que se redacta la carta: ")
        ciudad = input("Ingresa la ciudad en que se redacta la carta: ")
        saludo = input("Ingresa el saludo que tendrá la carta: ")
        motivo = input("Ingresa el el motivo de la carta: ")

        archivo = open("db/carta.json", "+r")
        archivo_l=json.load(archivo)

        carta = {
            "encabezado":{
                "fecha": fecha,
                "ciudad": ciudad,
            },
            "cuerpo":{
                "saludo": saludo,
                "motivo": motivo,
            }
        }

        archivo_l["cartas"].append(carta)


        archivo.seek(0)
        json.dump(archivo_l,archivo, indent=4)
        archivo.truncate()
        print("Se agregó exitosamente")


