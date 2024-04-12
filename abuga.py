# class masina:
#     def __init__(self, marca, model, an):
#         self.marca = marca
#         self.model = model
#         self.an = an
#
#     def afisare_info(self):
#         print(f"Masina: {self.marca} {self.model}, Anul {self.an}")
#
#
# masina1 = masina("Ford", "Focus", 2019)
# masina1.afisare_info()
# # self este un fel de public
#
# class angajat:
#     numar_angajati = 0
#
#     def __init__(self, nume, salariu):
#         self.nume = nume
#         self.salariu = salariu
#         angajat.numar_angajati +=1
#     def afisare(self):
#         print(f"Angajatul {self.nume} are un salariu de {self.salariu}")
#     @classmethod
#     def numar_total_angajati(cls):
#         print(f"Numarul total de angajati: {cls.numar_angajati}")
#
# angajat1 = angajat("John",5000)
# angajat2 = angajat("Alice",6000)
# angajat1.afisare()
# angajat.numar_total_angajati()

# INCAPSULARE
# basically hiding it in packages

# class contbancar:
#     def __init__(self,proprietar,sold):
#         self.__proprietar = proprietar
#         self.__sold = sold
#     def afisare(self):
#         print(f"Soldul contului: {self.__sold}")
#     def depune(self,suma):
#         self.__sold +=suma
# cont = contbancar("John",5000)
#
# cont.afisare()
# cont.depune(900)
# cont.afisare()

# underscore urile o fac protected. so you know, not seen

# MOSTENIRE

# class Animal:
#     def __init__(self,nume):
#         self.nume = nume
#     def sunet(self):
#         pass
# class Caine(Animal):
#     def sunet(self):
#         return "Ham!"
# class Pisica(Animal):
#     def sunet(self):
#         return "Miau!"
#
# caine = Caine("Rex")
# pisica = Pisica("Casper")
# print(caine.nume + ": "+ caine.sunet())
# print(pisica.nume + ": " + pisica.sunet())

# POLIMORFISM
#
# class Animal:
#     def sunet(self):
#         pass
# class Caine(Animal):
#     def sunet(self):
#         return "Ham!"
# class Pisica(Animal):
#     def sunet(self):
#         return "Miau!"
#
# def afisare_sunet(animal):
#     print(animal.sunet())
#
# caine = Caine()
# pisica = Pisica()
# afisare_sunet(caine)
# afisare_sunet(pisica)

#
# class contbancar:
#     def __init__(self, sold):
#         self.__sold = sold
#
#     def afisare(self):
#         print(f"Soldul contului: {self.__sold}")
#
#     def depune(self, suma):
#         self.__sold += suma
#
#     def retragere(self, suma):
#         if self.__sold < suma:
#             print("Sold insuficient")
#         else:
#             self.__sold -= suma
#
#
# cont = contbancar(5000)
# #print(cont.__sold)
# cont.afisare()
# cont.depune(900)
# cont.afisare()
# cont.retragere(500)
#
#
# class FormaGeometrica:
#     def __init__(self,lungime,latime):
#         self.lungime = lungime
#         self.latime = latime
# class Dreptunghi(FormaGeometrica):
#     aria = 1
#     def Aria_dreptunghi(self):
#         self.aria = self.lungime * self.latime
#
#     def afisare_info(self):
#         print(f"Lungime: {self.lungime}")
#         print(f"Latime: {self.latime}")
#         print(f"Aria: {self.aria}")
# dreptunghi =Dreptunghi(10,5)
# dreptunghi.Aria_dreptunghi()
# dreptunghi.afisare_info()


class Camera:
    def descriere(self):
        pass
class CameraSimpla(Camera):
    def descriere(self):
        return "Doua camere si o baie"
class CameraDubla(Camera):
    def descriere(self):
        return "Patru camere cu doua bai si spa"

def afisare_descriere(Camera):
    print(Camera.descriere())

simpla = CameraSimpla()
dubla = CameraDubla()
afisare_descriere(simpla)
afisare_descriere(dubla)