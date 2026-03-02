import random
import csv_export

iterations = 50000
risk = 0

currentIteration = 1
spinResults = []
labels = []
countedReslults = []
spin1 = 0
spin2 = 0
total = 0

def simulateRound():
    spin1 = random.randint(1,20)
    spin1 = spin1 * 5
    spin2 = 0
    if spin1 <= risk and not spin1 == 100:
        spin2 = random.randint(1,20)
        spin2 = spin2 * 5
    total = spin1 + spin2
    if total > 100:
        total = 0
    spinResults.append(total)

for j in range(18,20):
    spinResults = []
    labels = []
    countedReslults = []
    risk = j*5
    for i in range (iterations):
        simulateRound()

    for i in range(21):
        toTrack = i * 5
        labels.append(toTrack)
        countedReslults.append(spinResults.count(toTrack))

    csv_export.export_to_csv(f"results{j*5}.csv",labels,countedReslults)
