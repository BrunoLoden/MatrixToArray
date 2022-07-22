# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:12:54 2022

@author: ASUS
"""
from pyomo.environ import *

#Creación del modelo
model = ConcreteModel()

n_barras = 6


barra_i = list(range(n_barras))
print(" número de barras: ", n_barras)
print(" indice de barras: ", barra_i)
barra_j = list(range (n_barras))

generada = [0.50, 0.0, 1.65, 0.0, 0.0, 5.45]
demanda = [0.80, 2.4, 0.40, 1.6, 2.4, 0.0]
costos = [[0, 40,38,60,20,68], 
          [40, 0,20,40,31,30],
          [38,20, 0,59,20,48], 
          [60,40,59, 0,63,30], 
          [20,31,20,63, 0,61], 
          [68,30,48,30,61, 0]]
n_barras_iniciales = [[0, 1, 0, 1,1,0], 
                      [1, 0, 1, 1,0,0], 
                      [0, 1, 0, 0,1,0], 
                      [1, 1, 0, 0,0,0], 
                      [1, 0, 1, 0,0,0], 
                      [0, 0, 0, 0,0,0]]

flujo_maxi = [[0   , 1  , 1   , 0.80,1    ,0.70], 
              [1   , 0  ,1    , 1   , 1   , 1], 
              [1   , 1  , 0   , 0.82, 1   , 1], 
              [0.80, 1  , 0.82, 0   , 0.75, 1], 
              [1   , 1  , 1   , 0.75, 0   , 0.78], 
              [0.70, 1  , 1   , 1   , 0.78, 0]]

Pgen_MAX = [1.50, 0.0, 3.60   , 0.0 , 0.0, 6.0]

n_barras_MAX = 5

S = [[0,-1,0,-1,-1,0],
     [-1,0,-1,-1,0,-1],
     [0,-1,0,0,-1,0],
     [-1,-1,0,0,0,-1],
     [-1,0,-1,0,0,0],
     [0,-1,0,-1,0,0.0]]


# Variables
model.nbar = Var (barra_i, barra_j, domain = NonNegativeIntegers)
model.flujo = Var (barra_i, barra_j, domain = NonNegativeIntegers)
model.Pgen = Var (barra_i, domain = NonNegativeReals)

# Objective function
model.obj = Objective(expr = sum(costos[i][j] * model.nbar[i,j] for i in barra_i for j in barra_j), sense=minimize)

# Restricciones
model.NEGA_flujo = ConstraintList()
for i in barra_i:
    for j in barra_j:
        if(i<j):
            model.NEGA_flujo.add(expr = model.flujo[j,i]== - model.flujo[i,j])

model.Pflujo = ConstraintList()
for i in barra_i:
    model.Pflujo.add(expr = sum(S[i][j]*model.flujo[i,j] for j in barra_j) + generada[i] == demanda[i])

model.vAbsoluto = ConstraintList()
for i in barra_i:
    for j in barra_j:
        if (i < j):
            model.vAbsoluto.add(expr = model.flujo[i,j] <= (model.nbar[i,j] + n_barras_iniciales[i][j]) * flujo_maxi[i][j])
            model.vAbsoluto.add(expr = model.flujo[i,j] >= -(model.nbar[i,j] + n_barras_iniciales[i][j]) * flujo_maxi[i][j])

model.Pot_gen = ConstraintList()
for i in barra_i:
    model.Pot_gen.add(expr = model.Pgen[i] <= Pgen_MAX[i])

model.N_nbar = ConstraintList()
for i in barra_i:
    for j in barra_j:
        if (i < j):
            model.N_nbar.add(expr = model.nbar[i,j] <= n_barras_MAX)

model.pprint()
#Seleccionamos solver
optimizer = SolverFactory('glpk')

#resolucion del problema
results = optimizer.solve(model, tee=False)
#objValue = model.obj.expr()
#print("el valor óptimo de la funcion objetivo es: ", objValue)

#Impresion de la solucion
for i in barra_i:
    for j in barra_j:
        xValue = model.nbar[i,j].value

        #print("Se deben agregar %d barras, una de ellas será en: la barra B[%d][%d]" % (xValue, i,j))

termination = results.solver.termination_condition
print("el programo termino porque es: ", termination)
