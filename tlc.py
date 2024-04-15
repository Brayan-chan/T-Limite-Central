from scipy import stats #Para la distribución de probabilidad
import matplotlib.pyplot as plt #Para graficar
import numpy as np #Para arreglos

np.random.seed(0) #Para fijar una semilla
plt.rcParams["font.size"] = 18 #Para cambiar el tamaño de fuente

def datos_sesgados(sesgo, cantidad, maximo): #Función para generar datos sesgados
    aleatorios = stats.skewnorm.rvs(sesgo, #Distribución de probabilidad
                                    size=cantidad, #Tamaño de la muestra
                                    random_state=1) #Fijar una semilla
    aleatorios = (aleatorios + abs(aleatorios.min())) #Para que los datos sean positivos
    aleatorios = aleatorios / aleatorios.max() * maximo #Para que los datos sean entre 0 y maximo
    return aleatorios

mayores = datos_sesgados(-10, 100000, 100) #Generar datos sesgados
plt.hist(mayores, bins = 1000, alpha = 0.5, label = "Mayores", color = "blue") #Graficar histograma

jovenes = datos_sesgados(10, 100000, 100) #Generar datos sesgados
plt.hist(jovenes, bins = 1000, alpha = 0.5, label = "Jovenes", color = "deeppink") #Graficar histograma

normales = datos_sesgados(0, 100000, 100) #Generar datos sesgados
plt.hist(normales, bins = 1000, alpha = 0.5, label = "Normales", color = "orange") #Graficar histograma

plt.ylim([0, 400]) #Para ajustar el eje y
plt.xlim([0, 100]) #Para ajustar el eje x

plt.legend(bbox_to_anchor = (1, 0.5)) #Para colocar la leyenda
plt.show() #Para mostrar el histograma