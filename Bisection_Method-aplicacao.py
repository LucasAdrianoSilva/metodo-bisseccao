"""
BISECTION METHOD
"""

# 
#Bisection Theorem
#Assumindo que f é uma funcao continua [a,b], e existe um r no intervalo [a,b] 
#f(r) = 0.
# se f(a) e f(b) tem sinais opostos, {c_n}_n=0^inf representa a
# sequencia de pontos médios gerados pelo bisection process
#Entao:
# |r - c_n| <= (b-a)/(2^(n+1)), para n = 0, 1, ...
#
#{c_n} converge para zero x=r,
# lim(c_n) = r
#
#O intervalo diminui pela metade a cada passo
#

"""
Input:
    f: The function input
    a: The left endpoint
    b: The right endpoint
    delta: The tolerance
Output:
    c: The zero/root
    yc = f(c)
    err: The error estimate for c
"""
def bisect(f, a, b, delta):
    ya = f(a)
    yb = f(b)
    if ya*yb > 0: return np.nan, np.nan, np.nan
    
    maxit = 1+int(np.round((np.log(b-a)-np.log(delta))/np.log(2)))
    for k in range(maxit):
        c = (a+b)/2
        yc = f(c)
        if yc == 0: 
            a,b = c,c
        elif yb*yc > 0:
            b, yb = c, yc
        else:
            a, ya = c, yc
        if b - a < delta: break
    c = (a+b)/2
    err = np.abs(b-a)
    yc = f(c)
    return c, yc, err


root, fr, erro = bisect(excess_supply_function, 1, 5, 0.0000001)
root
fr
erro

#################################################################################
#################################################################################
#################################################################################
#################################################################################


#
# Economizando 250 reais por mes no periodo de 20 anos
#Qual é a taxa de juros necessária para que o valor total se torne 250.000 reais?
#
# P = 250
# A = 250000
# N = 240
#
# A = (P/(I/12))*((1+I/12)**N - 1)
#

def A(P,I,N):
    return (P/(I/12))*((1+I/12)**N - 1)

A(250, 0.10, 240)
A(250, 0.15, 240)

def f(x):
    return A(250, x, 240) - 250000

root, fr, erro = bisect(f, 0.10, 0.15, 0.0000001)
root
fr
erro

A(250, root, 240)
