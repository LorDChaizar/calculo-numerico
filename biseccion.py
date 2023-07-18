import math
def biseccion(f,a,b,er,n):
    if f(a)*f(b)<0:
        it=1
        p_M_ACTUAL=0
        p_M_PREVIO=0
        e=100;
        while (it<n)&(e>er):
            p_M_PREVIO=p_M_ACTUAL
            p_M_ACTUAL=(a+b)/2
            if f(p_M_ACTUAL)*f(b)<0:
                a=p_M_ACTUAL
            else:
                b=p_M_ACTUAL
            if it>1:
                e=abs (p_M_ACTUAL-p_M_PREVIO/p_M_ACTUAL)
            it=it+1
            print("iteracion:",it,"medio", p_M_ACTUAL,"error:", e )
        return p_M_ACTUAL 
    else:
        print("EL INTERVALO NO ES VALIDO")
if __name__ == "__main__":
    # Pruebe aquí su función.
    f=lambda x:(math.e)**x-3*(x**2)
    biseccion(f,0,1,0.03,100)
    pass