# def funct(nr1,nr2):
#     rezultat = nr1 + nr2
#     print(rezultat)
# nr1=int(input("Dati numar 1:"))
# nr2 =int(input("Numar 2:"))
# funct(nr1,nr2)
#
# def paritate(x):
#     if(x%2 ==1): print("este impar")
#     else: print("este par")
#
# #better versiom
#
# def pari(x):
#     return x%2
# nr =int(input("da numar:"))
# paritate(nr)
# print(paritate(nr))
#
# def factorial(x):
#     if x ==0:
#         return 1
#     else:
#         return x * factorial(x-1)
# x=int(input("Da numar"))
# print(factorial(x))

#
# def string(cuv):
#     i=0
#     newstring = ''
#     while i < len(cuv) and cuv[i] != '\0':
#         newstring += cuv[len(cuv)-i]
#         i += 1
#     # daca scrii return string[::-1] also works. practic for care merge inapoi in string datorita -1
#     return newstring
# cuv=input("Cuvant: ")
# print(string(cuv))
#
# def vocale(cuv):
#     nr=0
#     vocal="aeiou"
#     for i in cuv:
#         if i in vocal:
#             nr+=1
#     return nr
# cuv = input("Dati cuvant: ")
# print(vocale(cuv))
#
# def gcd(n1,n2):
#     if n1 == n2:
#         return n1
#     elif n1 > n2:
#         return gcd(n1-n2,n2)
#     else: return gcd(n2-n1,n1)
#
# n1=int(input("Nr 1:"))
# n2=int(input("Nr 2:"))
# print(gcd(n1,n2))

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
nr=int(input("numar: "))
print(fibonacci(nr))