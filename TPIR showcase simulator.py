import random
import csv_export

iterations = 5000

def simulatorRound():
    spin1 = random.randint(1,20)
    spin1 = spin1 * 5
    print (spin1)

for count in range (iterations):
    simulatorRound()
