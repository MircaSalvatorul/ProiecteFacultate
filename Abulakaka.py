# # # # # # # # # # lista_num = [1, 2, 3, 4, 5]
# # # # # # # # # #
# # # # # # # # # # primul_elem = lista_num[0]
# # # # # # # # # #
# # # # # # # # # # #slicing
# # # # # # # # # # sublist =lista_num[2:4]
# # # # # # # # # # print(sublist)
# # # # # # # # # #
# # # # # # # # # # lista_num[0] = 3
# # # # # # # # # # print(lista_num[0])
# # # # # # # # #
# # # # # # # # # numere =[1,5, 10, 15,20]
# # # # # # # # #
# # # # # # # # # rezultat = []
# # # # # # # # #
# # # # # # # # # for numar in numere:
# # # # # # # # #     if numar % 2 == 0:
# # # # # # # # #         rezultat.append(numar *2)
# # # # # # # # #     else:
# # # # # # # # #         rezultat.append(numar+1)
# # # # # # # # # print(rezultat)
# # # # # # # # #
# # # # # # # #
# # # # # # # # cuvinte = ["python", "abu", "la", "kaka","if","if-else"]
# # # # # # # #
# # # # # # # # #list comprehension care e ceva asemanator parcurgere, sau asa explica el
# # # # # # # #
# # # # # # # # cuvinte_cu_e = [cuvant for cuvant in cuvinte if 'e' in cuvant]
# # # # # # # # #its weird that the thing above actually works, da, ok are sens insa capul meu de c++ nu intelege astea
# # # # # # # # print(cuvinte_cu_e)
# # # # # # # #
# # # # # # #
# # # # # # # numere = [1,2,3,4,5]
# # # # # # # litere = ['e','b','c','r','t']
# # # # # # #
# # # # # # # rezultat = []
# # # # # # # for i in range(len(numere)):
# # # # # # #     if i % 2 ==0:
# # # # # # #         rezultat.append(numere[i])
# # # # # # #     else:
# # # # # # #         rezultat.append(litere[i])
# # # # # # #
# # # # # # # print(rezultat)
# # # # # #
# # # # # # animale = ["caine","pisica"]
# # # # # # animale.insert(1,"papagal")
# # # # # # print(animale)
# # # # # #
# # # # # # animale.remove("pisica")
# # # # # # print(animale)
# # # # #
# # # # # #acum vorbim tuple,whatever they are
# # # # # #so...basically constant list, sounds easy
# # # # # tuplu_culori = ("rosu","verde","albastru")
# # # # # coordonate = (3,7)
# # # # #
# # # # # sub_tupla = tuplu_culori[1:3]
# # # # # print(sub_tupla)
# # # # # tupla_singur = (42,)
# # # # #
# # # # # print(tupla_singur)
# # # # #
# # # #
# # # # tupla_mutable = ([1,2,3], "test")
# # # # tupla_mutable[0][0] =10
# # # # print(tupla_mutable)
# # # #
# # # # # tupla_mutable[1] = 10,asta nu se poate ca nu poti sa schimbi tupla.
# # # # #funnily enough poti sa schimbi o lista dintr-o tupla
# # # #
# # #
# # # tuplu_culori = ("rosu","verde","albastru")
# # # for culoare in tuplu_culori:
# # #     print(culoare)
# #
# # #dictionar, which is list but more,similar la o clasa
# # student = {"nume": "Ana", "varsta": 24, "note":9.5}
# #
# # print(student["varsta"])
# # student["varsta"] = 21
# # print(student)
# #
# # student["departament"] = "matematicaptu"
# # print(student)
# #
# # #this one is funny, nu mai ai removal ai direct DELETE
# # del student["note"]
# # print(student)
# #
# # if "varsta" in student:
# #     print("Cheia 'varsta' exista")
# #
# # for cheie in student:
# #     print(cheie)
# #
# # for cheie, valoare in student.items():
# #     print(cheie,valoare)
# #
# # chei = list(student.keys())
# # print(chei)
# # valori = list(student.values())
# # print(valori)
# #
#
# catalog = {
#     "Ana": [3,4,5],
#     "Ion":[9,5,7]
# }
# print("Notele Anei sunt: ", catalog["Ana"])
#
# catalog["Andrei"]= [6,7,4]
#
# catalog["Ion"].append(9)
#
# for student,note in catalog.items():
#     medie = sum(note)/ len(note)
#     print(f"Medie pentru {student} este: ,{medie: .2f}")
#
# numar_studenti = len(catalog)
# print(numar_studenti)
#
# student_cu_medie_max = max(catalog, key=lambda student:sum(catalog[student]) / len(catalog[student]))
# print(student_cu_medie_max)
#
