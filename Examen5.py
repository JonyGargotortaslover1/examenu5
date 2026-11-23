estudiantes = int(input("Cuantos estudiantes tiene el grupo: "))
materias = int(input("Cuantas materias tiene el grupo: "))


calificaciones = []

for i in range(estudiantes):
    fila = []
    print("\nEstudiante", i + 1)

    for j in range(materias):
        nota = float(input("Calificacion de la materia " + str(j + 1) + ": "))

        while nota < 0 or nota > 100:
            print("Error: la calificacion debe ser de 0 a 100")
            nota = float(input("Ingresa nuevamente la calificacion: "))

        fila.append(nota)

    calificaciones.append(fila)

print("\n===== MATRIZ DE CALIFICACIONES =====")

for fila in calificaciones:
    print(fila)

print("\n===== PROMEDIO POR ESTUDIANTE =====")

for i in range(estudiantes):
    promedio = sum(calificaciones[i]) / materias
    print("Estudiante", i + 1, ":", round(promedio, 2))

print("\n===== PROMEDIO POR MATERIA =====")

for j in range(materias):
    suma = 0

    for i in range(estudiantes):
        suma += calificaciones[i][j]

    promedio = suma / estudiantes
    print("Materia", j + 1, ":", round(promedio, 2))

todas = []

for fila in calificaciones:
    for nota in fila:
        todas.append(nota)

mayor = max(todas)
menor = min(todas)

print("\n===== RESULTADOS GENERALES =====")
print("Calificacion mas alta:", mayor)
print("Calificacion mas baja:", menor)
