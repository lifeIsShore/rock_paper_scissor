import random as r

def rps(you):

    comp= r.choice(["rock","paper","scissor"])    
    if comp == "rock" and you == "paper":
        print("you win","comp = ",comp,",you = ",you)
    elif comp == you:
        print("draw","comp = ",comp,",you = ",you)
    elif comp == "paper" and you == "paper":
        print("you win","comp = ",comp,",you = ",you)
    elif comp == "scissor" and you == "rock":
        print("you win","comp = ",comp,",you = ",you)
    else:
        print("you lost","comp = ",comp,",you = ",you)

while True:
    you = input("pls type your choice if you want to leave type 0")
    if you == "rock":
        rps(you)
    elif you == "paper":
        rps(you)
    elif you == "scissor":
        rps(you)
    elif you == "0":
        break
    else:
        print("pls type one of them: paper, rock, scissor")