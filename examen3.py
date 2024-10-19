import random
def examen3():
    numero_random = random.randint(1, 100)
    intentos = 0
    print("Intenta adivinar el numero que elegi en el menor numero de intentos posibles")
    while True:
        intento = input("Ingresa un numero del 1 al 100: ")
        try:
            intento = int(intento)
            intentos += 1
        except ValueError:
            print("Ingresa un numero del 1 al 100.")
            continue
        if intento < numero_random:
            print("Tu numero es menor.")
        elif intento > numero_random:
            print("tu numero es mayor.")
        else:
            print(f"Adivinaste el numero {numero_random} en {intentos} intentos.")
            break
examen3()