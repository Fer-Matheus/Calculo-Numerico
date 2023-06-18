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

"""
    Exemplo da matriz A
    A = [[0,0,0]
         [0,0,0]
         [0,0,0]
        ]
"""
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
"""
              f(x)=1 f(x)=x f(x)=x²
    f(x)=1  [ 4.0   15.0   79.0  ]
    f(x)=x  [ 15.0  79.0   477.0 ]
    f(x)=x² [ 79.0  477.0  3043.0]
    
    [ 4.0 15.0][b]=[19.4]
    [15.0 79.0][a]=[96.5]
    
    a = 0.94 , b = 1.04
    
    f(x)=0.94x + 1.04
"""
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
  
      
A, b = MontaMatriz([f1,fx],[1,2,5,7],[2.1,2.9,6.1,8.3])
MostrarMatriz(A,b)


import numpy.linalg as lg
c = lg.solve(A,b)

print(f'f(x)= {round(c[0], 2)}x + {round(c[1],2)}')