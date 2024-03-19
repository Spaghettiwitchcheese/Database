import random
colors = ('A','B','C','D')

values = ('1','2','3','4', '5','6','7','8','9','10','j','Q','k')

deck = []

for x in range(len(colors)):
    for y in range(len(values)):
        deck.append(colors[x]+values[y])
print(deck)
print(len(deck))

tmp = 0 

random.shuffle(deck)

print(deck)


deck.remove[0,1]