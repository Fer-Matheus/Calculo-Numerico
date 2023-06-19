import numpy as np
import matplotlib.pyplot as plt
def f1(i):
    return 1
def fx(i):
    return i
def fx2(i):
    return i**2
def fx3(i):
    return i**3
def fx4(i):
    return i**4
def fx5(i):
    return i**5
def fx6(i):
    return i**6

def Somatorio(fLinha, fColuna, valoresX, valoresY):
    soma = 0.0
    if fColuna is None:
        for i in range(0,len(valoresX)):
            soma += fLinha(valoresX[i])*valoresY[i]
        return soma
    else:
        for i in valoresX:
            soma += fLinha(i)*fColuna(i)
        return soma

def MontaMatriz(func, valoresX, valoresY):
    A = []
    b = []
    for fLinha in func: # [f1,fx,]
        b.append(Somatorio(fLinha, None, valoresX, valoresY))
        linha = []
        for fColuna in func:
            linha.append(Somatorio(fLinha, fColuna, valoresX, None))
        A.append(linha)
    return A, b

def MostrarMatriz(A,b):
    alf = list("abcdefghijklmnopqrstuvwxyz")
    subAlf = alf[0:len(A)]
    reverseindex = -1
    for linha in A:
        print(f"{linha} [{subAlf[reverseindex]}] = {round(b[A.index(linha)],2)}")
        reverseindex-=1
        
def GeraGrafico(f,x,y):
    conjX = np.linspace(min(x), max(x), 2000)
    conjY = []
    index = -1
    for item in conjX:
        conjY.append(0)
        for func in f:
            conjY[index] += coeficientes[f.index(func)]*func(item)
    plt.scatter(x,y)
    plt.plot(conjX,conjY,'red')
    plt.show()
  
x = [2.5, 3.8, 5.8, 4.2, 6.6, 3, 3.4, 7.4, 6.6, 1.9]
y = [0.9, 1.2, 1.6, 1.42, 1.75, 1.10, 1.2, 2, 1.96, 0.58]
f = [f1,np.log]
A, b = MontaMatriz(f,x,y)
MostrarMatriz(A,b)



coeficientes = np.linalg.solve(A,b)
GeraGrafico(f,x,y)


