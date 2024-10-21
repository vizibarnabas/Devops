class Auto:
    def __init__(self, marka, modell, evjarat, uzemanyag, sebesseg):
        self.marka = marka
        self.modell = modell
        self.evjarat = evjarat
        self.uzemanyag = uzemanyag
        self.sebesseg = sebesseg

    def adatok(self):
        return f"Autó: {self.marka} {self.modell}, Évjárat: {self.evjarat}, Üzemanyag: {self.uzemanyag}, Sebesség: {self.sebesseg} km/h"

    def get_marka(self):
        return self.marka

    def get_modell(self):
        return self.modell

    def get_evjarat(self):
        return self.evjarat

    def get_uzemanyag(self):
        return self.uzemanyag

    def get_sebesseg(self):
        return self.sebesseg

    def set_sebesseg(self, uj_sebesseg):
        self.sebesseg = uj_sebesseg
