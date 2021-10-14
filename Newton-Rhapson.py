import numpy as np
#import sympy as sp
import pandas as pd
pt=pd.read_csv("PARCIAL.csv",encoding="utf8")
Y=np.array([[2.8239-14.9607j,-1.923+9.6153j,-0.9009+5.4054j],[-1.923+9.6153j,3.582-15.7893j,-1.659+6.224j],[-0.9009+5.4054j,-1.659+6.224j,2.5599-11.559j]])
#Y=np.array([[2.1567-8.6273j,-0.5882+2.3529j,0+0j,-0.3921+1.5686j,-1.1764+4.7058j],[-0.5882+2.3529j,2.3528-9.4116j,-1.1764+4.7058j,-0.5882+2.3529j,0+0j],[0+0j,-1.1764+4.7058j,2.3528-9.4116j,0+0j,-1.1764+4.7058j],[-0.3921+1.5686j,-0.5882+2.3529j,0+0j,0.9803-3.9215j,0+0j],[-1.1764+4.7058j,0+0j,-1.1764+4.7058j,0+0j,2.3528-9.4116j]])
#V=np.array([1.02,1.0,1.04,1.0,1.0])
#the=np.array([0,0,0,0,0])
#S_G=np.array([0+0j,0+0j,1.0+0j,0+0j,0+0j])
#S_C=np.array([0+0j,0.6+0.3j,0+0j,0.4+0.1j,0.6+0.2j])
#Y=np.array([[4.098-4.918j,0+0j,-4.098+4.918j],[0+0j,3.975-10.056j,-3.975+10.056j],[-4.098+4.918j,-3.975+10.056j,8.073-14.974j]])
#Y=np.array([[3.6090-36.5636j,-2.0715+20.8916j,-1.5374+15.6720j],[-2.0715+20.8916j,4.1431-41.7833j,-2.0715+20.8916j],[-1.5374+15.6720j,-2.0715+20.8916j,3.6090-36.5636j]])
#Y=np.array([[15-35j,-10+20j,-5+15j],[-10+20j,30-60j,-20+40j],[-5+15j,-20+40j,25-55j]])
#Y=np.array([[-29.98j,20j,10j],[20j,-29.98j,10j],[10j,10j,-20j]])
V=pt["voltage"].to_numpy()
the=pt["thet"].to_numpy()
S_G=pt["P_G"].to_numpy()+pt["Q_G"].to_numpy()*1j
S_C=pt["P_C"].to_numpy()+pt["Q_C"].to_numpy()*1j
tipo=pt["type"].to_numpy()
S=S_G-S_C
N_PV=0
N_PQ=0
for i in range(len(V)):
    if tipo[i]==2:
        N_PV=N_PV+1
    elif tipo[i]==3:
        N_PQ=N_PQ+1
    else:
        pass

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

P=np.ones(len(V)).astype(float)
Q=np.ones(len(V)).astype(float)
###Calculos de las potencias
for i in range(len(V)):
    P_T=0
    Q_T=0
    for m in range(len(V)):
        P_it=V[m]*(Y[i][m].real*np.cos(the[i]-the[m])+Y[i][m].imag*np.sin(the[i]-the[m]))
        Q_it=V[m]*(Y[i][m].real*np.sin(the[i]-the[m])-Y[i][m].imag*np.cos(the[i]-the[m]))
        P_T=P_T+P_it
        Q_T=Q_T+Q_it
    P[i]=V[i]*P_T
    Q[i]=V[i]*Q_T
TP=S.real-P
TQ=S.imag-Q
#creacion del vector de potencias
def Potencia_B(TP,TQ,tipo):
    B=np.array([])
    for i in range(len(TP)):
        m=tipo[i]
        if m==1:
            pass
        else:
            B=np.append(B,TP[i])
    for i in range(len(TQ)):
        m=tipo[i]
        if m==3:
            B=np.append(B,TQ[i])
        else:
            pass
    return B
B=Potencia_B(TP,TQ,tipo)
##JACOBIANO
def H(k,m):
    if k!=m:
        return V[k]*V[m]*(Y[k][m].real*np.sin(the[k]-the[m])-Y[k][m].imag*np.cos(the[k]-the[m]))
    else:
        return -Y[k][k].imag*V[k]**2 -Q[k]
def N(k,m):
    if k!=m:
        return V[k]*V[m]*(Y[k][m].real*np.cos(the[k]-the[m])+Y[k][m].imag*np.sin(the[k]-the[m]))
    else:
        return P[k]+Y[k][k].real*V[k]**2
#######  M=-N    L=H
def M(k,m):
    if k!=m:
        return -N(k,m)
    else:
        return P[k]-Y[k][k].real*V[k]**2
def L(k,m):
    if k!=m:
        return H(k,m)
    else:
        return Q[k]-Y[k][k].imag*V[i]**2
##Creacion de la matriz jacobiana
H_J=np.array([])
N_J=np.array([])
M_J=np.array([])
L_J=np.array([])
for i in range(len(V)):
    if tipo[i]==1:
        pass
    elif tipo[i]==2:
        for j in range(len(V)):
            if tipo[j]==1:
                pass
            elif tipo[j]==2:
                H_J=np.append(H_J,H(i,j))
            else:
                H_J=np.append(H_J,H(i,j))
                N_J=np.append(N_J,N(i,j))
    else:
        for j in range(len(V)):
            if tipo[j]==1:
                pass
            elif tipo[j]==2:
                H_J=np.append(H_J,H(i,j))
                M_J=np.append(M_J,M(i,j))
            else:
                H_J=np.append(H_J,H(i,j)) 
                N_J=np.append(N_J,N(i,j))
                M_J=np.append(M_J,M(i,j))
                L_J=np.append(L_J,L(i,j))
H_J=np.resize(H_J,(N_PV+N_PQ,N_PV+N_PQ))
N_J=np.resize(N_J,(N_PV+N_PQ,N_PQ))
M_J=np.resize(M_J,(N_PQ,N_PQ+N_PV))
L_J=np.resize(L_J,(N_PQ,N_PQ))
J=np.concatenate((np.concatenate((H_J,N_J),axis=1),np.concatenate((M_J,L_J),axis=1)),axis=0)
V_est=np.matmul(np.linalg.inv(J),B)
#T_V=V_est[2]*V[2]


#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

print(pt)
print(V_est)
print(B)
print(J)
print(Y)
print(TP)
print(TQ)
print(P)
print(Q)
