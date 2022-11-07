#this one does the a ** b operation 
def elevado(a,n):
    if n == 1:
        return a
    return a * elevado(a,n-1)

#this one does thhe basic multiplication operation
def produto(a,b):
    if b == 1:
        return a
    return a + produto(a,b-1)

#this one gives you the number in binary
def binario(a):
    if a > 1:
        binario(a//2)
    print(a % 2,end = '')

#This one tells you how many digits there are
def digitos(a):
    if a < 10:
        return 1
    else:
        return 1 + digitos(a / 10)

# This one adds the values of the digits
def soma_digitos(a):
    if a < 10:
        return a
    else:
        return (a % 10) + int(soma_digitos(a/10))

#This one gives tou max from list
def Max(s):
    if len(s) == 1:
        return s[0]
    else:
        return s[0] if s[0] > Max(s[1:]) else Max(s[1:])

#This one gives you min from list
def Min(s):
    if len(s) == 1:
        return s[0]
    else:
        return s[0] if s[0] < Min(s[1:]) else Min(s[1:])

#This one gives you the sum of the list
def soma_list(s):
    if len(s)== 1:
        return s[0]
    else:
        return s[0] + soma_list(s[1:])

#This one gives you the sum of even numbers of the list
def soma_pares_lista(s):
    if not s:
        return 0
    else:
        verif = 0 if s[0] % 2 != 0 else s[0]
        return verif + soma_pares_lista(s[1:]) 

#This one is a linear search using recursion
def busca_linear(s,k):
    if s[0] == k:
        return s[0]
    else:
        t = len(s)
        return busca_linear(s[1:], k)if t != 1 else 'não existe na lista'

#This one gives you the multiplication of 2 numbers with the russian multiplication method
def multi_russa(a,b,s = 0):
    if a == 1:
        return s + b if a % 2 !=0 else s
    else:
        return multi_russa(a // 2, b * 2, s + b) if a % 2 !=0 else multi_russa(a // 2, b * 2, s)

