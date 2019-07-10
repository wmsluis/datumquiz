import time
import datetime
import random
import sys
import calendar

class DatumQuiz(object):
    """toon een datum en laat de gebruiker de dag van de week berekenen"""

    def __init__(self, startyear, yearcnt):
        self.weekdays = [x for x in calendar.day_abbr]
        self.weekdays.insert(0, self.weekdays.pop(6))
        self.dateStart = datetime.date(startyear, 1, 1)
        dateEnd = datetime.date(startyear + yearcnt, 1, 1)
        self.daycnt = (dateEnd - self.dateStart).days
        self.vraag_cnt = 0
        self.correct_cnt = 0
        self.starttijd = datetime.datetime.now()
        
    def play(self):
        # een finite-state machine 
        # de toestand is een string waar ook een methode voor bestaat
        # iedere methode geeft een string terug met de naam van de volgende toestand
        toestand = "stel_vraag"
        while toestand != "afsluiten":
            actie = getattr(self, toestand)
            toestand = actie()
            
    def stel_vraag(self):
        d = random.randint(0, self.daycnt)
        datum = self.dateStart + datetime.timedelta(days=d)
        self.correct_antwoord = datum.strftime("%a")
        print("Op welke dag valt %s?" % datum.strftime("%d %b %Y"))
        self.vraag_cnt += 1
        return "get_antwoord"
    
    def get_antwoord(self):
        invoer = input("(zo=0, ma=1, di=2, wo=3, do=4, vr=5, za=6 of druk op x om te stoppen): ")
        if not invoer:
            return "get_antwoord"

        if invoer[0].lower() in 'xq':
            return "stoppen"
        
        if invoer[0].lower() in 'h':
            return "hint"

        if not invoer.isdigit():
            return "invoer_incorrect"
               
        antwoord = int(invoer)
        if antwoord > 6:
            return "invoer_incorrect"
                    
        if self.weekdays[antwoord] == self.correct_antwoord:
            self.correct_cnt += 1
            print("Correct\n")
            return "stel_vraag"
        else:
            self.vraag_cnt += 1
            print("Niet correct, probeer opnieuw ...")
            return "get_antwoord"
            
    def invoer_incorrect(self):
        print("Incorrecte invoer, probeer het opnieuw")
        return "get_antwoord"
    
    def stoppen(self):
        self.vraag_cnt -= 1
        if self.vraag_cnt > 0:
            print("aantal vragen : %d" % self.vraag_cnt)
            print("correct       : %d" % self.correct_cnt        )
            tijdgebruikt = (datetime.datetime.now() 
                            - self.starttijd).seconds / self.vraag_cnt
            print("tijd per vraag: %.1f" % tijdgebruikt)
        return "afsluiten" 

    def hint (self):
        """toon een hint"""
        print("weekdag = datum + jaardag - maanddag")
        print("maanddag:")
        print("  x/x:    4 april, 6 juni, 8 augustus, 10 october, 12 december")
        print("  5-to-9: 5 september, 9 mei")
        print("  7/11:   7 november, 11 juli")
        print("          2 januari, 6 februari (van het voorliggende jaar)")
        print("jaardag = eeuwdag + jaar + jaar / 4 (naar beneden afgerond) ")
        print("eeuwdag: 1900=3, 2000=2")
        return "get_antwoord"
