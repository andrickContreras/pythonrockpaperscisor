import random, sys

win = 0
losses = 0
ties = 0
# 1 = Rock
# 2 = Paper
# 3 = Scissors


print("ROCK, PAPER, SCISSORS")

while losses <= 3 or win >= 3 or ties >= 3:
    print("Enter, your move: (r)ock (p)aper (s)cissors or (q)uit")
    playerInput = input()
    enemyMovement = random.randint(1,3)
    if playerInput == 'q':
        sys.exit()
    elif(losses == 3):
        print("Sorry, better luck NEXT TIME")
        sys.exit()
    elif(win == 3):
        print("Congrats, YOU WON")
        sys.exit()
    elif(ties == 3):
        print("SORRY, TRY AGAIN")
        sys.exit()
    elif playerInput == "r" and enemyMovement == 1:
        print("Tie")
        ties = ties + 1
    elif playerInput == "p" and enemyMovement == 1:
        print("Congrats, you win")
        win = win + 1
    elif playerInput == "s" and enemyMovement == 1:
        print("Sorry, you lose")
        losses = losses + 1
    elif playerInput == "p" and enemyMovement == 2:
        print("Tie")
        ties = ties + 1
    elif playerInput == "r" and enemyMovement == 2:
        print("Sorry, you lose")
        losses = losses + 1 
    elif playerInput == "s" and enemyMovement == 2:
        print("Congrats, you win")
        win = win + 1
    elif playerInput == "s" and enemyMovement == 3:
        print("Tie")
        ties = ties + 1
    elif playerInput == "p" and enemyMovement == 3:
        print("Sorry, you lose")
        losses = losses + 1 
    elif playerInput == "r" and enemyMovement == 3:
        print("Congrats, you win")
        win = win + 1
    print(win)
    print(losses)
    print(ties)
