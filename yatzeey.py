import random
from collections import Counter

current_dice = [0,0,0,0,0,0]

index_to_roll= [0,1,2,3,4,5]

def roll(to_roll):
    for i in to_roll:
        current_dice[i] = random.randint(1,6)
    global index_to_roll
    index_to_roll= [0,1,2,3,4,5]

roll(index_to_roll)
to_go_for = Counter(current_dice).most_common(1)[0][0]
print(to_go_for)
