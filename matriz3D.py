import random

# Definir dimensiones de la matriz 3D
dimension_ciudades = 3
dimension_dias = 7
dimension_semanas = 4

# Inicializar la matriz 3D para almacenar temperaturas
matriz_temperaturas = [[[0] * dimension_semanas for _ in range(dimension_dias)] for _ in range(dimension_ciudades)]

# Llenar la matriz con datos de temperaturas (números aleatorios en este ejemplo)
for ciudad in range(dimension_ciudades):
    for dia in range(dimension_dias):
        for semana in range(dimension_semanas):
            matriz_temperaturas[ciudad][dia][semana] = random.randint(20, 35)

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in range(dimension_ciudades):
    for semana in range(dimension_semanas):
        suma_temperaturas = sum(matriz_temperaturas[ciudad][dia][semana] for dia in range(dimension_dias))
        promedio_temperaturas = suma_temperaturas / dimension_dias
        print(f"El promedio de temperaturas en la ciudad {ciudad + 1} para la semana {semana + 1} es: {promedio_temperaturas:.2f}°C")

# Calcular el promedio de temperaturas para Tena y cada semana
ciudad_tena = 0  # Tena es la primera ciudad en la matriz
for semana in range(dimension_semanas):
    suma_temperaturas_tena = sum(matriz_temperaturas[ciudad_tena][dia][semana] for dia in range(dimension_dias))
    promedio_temperaturas_tena = suma_temperaturas_tena / dimension_dias
    print(f"El promedio de temperaturas en Tena para la semana {semana + 1} es: {promedio_temperaturas_tena:.2f}°C")

