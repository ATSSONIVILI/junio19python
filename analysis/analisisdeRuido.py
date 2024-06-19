import pandas as pd

from generators.generadorDecibelios import generarDatosRuido


def construirDataRuido():
    #Creando un dataframe
    datosRuido=generarDatosRuido()
    ruidoDataFrame=pd.DataFrame(datosRuido, columns=["id","nivel de ruido","comuna"])
    ruidoDataFrame.to_csv("datosruido.csv", index=False)
    
    print(ruidoDataFrame)

construirDataRuido()