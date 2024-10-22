import seaborn as sns # instalar con pip3
from random import randint
from PIL import Image, ImageColor # instalar con pip3
n = 22 #modificar dato
fondo = (0, 70, 255) # azul
zona = Image.new('RGB', (n, n), color = fondo)
celda = zona.load()
k = 22 #modificar semillas
color = sns.color_palette("Set3", k).as_hex() #modificar colores de paletas
for semilla in range(k):
    while True:
        columna = randint(0, n - 1)
        fila = randint(0, n - 1)
        if celda[columna, fila] == fondo:
            celda[columna, fila] =  ImageColor.getrgb(color[semilla])
            break
visual = zona.resize((10 * n,  10 * n))
visual.show()
visual.save("p4p.png")