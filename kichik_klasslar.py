class Shaxs():
    """ Shaxs nomli klass yaratamiz """
    def __init__(self, ism, familya, ota_ismi, t_yili, manzili, malumoti, kasb):
        """ Shaxsning xsusiyatlari """
        self.ism = ism
        self.familya = familya
        self.ota_ismi = ota_ismi
        self.t_yili = t_yili
        self.manzili = manzili
        self.malumoti = malumoti
        self.kasb = kasb

    def get_fulname(self):
        return f"Assalomu alekum mening isim sharifim {self.ism.title()} {self.familya.title()} {self.ota_ismi.title()}"

    def get_age(self, joriy_yil):
        return f"Mening yoshim {joriy_yil - self.t_yili} da"

    def get_full_addres(self, tuman, mahalla, kocha):
        return f"Men {self.manzili.title()} viloyati {tuman.title()} tuman {mahalla.title()} mahallasi {kocha.title()} ko'chasida yashayman."

    def get_full_information(self, oqish_nomi, yonalish):
        return f"Malumotim {self.malumoti.title()} men {oqish_nomi.title()}ni {yonalish.title()} yo'nalishini tamomlaganman."

    def get_profession(self):
        return self.kasb.title()
    
