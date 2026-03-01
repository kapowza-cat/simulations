import random
import csv_export

iterations = 5000
spinResults = []
currentIteration = 1

def simulateRound():
    spin1 = random.randint(1,20)
    spin1 = spin1 * 5
    spinResults.append(spin1)

for i in range (iterations):
    simulateRound()

csv_export.export_to_csv("test.csv",spinResults)
