import galgje3
import re

with open('galgje_woorden.txt', mode='r', encoding='utf8') as f:
    tekst = f.read()

woorden = re.findall('\\b[a-zA-Z]+\\b', tekst)
woordenlijst = []

for woord in woorden:
    if len(woord) < 5:
        continue
    
    if woord not in woordenlijst:
        woordenlijst.append(woord)
 
galgje = galgje3.Galgje(woordenlijst, 5)
galgje.speel()

 
