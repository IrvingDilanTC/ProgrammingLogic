   #Contador de Palabras
print("Proyecto PIA, Irving Dilan Tovar Coronado te da la bienvenida al contador de palabras")

#Descripción del proyecto
print("Escribirás varias palabras y determinaré su cantidad.")

oración = input("Escriba varias palabras: ")
palabras = oración.split()
count = 0

for i in palabras:
    count+=1
print(count)