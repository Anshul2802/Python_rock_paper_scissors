import random

list = ['rock', 'paper', 'scissors']
win = {'rock': 'scissors', 'paper':'rock','scissors':'paper'}
i= 0
j=0

for q in range(1, 4):
    print(f"Round Number: {q}")
    picked = input("Pick Rock, Paper or Scissors: ")
    randon_item = random.choice(list)
    print("Computer picks: ", randon_item)
    if picked == randon_item:
        print("It's a Draw!")
    elif win[picked] == randon_item:
        print("You Win!")
        i += 1
    else:
        print("You Lose!")
        j += 1


print("Your Score: ",i)
print("Computer Score: ",j)

if i>j:
    print("You win the game!")
elif i<j:
    print("Computer wins the game!")
else:
    print("It's a draw!")