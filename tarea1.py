producto1="pepperoni"
costo1=99#int
iva=0.14#float
total1=costo1+(costo1*iva)
producto2="hawaiana"
costo2=119.0
total2=costo2+(costo2*iva)
producto3="mexicana"
costo3=129.0
total3=costo3+(costo3*iva)
producto4="recargada"
costo4=139.0
total4=costo4+(costo4*iva)
producto5="boneless"
costo5=119.0
total5=costo5+(costo5*iva)
producto6="alitas"
costo6=119.0
total6=costo6+(costo6*iva)
producto7="papas"
costo7=59.0
total7=costo7+(costo7*iva)
producto8="munchers"
costo8=69.0
total8=costo8+(costo8*iva)
producto9="espagueti"
costo9=39.0
total9=costo9+(costo9*iva)
producto10="refresco"
costo10=19.0
total10=costo10+(costo10*iva)
print("{:^20}   {:<20}  {:<20}".format("Producto",  "Valor sin IVA",    "Total de compra"))
print("{:20}    {:<20}  {:<20,.2f}".format(producto1,costo1,total1))
print("{:<20}   {:<20}  {:<20,.2f}".format(producto2,costo2,total2)) 
print("{:<20}   {:<20}  {:<20,.2f}".format(producto3,costo3,total3))
print("{:<20}   {:<20}  {:<20,.2f}".format(producto4,costo4,total4))
print("{:<20}   {:<20}  {:<20,.2f}".format(producto5,costo5,total5))
print("{:<20}   {:<20}  {:<20,.2f}".format(producto6,costo6,total6))
print("{:<20}   {:<20}  {:<20,.2f}".format(producto7,costo7,total7))
print("{:<20}   {:<20}  {:<20,.2f}".format(producto8,costo8,total8))
print("{:<20}   {:<20}  {:<20,.2f}".format(producto9,costo9,total9))
print("{:<20}   {:<20}  {:<20,.2f}".format(producto10,costo10,total10)) #str