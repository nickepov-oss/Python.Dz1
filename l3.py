import random

def game(choice, result):
    print("")
    print("=====Start Game rock, paper, scissors=====")
    computer_choice = random.choice("rps")
    print("--------------------------------")
    print("Your select – ",
          str.capitalize(choice))
    print("Computer select —",
          str.capitalize(computer_choice))
    if str.lower(choice) == computer_choice:
        print("Result of game – Draw")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "r" and computer_choice == "p":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "r" and computer_choice == "s":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "p" and computer_choice == "s":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
     elif str.lower(choice) == "p" and computer_choice == "r":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "s" and computer_choice == "r":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "s" and computer_choice == "p":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")


result = {"computer": 0, "player": 0}
choise = input("Select R / P / S – ")
game(choice=choise, result=result)
