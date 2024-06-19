import random
def generarDatosICA():
    datosEncuesta=[]
    for i in range(2000):
        datos={}
        comuna=random.choice(["comuna1","comuna2","comnuna3","comuna4","comuna5","comuna6","comuna7","comuna8","comuna9","comuna10","comuna11","comuna12","comuna13","comuna14","comuna15","comuna16"])
        ica=random.randint(10,100)
        fecha=random.choice(["2024-06-23","2024-06-25","2024-01-30","2024-07-31"])
        id=random.randint(1,50000)
        dato=[comuna,ica,fecha,id]
        datosEncuesta.append(dato)
    return (datosEncuesta)    
    
    
generarDatosICA()