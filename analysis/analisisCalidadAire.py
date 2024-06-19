import pandas as pd
import matplotlib.pyplot as plt

from generators.generadorICA import generarDatosICA


def construirDATAICA():
    #Creando un dataframe
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA, columns=["comuna","ICA","fecha","id"])
    dataFrameICA.to_csv("datosica.csv", index=False)
    
    print(dataFrameICA)
    
    
    #generando graficos de los datos por columna 
    datosOrdenadosPorComuna=dataFrameICA.groupby("comuna")["ICA"].mean()
    plt.figure(figsize=(20,20))
    datosOrdenadosPorComuna.plot(kind="bar", color="green")
    plt.show()

construirDATAICA()