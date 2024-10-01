producto1="pepperoni"
costo1=99#int
iva=0.14#float
dollar=20#int
total1=costo1+(costo1*iva)
dollar1=(costo1/dollar)
producto2="hawaiana"
costo2=119
total2=costo2+(costo2*iva)
dollar2=(costo2/dollar)
producto3="mexicana"
costo3=129#int
total3=(costo3*iva)
dollar3=(costo3/dollar)
producto4="recargada"
costo4=139#int
total4=costo4+(costo4*iva)
dollar4=(costo4/dollar)
producto5="boneless"
costo5=119
total5=costo5+(costo5*iva)
dollar5=(costo5/dollar)
producto6="alitas"
costo6=119
total6=costo6+(costo6*iva)
dollar6=(costo6/dollar)
print("{:^20}   {:<20}  {:<20}  {:<20}".format("Producto",  "Valor sin IVA",    "Total de compra", "Precio en Dolares"))
print("{:20}    {:<20}  {:<20}  {:<20,.2f}".format(producto1,costo1,total1,dollar1))
print("{:<20}   {:<20}  {:<20}  {:<20,.2f}".format(producto2,costo2,total2,dollar2)) 
print("{:<20}   {:<20}  {:<20}  {:<20,.2f}".format(producto3,costo3,total3,dollar3))
print("{:<20}   {:<20}  {:<20}  {:<20,.2f}".format(producto4,costo4,total4,dollar4))
print("{:<20}   {:<20}  {:<20}  {:<20,.2f}".format(producto5,costo5,total5,dollar5))
print("{:<20}   {:<20}  {:<20}  {:<20,.2f}".format(producto6,costo6,total6,dollar6)) #str
 