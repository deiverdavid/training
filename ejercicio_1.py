# Crear un diccionario(concecionario) que almacene los modelos mazda - chevrolet - nissan, 2 por marca
# concesonario: modelo, año, color, puertas
concecionario = {
    "mazda": [{
        "modelo": "rx7",
        "año": 2022,
        "color": "negro",
        "puertas": 2,
    },
    {
        "modelo": "rx8",
        "año": 2022,
        "color": "rojo",
        "puertas": 2,
    }],

    "chevrolet": [{
        "modelo": "camaro",
        "año": 2022,
        "color": "amarillo",
        "puertas": 4,
    },
    {
        "modelo": "silverado",
        "año": 2022,
        "color": "azul",
        "puertas": 4,
    }],

    "nissan": [{
        "modelo": "prado",
        "año": 2022,
        "color": "blanco",
        "puertas": 4,
    },
    {
        "modelo": "gtr",
        "año": 2022,
        "color": "verde",
        "puertas": 4,
    }]
}

print(concecionario["chevrolet"][0]["color"])
    
