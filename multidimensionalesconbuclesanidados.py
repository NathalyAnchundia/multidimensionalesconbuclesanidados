# Crear una matriz 3D para almacenar datos de Temperatura
# Primera dimensión: ciudades (6 ciudades)
# Segunda dimensión: dias de la Semanas (7 días)
# Tercera dimensión:  semana (3 semanas)
temperaturas = [
    [   # Ciudad 1 (Quito)
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ]
    ],
    [   # Ciudad 2 (Guayaquil)
        [   # Semana 1
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 95},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 15}
        ]
    ],
    [   # Ciudad 3 (Esmeraldas)
        [   # Semana 1
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 7},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 8},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 10},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 6},
            {"day": "Martes", "temp": 8},
            {"day": "Miércoles", "temp": 7},
            {"day": "Jueves", "temp": 75},
            {"day": "Viernes", "temp": 9},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 11}
        ]
    ]
]

# Nombres de las ciudades
nombres_ciudades = ["Quito", "Guayaquil", "Esmeraldas"]

# Iterando sobre las ciudades, semanas y días de la semana para calcular el promedio de temperaturas
for ciudad_index, ciudad in enumerate(temperaturas, start=1):
    nombre_ciudad = nombres_ciudades[ciudad_index - 1]
    print(f'CIUDAD No. {ciudad_index}: {nombre_ciudad}')
    for semana_index, semana in enumerate(ciudad, start=1):
        print(f'SEMANA No. {semana_index}')
        # Lista para almacenar las temperaturas diarias de la semana
        temperatura_semana = [dia["temp"] for dia in semana]
        # Calculando el promedio de temperaturas para la semana actual
        promedio_semana = sum(temperatura_semana) / len(temperatura_semana)
        print(f'El promedio de la semana es: {promedio_semana:.2f}')
        # Mostrar las temperaturas en grados
        for dia in semana:
            print(f"La temperatura para el {dia['day']} es: {dia['temp']}°")