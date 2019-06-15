import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", 
                    type=int, 
                    help = "display square of an integer")
parser.add_argument("-v", "--verbose", 
                    help="increase output verbosity",
                    action = "count",
                    default = 0)

args = parser.parse_args()

answer = args.square ** 2

if args.verbose >= 2:
    print "the square of {} is {}".format(args.square, answer)
elif args.verbose >= 1:
    print "{}^2 = {}".format(args.square, answer)
else:
    print answer

