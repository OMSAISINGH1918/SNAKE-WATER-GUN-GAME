import random
list=["s","w","g"]

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t SNAKE, WATER, GUN GAME 🐍🌊🔫\n \n")
print("s for snake \n w for water \n g for gun \n")

while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(list)

    if _input==_random:
        print ("YOU AND COMPUTER SELECTED THE SAME THEREFORE NO POINTS \n")

    # if user enters s
    if _input=="s" and _random=="g":
        computer_point=computer_point+1
        print ("YOU SELECTED",_input,"AND THE COMPUTER SELECTED",_random,"\n")
        print("YOU GET 0  POINT AS THE SNAKE WAS SHOT \n")
        print("COMPUTER'S POINT IS",computer_point, "AND YOUR POINT IS",human_point,"\n ")

    elif _input == "s" and _random == "w":
            human_point = human_point + 1
            print("YOU SELECTED", _input, "AND THE COMPUTER SELECTED", _random, "\n")
            print("YOU GET 1 POINT AS THE SNAKE DRANK WATER \n")
            print("COMPUTER'S POINT IS", computer_point, "AND YOUR POINT IS", human_point, "\n ")

            #if user enters w

    elif _input == "w" and _random == "g":
            human_point = human_point + 1
            print("YOU SELECTED", _input, "AND THE COMPUTER SELECTED", _random, "\n")
            print("YOU GET 1 POINT AS THE GUN WENT IN WATER \n")
            print("COMPUTER'S POINT IS", computer_point, "AND YOUR POINT IS", human_point, "\n ")

    elif _input == "w" and _random == "s":
            computer_point = computer_point + 1
            print("YOU SELECTED", _input, "AND THE COMPUTER SELECTED", _random, "\n")
            print("YOU GET 0 POINT AS SNAKE DRANK THE WATER \n")
            print("COMPUTER'S POINT IS", computer_point, "AND YOUR POINT IS", human_point, "\n ")

    elif _input == "g" and _random == "s":
            human_point = human_point + 1
            print("YOU SELECTED", _input, "AND THE COMPUTER SELECTED", _random, "\n")
            print("YOU GET 1 POINT AS THE YOU SHOT THE SNAKE \n")
            print("COMPUTER'S POINT IS", computer_point, "AND YOUR POINT IS", human_point, "\n ")

    elif _input == "g" and _random == "w":
            human_point = human_point + 1
            print("YOU SELECTED", _input, "AND THE COMPUTER SELECTED", _random, "\n")
            print("YOU GET 0 POINT AS YOUR GUN WENT IN WATER \n")
            print("COMPUTER'S POINT IS", computer_point, "AND YOUR POINT IS", human_point, "\n ")

    else:
        print("YOU HAVE GIVEN WRONG INPUT \n")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point > human_point:
    print("COMPUTER WINS AND YOU LOOSE")

if computer_point < human_point:
    print("YOU WIN AND COMPUTER LOOSES")

print ("THANKS FOR PLAYING THE 🐍🌊🔫 GAME")
print ("© OMSAI SINGH")












