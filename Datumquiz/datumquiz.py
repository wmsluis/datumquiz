import time
import datetime
import random
import sys
import calendar

class DatumQuiz(object):
    """toon een datum en laat de gebruiker de dag van de week berekenen"""

    def __init__(self, startyear, yearcnt):
        #self.weekdays = [x.lower() for x in calendar.day_abbr]
        #self.weekdays.insert(0, self.weekdays.pop(6))
        self.weekdays = ['zo','ma','di','wo','do','vr','za']
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
        self.correct_antwoord = self.weekdays[int(datum.strftime("%w"))]
        print("Op welke dag valt %s?" % datum.strftime("%d %b %Y"))
        self.vraag_cnt += 1
        return "get_antwoord"
    
    def get_antwoord(self):
        invoer = input(", ".join(self.weekdays) + " of druk op x om te stoppen: ").lower()
        if not invoer:
            return "get_antwoord"

        if invoer[0].lower() in 'xq':
            return "stoppen"
        
        if invoer[0].lower() in 'h':
            return "hint"

        if not invoer in self.weekdays:
            return "invoer_incorrect"
               
        if invoer == self.correct_antwoord:
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
        print("  x/x:    4 apr, 6 jun, 8 aug, 10 oct, 12 dec")
        print("  5-to-9: 5 sep, 9 mei")
        print("  7/11:   7 nov, 11 jul")
        print("          0 maa")
        print("          0 feb (1 feb in schrikkeljaar)")
        print("          3 jan (4 jan in schrikkeljaar)")
        print("jaardag = eeuwdag + jaar + jaar / 4 (naar beneden afgerond) ")
        print("eeuwdag: 1900=3, 2000=2")
        return "get_antwoord"

