import galgje3
import re

with open('galgje_woorden.txt', 'r', encoding='utf8', errors='ignore') as w:
    tekst = w.read()
    woorden = re.findall('\s[a-z]+', tekst)
    woordenlijst = []

    for woord in woorden:
        woord = woord.strip(' ')
        if len(woord) > 4:
            if woord not in woordenlijst:
                woordenlijst.append(woord)
        else:
            continue


galgje = galgje3.Galgje(woordenlijst)
galgje.speel()

 