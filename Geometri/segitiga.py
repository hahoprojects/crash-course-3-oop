from Geometri.bangunruang import BangunRuang


class Segitiga(BangunRuang):
    # constructor
    def __init__(self, alas = 0, tinggi = 0):
        self.a = alas
        self.t = tinggi

    def info(self):
        return f'Object ini dibentuk dari class PersegiPanjang dengan alas = {self.a} dan tinggi = {self.t}'

    def hitung_luas(self):
        return self.a * self.t / 2
