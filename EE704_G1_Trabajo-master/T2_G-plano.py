import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np



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

print(df_c)



#--------------------------------------------------

fig = plt.figure()
ax = fig.gca(projection='3d')
surf=ax.plot_trisurf(df_c["Mes"], df_c["Hrs"], df_c['kWh'], cmap=plt.cm.viridis, linewidth=0.2,antialiased=False)
#cmap=plt.cm.viridis -- Es la apleta de colores
fig.colorbar( surf, shrink=0.5, aspect=5)

# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_zlim(0.09,1)
ax.view_init(30, 45)
ax.set_xlabel('Mes')
ax.set_ylabel('Hrs')
ax.set_zlabel('kWh')


plt.xticks(np.arange(int((df_c["Mes"].min())), int(df_c["Mes"].max())+3+1, 1.0))
plt.yticks(np.arange(int((df_c["Hrs"].min())), int(df_c["Hrs"].max())+1, 3.0))
plt.show()


#--------------------------------------------------

