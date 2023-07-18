import math
def derivada(f, h = 0.01):
  
    def _(x):
        return (f(x + h) - f(x))/h

    return _

def operaciones(f,x0,n,x):
    contador=0
    px=0
    aux=0
    while contador<n:
        if contador==0:
            px=f(x0)
            contador=contador+1
        else:
            dfs=derivada(f)
            f=dfs
            aux=(dfs(x0)*((x-x0)**contador))
            aux=aux/math.factorial(contador)
            px+=aux
            contador=contador+1
    return px
def polinomio_taylor(f, x0, n):
    
    def __(x):
        po=operaciones(f,x0,n,x)
        return po
    return __


if __name__ == '__main__':
    
    f=lambda x: math.sin(x)
    pol=polinomio_taylor(f,0,4)
    x=0.30
    print(pol(x))