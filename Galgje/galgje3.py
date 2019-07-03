import re
import random


class Galgje(object):
    """ spelletje galgje """

    def __init__(self, woordenlijst):
        self.woordenlijst = []
        self.het_woord = random.choice(woordenlijst)
        self.aantal_gokken = 10
        self.invul = str("_ " * len(self.het_woord))
        self.geprobeerd = []


    def speel(self):
        toestand = "nieuw_woord"
        while toestand != "exit":
            actie = getattr(self, toestand)
            toestand = actie()

    def nieuw_woord(self):
        print(f'De lengte van het woord is {len(self.het_woord)} letters')
        return "start"


    def start(self):
        if '_' not in self.invul:
            return "woord_geraden"

        if self.aantal_gokken > 0:
            print(f'\nGalgje woord: {self.invul}')
            print(f'de volgende letter heb je reeds geprobeerd: {self.geprobeerd}')
            print(f'Je mag nog {self.aantal_gokken} keer raden')
            return "antwoord"

        else:
            print(f'Jammer joh! Dat was kennelijk te moeilijk :-p  Het woord was: {self.het_woord} ')
            input("druk op een toests om af te sluiten")
            return "exit"


    def antwoord(self):
        self.gok = input("raad een letter of probeer het woord te raden: ")

        if len(self.gok) == 1:
            return "check_letter"

        elif len(self.gok) == len(self.het_woord):
            return "check_woord"

        else:
            print("incorrect aantal letters. Vul één letter in of raad het hele woord ")
            return "start"


    def check_letter(self):
        self.geprobeerd.append(self.gok)

        if self.gok in self.het_woord:
            return "letter_correct"

        else:
            return "letter_incorrect"


    def letter_correct(self):
        print(f'de letter {self.gok} komt voor in het woord')
        for gevonden in re.finditer(self.gok, self.het_woord):
            positie = int(gevonden.start())
            self.invul = self.invul[:positie * 2] + self.gok + self.invul[2 * positie + 1:]
        return "start"


    def letter_incorrect(self):
        print(f'\nhelaas, de letter {self.gok} komt niet voor in het woord')
        self.aantal_gokken -= 1
        return "start"


    def check_woord(self):
        if self.gok == self.het_woord:
            return "woord_geraden"
        else:
            return "woord_incorrect"


    def woord_geraden(self):
        print(f"\nGefeliciteerd, je hebt het geraden!!! Het woord was '{self.het_woord}'")
        input("druk op een toests om af te sluiten")
        return "exit"


    def woord_incorrect(self):
        print(f'\nHelaas, pindakaas! {self.gok} is niet correct')
        self.aantal_gokken -= 1
        return "start"