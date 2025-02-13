#Bestelling.py
from Chocolademelk import Chocolademelk

class Bestelling:
    def __init__(self, timestap_tijd_datum, bestelling_cs, afgehaald, item="Chocolademelk"):
        self.timestap_tijd_datum = timestap_tijd_datum
        self.bestelling_cs = bestelling_cs
        self.afgehaald = afgehaald
        self.item = item
        self.chocolade = 0
        self.honing = 0

    def BestellingAfgehaald(self):
        self.afgehaald = True

    def BestellingNietAfgehaald(self):
        self.afgehaald = False

    def voegChocoladeToe(self, aantal):
        self.chocolade=aantal

    def voegHoningToe(self, aantal):
        self.honing=aantal