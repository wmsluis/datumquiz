#!/usr/bin/python3

# quiz waarbij vragen bestaan uit het noemen van een datum
# en de gebruiker de weekdag moet raden / berekenen.

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

