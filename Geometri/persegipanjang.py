from Geometri.bangunruang import BangunRuang


class PersegiPanjang(BangunRuang):
    # constructor
    def __init__(self, panjang, lebar):
        self.p = panjang
        self.l = lebar

    def info(self):
        return f'Object ini dibentuk dari class PersegiPanjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l
