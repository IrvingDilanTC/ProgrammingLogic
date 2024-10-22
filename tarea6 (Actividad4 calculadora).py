def calculadora():
    print("calculadora básica")
    num1 = int(input("ingresa el primer número: "))
    num2 = int(input("ingresa el segundo número: "))
    print("\nSelecciona la operación:")
    print("1. suma")
    print("2. resta")
    print("3. multiplicación")
    print("4. división")
    
    if Option == '1':
        print(f"\nEL resultado de sumar {num1} + {num2} es: {num1 + num2}")
    elif Option == '2':
        print(f"\nEl resultado de restar {num1} - {num2} es: {num1 - num2}")
    elif Option == '3':
        print(f"\nEl resultado de multiplicar {num1} * {num2} es: {num1 * num2}")
    elif Option == '4':
        if num2 != 0:
            print(f"\nEl resultado de dividir {num1} / {num2} es: {num1 / num2}")    
        else:
        print("\nError: no se puede dividir entre 0") 
    else:
         print:("\nOpción inválida. por favor elige una opción correcta.")    
                     
             
