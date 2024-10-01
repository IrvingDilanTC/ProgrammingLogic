equipo1="Horno"
precio1=400#int
taxes=0.05#float
pesos=200#int
total1=precio1+(precio1*taxes)
pesos1=(precio1*pesos)
equipo2="Freidora"
precio2=80
total2=precio2+(precio2*taxes)
pesos2=(precio2*pesos)
equipo3="Marmita"
precio3=300#int
total3=precio3+(precio3*taxes)
pesos3=(precio3*pesos)
equipo4="Sartén"
precio4=150#int
total4=precio4+(precio4*taxes)
pesos4=(precio4*pesos)
equipo5="Sierra"
precio5=350
total5=precio5+(precio5*taxes)
pesos5=(precio5*pesos)
equipo6="Congelador"
precio6=500
total6=precio6+(precio6*taxes)
pesos6=(precio6*pesos)
print("{:>20}   {:>20}  {:>20}  {:>25}".format("Equipo",  "Comprado en USD",       "Total más Taxes",    "Precio en Pesos MXN"))
print("{:>20}   {:>20}  {:>20}  {:>20,.3f}".format(equipo1,precio1,total1,pesos1))
print("{:>20}   {:>20}  {:>20}  {:>20,.3f}".format(equipo2,precio2,total2,pesos2)) 
print("{:>20}   {:>20}  {:>20}  {:>20,.3f}".format(equipo3,precio3,total3,pesos3))
print("{:>20}   {:>20}  {:>20}  {:>20,.3f}".format(equipo4,precio4,total4,pesos4))
print("{:>20}   {:>20}  {:>20}  {:>20,.3f}".format(equipo5,precio5,total5,pesos5))
print("{:>20}   {:>20}  {:>20}  {:>20,.3f}".format(equipo6,precio6,total6,pesos6)) #str