segundos=input ("ingrese los segundos que desea convertir a horas con minutos y segundos")
segundos= int(segundos)
horas=segundos//3600
sobrantes1=segundos%3600
minutos=sobrantes1//60
sobrantes2=sobrantes1%60
print("Horas")
print(horas)
print("Minutos" )
print(minutos)
print("Segundos")
print(sobrantes2)
