#Werknemer.py
class Werknemer:
    def __init__(self,name,achternaam,credits):
        self.name=name
        self.achternaam=achternaam
        self.credits=credits
        self.bestelling=None
        self.done=False

    def assign(self,bestelling):
        self.bestelling=bestelling


    def SubstractMax(self):
        self.credits-=self.credits


    def Done(self):
        self.done=True
        if self.bestelling is not None:
            self.bestelling.BestellingAfgehaald()

    def NotYet(self):
        self.done=False
        if self.bestelling is not None:
            self.bestelling.BestellingNietAfgehaald()


