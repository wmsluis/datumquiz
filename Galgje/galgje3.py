import re
import random

class Galgje(object):
    """ Eén spelletje galgje """

    def __init__(self, woordenlijst, maxgok):
        self.het_woord = random.choice(woordenlijst).upper()
        self.invul = ['_'] * len(self.het_woord)    # array met gedeeltelijk ingevulde antwoord
        self.max_gokken = maxgok
        self.pogingen = 0                           # aantal mislukte gokbeurten
        self.geprobeerd = []                        # gegokte letters
 
    def speel(self):
        toestand = "ophalen_gok"
        while toestand != "exit":
            actie = getattr(self, toestand)
            toestand = actie()

    def ophalen_gok(self):
        print(f'\nGalgje woord: {self.toon_woord()}')
        print(f'de volgende letters heb je reeds geprobeerd: {self.geprobeerd}')
        print(f'je mag nog {self.max_gokken - self.pogingen} keer raden')
        self.gok = input("Raad een letter of probeer het woord te raden (of punt(.) of te stoppen: ").upper()
        return "verwerk_gok"

    def verwerk_gok(self):
        if self.gok == ".":
            return "exit"

        if len(self.gok) != 1 or not self.gok.isalpha():
            print("incorrect invoer, vul één letter in.")
            return "ophalen_gok"

        if self.gok in self.geprobeerd:
            print("deze letter is al gebruikt, probeer opnieuw")
            return "ophalen_gok" 

        self.geprobeerd.append(self.gok)

        if not self.gok in self.het_woord:
            return "foute_gok" 
    
        return "goede_gok" 

    def foute_gok(self):
        print(f'\nhelaas, de letter {self.gok} komt niet voor in het woord')
        self.pogingen += 1
        return "toon_voortgang"

    def goede_gok(self):
        print(f'de letter {self.gok} komt voor in het woord')
        for index, letter in enumerate(self.het_woord):
            if letter == self.gok:
                self.invul[index] = self.gok
        return "toon_voortgang"

    def toon_voortgang(self):
        if self.pogingen >= self.max_gokken:
            return "te_veel_pogingen"

        if '_' not in self.invul:
            return "woord_geraden"

        return "ophalen_gok"

    def te_veel_pogingen(self):
        print(f'Jammer joh! Dat was kennelijk te moeilijk :-p  Het woord was: {self.het_woord} ')
        return "exit"

    def woord_geraden(self):
        print(f"\nGefeliciteerd, je hebt het geraden!!! Het woord was '{self.het_woord}'")
        return "exit"
 
    def toon_woord(self):
        "hulpfunctie, geen toestand" 
        return " ".join(self.invul)

