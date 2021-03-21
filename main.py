from Geometri.segitiga import Segitiga
from Geometri.persegipanjang import PersegiPanjang

print('Menggunakan OOP')

p1 = PersegiPanjang(12, 5)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(12, 5)
print(s1.info())
print(s1.hitung_luas())

# polymorphism
print('\nMencoba polymorphism')
list_bd = [p1, s1]
for bangun in list_bd:
    print(bangun.info())
    print(bangun.hitung_luas())
