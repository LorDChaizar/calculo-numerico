from math import *
def derivada(f,h=0.02):
    def _(x):
        return (f(x+h)-f(x))/h
    return _
def newton_rapson(f,x,er,N):
    df=derivada(f,h=0.02)
    xi=x
    error=1e3
    n=1
    while(error>er)&(n<N):
        xi=xi-f(xi)/df(xi)
        error=abs(f(xi))
        print("iteracion:",n,"aproximacion",xi,"error",error)
        n=n+1
        print("solucion aproximada",xi)
    return xi
if __name__ == "__main__":
    # Pruebe aquí su función.
    f= lambda x: x**2-10;
    newton_rapson(f,3,1e-3,5)
    pass