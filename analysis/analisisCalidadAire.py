import pandas as pd

from generators.generadorICA import generarDatosICA


def construirDATAICA():
    #Creando un dataframe
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA, columns=["comuna","ICA","fecha","id"])
    dataFrameICA.to_csv("datosica.csv", index=False)
    
    print(dataFrameICA)

construirDATAICA()