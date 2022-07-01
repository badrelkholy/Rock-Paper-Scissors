# This is a rock-paper-scissor game

import random

choiceList = ["Rock","Paper", "Scissors"]
comp_choice = random.choice(choiceList)

print("\n\nHello and welcome to the ulitmate rock-paper-scissor game.\n\n")

def help_mssg():
    print("""To play this game, choose from either of these choices and the computer will play a random choice:\n
            1.) To choose rock type in "r"
            2.) To choose paper type in "p"
            3.) To choose scissors type in "s"
            4.) To quit the game type in "q"\n""")

while True:
    help_mssg()
    ans = input("Choose a suitable option: ")
    
    if ans == "r":
        ans = "Rock"
        print(f"\nYou chose: {ans}\nComputer chose: {comp_choice}")
        if comp_choice == "Rock":
            print("\nYou have tied with the computer!\n")
        elif comp_choice == "Paper":
            print("\nThe computer has beaten you\n")
        elif comp_choice == "Scissors":
            print("\nYou have beaten the computer!\n")

    elif ans == "p":
        ans = "Paper"
        print(f"\nYou chose: {ans}\nComputer chose: {comp_choice}")
        if comp_choice == "Rock":
            print("\nYou have beaten the computer!\n")
        elif comp_choice == "Paper":
            print("\nYou have tied with the computer!\n")
        elif comp_choice == "Scissors":
            print("\nThe computer has beaten you\n")

    elif ans == "s":
        ans = "Scissors"
        print(f"\nYou chose: {ans}\nComputer chose: {comp_choice}")
        if comp_choice == "Rock":
            print("\nThe computer has beaten you!\n")
        elif comp_choice == "Paper":
            print("\nYou have beaten the computer!\n")
        elif comp_choice == "Scissors":
            print("\nYou have tied with the computer\n")
    
    elif ans == "q":
        print("""\nThank you for playing the game. Hope you enjoyed it and don't forget to play again.\n\nFor any problems please contact belkholy3648@gmail.com\n""")
        exit()
        
    else:
        print("\n*WARNING* The option you chose is not a suitable answer.\n")
