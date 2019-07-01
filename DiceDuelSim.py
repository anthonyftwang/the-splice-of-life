#Dice Duel simulator for an original board game concept

import random

#Set P1HasCard and P2HasCard accordingly. (game mechanic that allows 2 attempts)

P1HasCard = True
P2HasCard = True

P1WinCount = 0
tieCount = 0
P2WinCount = 0
errorCount = 0 #for debugging

N = int(input("Enter the number of rounds to simulate. (e.g. 100000): "))

for i in range(0,N):

    #P1 roll for sum

    if P1HasCard == False:
        P1A = random.randint(0,6)
        P1B = random.randint(0,6)
        P1Sum = P1A + P1B

    if P1HasCard == True:
        P1A = random.randint(0,6)
        P1B = random.randint(0,6)
        P1SumAB = P1A + P1B
        P1C = random.randint(0,6)
        P1D = random.randint(0,6)
        P1SumCD = P1C + P1D
        if P1SumCD > P1SumAB:
            P1Sum = P1SumCD
        else:
            P1Sum = P1SumAB

    #P2 roll for sum
    
    if P2HasCard == False:
        P2A = random.randint(0,6)
        P2B = random.randint(0,6)
        P2Sum = P2A + P2B
    
    if P2HasCard == True:
        P2A = random.randint(0,6)
        P2B = random.randint(0,6)
        P2SumAB = P2A + P2B
        P2C = random.randint(0,6)
        P2D = random.randint(0,6)
        P2SumCD = P2C + P2D
        if P2SumCD > P2SumAB:
            P2Sum = P2SumCD
        else:
            P2Sum = P2SumAB

    #Compare sums

    if P1Sum > P2Sum:
        P1WinCount += 1
    elif P1Sum < P2Sum:
        P2WinCount += 1
    elif P1Sum == P2Sum:
        tieCount += 1
    else:
        errorCount += 1

print()
print("P1 Wins:", P1WinCount)
print("Ties:", tieCount)
print("P2 Wins:", P2WinCount)
print("Errors:", errorCount)
print()
print("Total simulated rounds:", N)
