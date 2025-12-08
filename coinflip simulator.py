import random

current = 0
times = 0

while current != 20:
    times+=1
    if random.randint(0,1) == 0:
     current+=1
    else:
     current=0

print(times)