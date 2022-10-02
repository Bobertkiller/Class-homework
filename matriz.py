import random 

#gera matriz no tamanho informado
def gera_matriz():
    t = int(input('Quantas linhas na sua matriz: ')) 
    c = int(input('Quantas colunas na sua matriz: '))
    a = [0]*t 
    print('Sua matriz:')
    for i in range(t): 
        b = [0]* c 
        for j in range(c): 
            n = random.randint(1,100) 
            b[j] = n 
        print(b) 
        a[i] = b 
    return a

#Essa função soma os elementos acima da diagonal principal
def s_acima_dp(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j > i:
                s += m[i][j]
    return s

#Essa função soma os elementos abaixo da diagonal principal
def s_abaixo_dp(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j < i:
                s += m[i][j]
    return s

#Essa função calcula a soma dos elementos na diagonal principal
def s_dp(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j == i:
                s += m[i][j]
    return s

#Essa função soma matrizes se possivel
def s_matriz(m,s):
    if len(m) == len(s) and len(m[0]) == len(s[0]):
        s = 0
        for i in range(len(m)):
            for i in range(len(m[0])):
                s+= m[i][j] + s[i][j]
        return s
    else:
        print('Não é possivel realizar a soma dessas matrizes favor insira outras')

#Faz o produto das matrizes se possivel
def p_matriz(m,p):
    if len(m[0]) == len(p):
        n = [0]*len(m)
        for i in range(len(m)):
            c = [0]*len(m[0])
            n[i] = c
            for j in range(len(p[0])):
                for f in range(len(m[0])):
                    n[i][j] += m[i][f] * p[f][j]
        return n
    else:
        print('Essas matrizes são incompatíveis, insira outras')
        
#verifica soma das colunas
def s_colunas(m,c):
    s = 0
    for i in range(len(m)):
        s += m[i][c]
    return s
    
def s_ds(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (j == 1 and i == 1) or (j == 0 and i == 2) or (j == 2 and i == 0):
                s += m[i][j]
    return s

def s_l(m,l):
    s = 0
    for i in range(len(m)):
        s += m[l][i]

#verifica se é um quadrado magico
def verifica_magico(m):
    d1 = s_dp(m)
    d2 = s_ds(m)
    c1 = s_colunas(m, 0)
    c2 = s_colunas(m, 1)
    c3 = s_colunas(m, 2)
    l1 = s_l(m, 0)
    l2 = s_l(m, 1)
    l3 = s_l(m, 2)
    if d1 == d2 == c1 == c2 == c3 == l1 == l2 == l3:
        print('É magico')
    else:
        print('não é magico')


#Exercicio 1:
def exer_1():
    m = gera_matriz()
    print(s_acima_dp(m))

#exercicio 2:
def exer_2():
    m = gera_matriz()
    print(s_abaixo_dp(m))

#exercicio 3
def exer_3():
    m = gera_matriz()
    print(s_dp(m))

#exercicio 4
def exer_4():
    m = gera_matriz()
    s = gera_matriz()
    print(s_matriz(m,s))

#exercicio 5
def exerc_5():
    m = gera_matriz()
    p = gera_matriz()
    p_matriz(m, p)
exerc_5()

#exercicio 6
def exerc_6():
    m = [[8,1,6],[3,5,7],[4,9,2]]
    verifica_magico(m)