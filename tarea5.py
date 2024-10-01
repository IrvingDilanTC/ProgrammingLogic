zona1="Guadalupe"
envio1=100#int
arecoger=0.5#float
moto=2.5#float
arecoger1=(envio1*arecoger)
carro1=(envio1*moto)
zona2="Monterrey"
envio2=180
arecoger2=(envio2*arecoger)
carro2=(envio2*moto)
zona3="Apodaca"
envio3=130
arecoger3=(envio3*arecoger)
carro3=(envio3*moto)
zona4="Escobedo"
envio4=200
arecoger4=(envio4*arecoger)
carro4=(envio4*moto)
zona5="Juarez"
envio5=160
arecoger5=(envio5*arecoger)
carro5=(envio5*moto)
zona6="Cadereyta"
envio6=300
arecoger6=(envio6*arecoger)
carro6=(envio6*moto)
print("{:>20}   {:>25}  {:>20}  {:>25}".format("Zona",  "Costo Envio a Moto",       "Costo a recoger",    "Costo Envio en Carro"))
print("{:>20}   {:>20}  {:>20}  {:>20}".format(zona1,envio1,arecoger1,carro1))
print("{:>20}   {:>20}  {:>20}  {:>20}".format(zona2,envio2,arecoger2,carro2))
print("{:>20}   {:>20}  {:>20}  {:>20}".format(zona3,envio3,arecoger3,carro3))
print("{:>20}   {:>20}  {:>20}  {:>20}".format(zona4,envio4,arecoger4,carro4))
print("{:>20}   {:>20}  {:>20}  {:>20}".format(zona5,envio5,arecoger5,carro5))
print("{:>20}   {:>20}  {:>20}  {:>20}".format(zona6,envio6,arecoger6,carro6))