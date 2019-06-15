#!/usr/bin/python

# willem sluis
# 5 jan 2012

# quiz waarbij vragen bestaan uit het raden van de weekdag 
# van een random gegenereerde datum

import datetime
import argparse
import datumquiz

parser = argparse.ArgumentParser(description="Start de Datum Quiz")
parser.add_argument("-y", "--year", 
                    type = int,
                    default = datetime.date.today().year,
                    help="start jaar")
parser.add_argument("-c", "--count", 
                    type = int,
                    default = 1, 
                    help = "aantal jaren")

args = parser.parse_args()

quiz = datumquiz.DatumQuiz(args.year, args.count)
quiz.play()
