
import numpy as np
import pandas as pd

def l1(a):
    for i in a:
        del i[0]
    return a

df_a = pd.DataFrame(pd.read_excel("Datos.xlsx","H1"))

#Probar fech para terminar con elcommit
generada = np.array(df_a["Generada"])
demanda = np.array(df_a["Demanda"])
Pgen_MAX = np.array(df_a["Pgen_MAX"])

df_b = pd.DataFrame(pd.read_excel("Datos.xlsx","Costos"))
costos = l1(df_b.to_numpy().tolist())
print(costos)
print("------------------------------------------")

df_c = pd.DataFrame(pd.read_excel("Datos.xlsx","n_b_i"))
n_barras_iniciales = l1(df_c.to_numpy().tolist())
print(n_barras_iniciales)
print("------------------------------------------")

df_d = pd.DataFrame(pd.read_excel("Datos.xlsx","Flujo_maxi"))
flujo_maxi = l1(df_d.to_numpy().tolist())
print(flujo_maxi)
print("------------------------------------------")

df_e = pd.DataFrame(pd.read_excel("Datos.xlsx","S"))
S = l1(df_e.to_numpy().tolist())
print(S)

# df_e = pd.DataFrame(pd.read_excel("Datos.xlsx","S"))
# S = df_e.to_numpy().transpose().tolist()
# del S[0]
# print(S)