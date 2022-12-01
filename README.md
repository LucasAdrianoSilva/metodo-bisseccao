# metodo-bisseccao



O método da bissecção consiste na divisão do intervalo [a, b] ao meio, obtendo os subintervalos [a, m] e [m, b], e considerar como intervalo de busca o subintervalo em que f possui sinais opostos nos extremos.

Assumindo que f é uma função contínua [a,b], e existe um r no intervalo [a,b]. Considerando f(r) = 0, se f(a) e f(b) tem sinais opostos, {c_n}_n=0^inf representa a sequência de pontos médios gerados pelo método de bissecção.
Então:
|r - c_n| <= (b-a)/(2^(n+1)), para n = 0, 1, ...
