#discutii while si for
# for x in range(6):
#       print(x)
#
# for x in range(2, 30, 3):
#   print(x)
#
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x, y)
#
# i = 1
# while i < 6:
#   print(i)
#   i += 1
#
# #VARIANTA CORECTA
# i=0
# n = int(input("Enter a number:"))
# while i<n:
#     if i%2==0: print(i)
#     i+=1
#
# #VARIANTA 2
# i=0
# n = int(input("Enter a number:"))
# while i<n:
#     print(i)
#     i+=2
#
#
# i=1
# j=1
# n=12
# a=0
# print(i)
# print(j)
# for x in range(n):
#     k=i+j
#     print(k)
#     i=j
#     j=k
# else:
# #     print("Uite fir fibonacci")
# #SUMA patratelor numerelor panna la n
# s=0
# n=int(input("Dati numar limita"))
# for x in range(1,n,1):
#     s+= x**2
# print("Suma numerelor patrate")
# print(s)

# #CALCUL FACTORIAL
# n=int(input("Numarul pt factorial: "))
# i=1
# factorial=1
# while i<=n:
#     factorial*=i
#     i+=1
#
# print("Factorial: ")
# print(factorial)
#
#
# #CAUTARE PRIM
# n=int(input("Numarul pt prim: "))
# i=2
# s=0
# while i<n/2:
#     if n%i==0:
#         s+=1
#         break
#     else: pass
#     i += 1
#
# if s==0: print("Este prim")
# else: print("Nu este prim")

# Daca e palindrom numarul doamne ajuta ca am si uitat de cuvantul asta

cuvant=input("Dati cuvant de palindrom")

i=0
s=0
k=0
while i<len(cuvant):
    k+=1
    x=cuvant[i]
    if x==cuvant(-(i+1)): s+=1
    i+=1
if(k==s):print("Este palindrom")
else: print("Nu este")


