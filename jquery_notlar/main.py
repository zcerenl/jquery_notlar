# class Kisi:
#     def __init__(self, isim, soyisim):
#         self.isim = isim
#         self.soyisim = soyisim

#     def bilgiGoster(self):
#         print(f'İsim: {self.isim}, Soyisim: {self.soyisim}')

# class Ogrenci(Kisi):
#     def __init__(self, isim, soyisim, okulNo, ortalama):
#         super().__init__(isim, soyisim)
#         self.okulNo = okulNo
#         self.ortalama = ortalama


# kisi1 = Kisi("Ali", "Ahmet")
# ogrenci1 = Ogrenci("Ali", "Ahmet", "541", "80")

# # print(kisi1.isim, kisi1.soyisim)
# print(ogrenci1.okulNo)

#Köpek
#Tavşan
#kırkayak
# class Hayvan: 
#     def __init__(self, boyut, renk, patiSayisi):
#         self.boyut = boyut
#         self.renk = renk
#         self.patiSayisi = patiSayisi

#     def kacAyakli(self):
#         print(f'{self.patiSayisi}')

# class Kopek(Hayvan):
#     pass
#     # def kacAyakli(self):
#     #     print(f'{self.patiSayisi}')

# class Insan(Hayvan):
#     def kacAyakli(self):
#         print(f'{self.patiSayisi}')

# class Kirkayak(Hayvan):
#     def kacAyakli(self):
#         print(f'{self.patiSayisi}mm')


# kopek1 = Kopek("20","siyah","4")
# insan1 = Insan("180","ten rengi","2")
# kirkayak1 = Kirkayak("3", "siyah", "40")

# kopek1.kacAyakli()
# insan1.kacAyakli()
# kirkayak1.kacAyakli()

