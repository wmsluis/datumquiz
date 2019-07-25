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
        print("De volgende datums vallen in een jaar altijd op dezelfde weekdag:")
        print("    - 4 apr, 6 jun, 8 aug, 10 okt, 12 dec  (denk aan x van x-de maand)")
        print("    - 9 mei, 5 sep                         (denk aan werktijden 9-to-5)")
        print("    - 7 nov, 11 jul                        (denk aan de winkel 7/11)")
        print("    - 0 mrt                                (de dag voor 1 mrt)")
        print("    - 0 feb, 3 jan, echter:")
        print("    - 1 feb, 4 jan voor schrikkeljaren")
        print("Nummer de weekdagen als volgt: zo=0, ma=1, di=2, wo=3, do=4, vr=5, za=6 en reken modulo 7.")
        print("    - het jaar 19jj heeft dag: 3 + jj + jj/4 (deling afronden naar beneden)")
        print("    - het jaar 20jj heeft dag: 2 + jj + jj/4")
        print("Bijvoorbeeld, op welke dag valt 5 mei 1945?")
        print("    1945 heeft dag: 3 + 45 + 45/4 = 3 + 45 + 11 = 59 = 3 (mod 7) = wo")
        print("    Dus 9 mei valt op 3 (met andere woorden, -6)")
        print("    Dus 5 mei valt op 5-6=-1=6=za.")
        return "get_antwoord"

