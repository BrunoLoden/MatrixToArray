# https---github.com-BrunoLoden-EE704_G1_Trabajo
Objetivo: Plotear una seria de valores en un plano 3D que muestre Hora, Mes y Energia.
Problema1:No se podia plotear de forma directa extrayendo los datos con un data frame desde el excel. 
Sol1: Se manipulo la informacion el la tabla para obtener un Data frame de 3 columnas "Hora, Mes y Energia" para poder usar mthplotlib para plotear

Poblema2: El atrivuto ".plot_trisurf" para el plotero permite usar columnas de DataFrames, pero nos acepta calores que no sean numeros para el eje Y de "Mes"
Solucion2: Cambiar los meses en forma de numeros :"v - Buscar solucion para esto
