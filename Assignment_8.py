"""  Write a Python program to make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of
congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock"""


#game rules
print("*ROCK-PAPER-SCISSOR GAME*")
print("__________________________")

print("Game rules are:")
print("Rock beats scissors")
print("Scissors beats paper")
print("Paper beats rock")
print("------------------------")

while True:

    choiceplyr1= str(input("Player1: type your choice: "))

    choiceplyr2= str(input("Player2: type your choice: "))
    print("_______________________________")
    print("Choice of player 1:",choiceplyr1)
    print("Choice of payer 2:",choiceplyr2)
    print("_______________________________")


    if choiceplyr1 == "rock" and choiceplyr2 =="scissors":
        print("CONGARTULATIONS*_*Winner is Player 1")
        print("")
        option = str(input("Do you want to play againType 'yes' to continue and 'no' to stop.?"))
        if option== "no":
            break
    elif choiceplyr1 == "rock" and choiceplyr2 == "paper":
        print("CONGARTULATIONS*_*Winner is Player 2")
        print("")
        option = str(input("Do you want to play again?Type 'yes' to continue and 'no' to stop."))
        if option == "no":
            break
    elif choiceplyr1 == "scissors" and choiceplyr2 == "rock":
        print("CONGARTULATIONS*_*Winner is Player 2")
        print("")
        option = str(input("Do you want to play again?Type 'yes' to continue and 'no' to stop."))
        if option == "no":
            break
    elif choiceplyr1 == "scissors" and choiceplyr2 =="paper":
        print("CONGARTULATIONS*_*Winner is Player 1")
        print("")
        option = str(input("Do you want to play again?Type 'yes' to continue and 'no' to stop."))
        if option == "no":
            break
    elif choiceplyr1 == "paper" and choiceplyr2 == "scissors":
        print("CONGARTULATIONS*_*Winner is Player 2")
        print("")
        option = str(input("Do you want to play again?Type 'yes' to continue and 'no' to stop."))
        if option == "no":
            break
    elif choiceplyr1 == "paper" and choiceplyr2 == "rock":
        print("CONGARTULATIONS*_*Winner is Player 1")
        print("")
        option = str(input("Do you want to play again?Type 'yes' to continue and 'no' to stop."))
        if option == "no":
            break
    elif choiceplyr1 == choiceplyr2:
        print("Same choice, no one wins..")
        print("")
        option = str(input("Do you want to play again? Type 'yes' to continue and 'no' to stop."))
        if option == "no":
            break



