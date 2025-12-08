import random


current = 0
times = 0
increment = 1
target = 30

while increment < target+1:
    while current !=increment:
        times+=1
        if random.randint(0,1) == 0:
            current+=1
        else:
            current=0
    print(times , "at" , increment)
    increment+=1
    times = 0
    current = 0