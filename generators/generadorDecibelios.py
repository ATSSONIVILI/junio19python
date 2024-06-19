import random

def generarDatosRuido():
    encuestaRuido=[]
    for i in range(2000):
        dato={}
        id=random.randint(1,50000)
        nivelRuido=random.randint(10,90)
        comuna=random.choice(["comuna1","comuna2","comnuna3","comuna4","comuna5","comuna6","comuna7","comuna8","comuna9","comuna10","comuna11","comuna12","comuna13","comuna14","comuna15","comuna16"])
        
        dato=[id,nivelRuido,comuna]
        encuestaRuido.append(dato)
        
    print(encuestaRuido)
generarDatosRuido()
