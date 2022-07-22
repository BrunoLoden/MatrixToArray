import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


a = pd.read_excel("Avance 2.xlsx","Tabla-Consumo",header=1)
#a = pd.read_excel("Avance 2.xlsx","Tabla-Consumo",header=1,index_col=1)
df_a = pd.DataFrame(a)

df_a.drop('Unnamed: 0', inplace=True, axis=1) #axis = 1 : colum not row
df_a.drop(24,axis=0,inplace=True)
#df_a.drop("Total diario",axis=0,inplace=True)
#del df_a["a"]                        #Quitar columna por nombre  
j=1

for i in df_a.columns.drop(["Hrs","Promedio "]):
    
    l=((str(j)+" ")*len(df_a.index)).split()
    #l=((str(i)+" ")*len(df_a.index)).split()

    df_b = df_a[["Hrs",str(i)]]
    
    df_b=df_b.assign(Mes=l)
    df_b=df_b[["Mes","Hrs",str(i)]]
    df_b.rename(columns={str(i):"kWh"},inplace=True)
    
    if (j<=1):
        df_c = df_b

    else:
        df_c = df_c.append(df_b,ignore_index=True)

    j = j+1
    #print(df_c)
    

print(df_c)
    

threedee = plt.figure().gca(projection='3d')
threedee.scatter(df_c["Mes"], df_c["Hrs"], df_c['kWh'])
threedee.set_xlabel('Mes')
threedee.set_ylabel('Hrs')
threedee.set_zlabel('kWh')
plt.show()

#--------------------------------------------------
# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True

# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)

# x, y = np.meshgrid(x, y)
# eq = 0.12 * x + 0.01 * y + 1.09

# fig = plt.figure()

# ax = fig.gca(projection='3d')

# ax.plot_surface(x, y, eq)

# plt.show()