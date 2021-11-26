import os

import time

# Time value

a = 0.2
b = 2
c = 4


def clear_console():
    """ Clear the console. """

    os.system('cls' if os.name == 'nt' else 'clear')


def choose_play():
    """ Prints message and ask for user input """

    print("Are you ready to start \n   THE MAZE GAME ? \n    (Y or N) ")
    time.sleep(b)

    while True:

        answer = input("Type you choice : \n>> ")
        if answer.lower() != 'y' and answer.lower() != 'n':
            print("Incorrect answer.")

        else:

            return answer.lower()


def intro_game():
    """ Prints message and ask for user input """
    time.sleep(b)
    print("What is your name ?")

    while True:

        answer = input(">> ")
        if answer.strip() == '':
            print("Name cannot be empty!")

        else:

            return answer.capitalize()


def level_one():
    """ Prints message and ask for user input """

    print()
    print("We are searching your name in our data base...")
    time.sleep(c)
    print()
    print("SEARCHING...")
    print()
    time.sleep(c)
    print("Results confirms that this is your life history...")
    time.sleep(b)
    print()
    print("You have been born in a Robots world and during the time you")
    time.sleep(b)
    print("fight to survive and find freedom that is in a parallel world.")
    time.sleep(b)
    print("Unfortunately our data base confirms,")
    print("that  you are the only human that survived so far,")
    time.sleep(b)
    print("but finally you found  the secret secured Maze")
    time.sleep(b)
    print("The Maze is the pass between the Robots world and Normal world")
    time.sleep(b)
    print("If you succeed  you will be free in a normal world.")
    time.sleep(b)
    print("You are wakilng towords the entrance of the Maze.....")
    time.sleep(b)
    print("You arrived and you are realeasing that")
    time.sleep(b)
    print("you need to choose between to dark ways..")
    time.sleep(b)
    print("One corridor on the Left and on corridor on Right")
    time.sleep(b)
    print("Wich way are you going...")

    while True:

        answer = input("Type you choice :\nL or R : \n>> ")
        if answer.lower() != 'l' and answer.lower() != 'r':
            print("Incorrect answer!")

        else:

            return answer.lower()


def right_side():
    """ Prints message and ask for user input """

    print("You choose Right ")
    time.sleep(b)
    print("Good Choice ...")
    time.sleep(b)
    print("Are you scared ?....No worries..")
    time.sleep(b)
    print("There is no danger yet but you can hear the noise made")
    time.sleep(b)
    print("by the robots that are patroling in the maze , going forward you")
    print("arrived in front of one door of Red colour and one Lift")
    time.sleep(b)
    print("You will need to chose carefully because behind")
    print("one of this options is a robot ready to kill you.")

    while True:

        answer = input("Type you choice :\nR or L : \n>> ")
        if answer.lower() != 'l' and answer.lower() != 'r':
            print("Incorrect answer!")
        else:

            return answer.lower()


def left_side():
    """ Prints message and ask for user input """
    print("You chose Left ")
    time.sleep(b)
    print("Good Choice ...")
    time.sleep(b)
    print("Are you scared?....No worries..")
    time.sleep(b)
    print("There is no danger yet but you can hear the noise made")
    print("by the robots that are patroling in the maze, going forward you")
    print("arrived in front of two colored doors : one Red and one Blue")
    time.sleep(b)
    print("You will need to chose carefully because behind")
    print("one of this doors there is a robot ready to kill you.")

    while True:

        answer = input("Type you choice :\nR or B : \n>> ")
        if answer.lower() != 'r' and answer.lower() != 'b':

            print("Incorrect answer!")

        else:

            return answer.lower()


def level_two():

    print("Good choice - You are so lucky!")
    time.sleep(b)
    print("Run forward to find the next two doors.")
    time.sleep(b)
    print("You are in front of the second door choice challange")
    time.sleep(b)
    print("What door you choose to open ? ")
    time.sleep(b)
    print("The Green or the White door")

    while True:

        answer = input("Type you choice :\nW or G : \n>> ")
        if answer.lower() != 'w' and answer.lower() != 'g':
            print("Incorrect answer!")

        else:

            return answer.lower()


def level_three():

    print("Good choice - You are so lucky !")
    time.sleep(b)
    print("Running forword you found the next two doors that are black.")
    time.sleep(b)
    print("On each door is a number...1...and...2.")

    while True:

        answer = input("Type you choice :\n1 or 2 : \n>> ")
        if answer != '1' and answer != '2':
            print("Incorrect answer!")

        else:

            return answer


def level_four():

    print("Good choice - You are so lucky!")
    time.sleep(b)
    print("Run forward to find the last challange.")
    time.sleep(b)
    print("You are in front of the last door...that has a panel new to it")
    time.sleep(b)
    print("Panel has three options from where  you need to chose only one")
    time.sleep(b)
    print("It has one wire / one emergency glass button/ and a switch")
    time.sleep(b)
    print("What is your choice cut the wire ,")
    print("break the glass or turn the switch ?")

    while True:

        answer = input("Type you choice :\nC, B or T : \n>> ")
        if answer.lower() != 'c' and answer.lower() != 'b' and answer.lower() != 't':
            print("Incorrect answer!")
        else:
            return answer.lower()


def game_over():
    """ Prints message and ask for user input """

    clear_console()

    print("!!!!!!!! ALARM !!!!!!!!!!")
    time.sleep(b)
    print("Seems that you took a wrong choice")
    time.sleep(b)
    print("All robots are coming towards you")
    print("No way to escape")
    time.sleep(b)
    print("You meet one of the robots but you did not")
    time.sleep(b)
    print("had any chance againts and you have been killed")
    time.sleep(b)
    print("Game over!")
    time.sleep(b)
    print("Do you want to start again?")
    time.sleep(b)
    start_again = input("Y or N\n>> ").lower().strip()

    if start_again == "y":
        start()

    else:

        end()


def end():

    clear_console()
    print("Sorry to see you leaving. Hope you enjoyed the game.")

    quit()


def start(repeat=False):
    """Start the  Game. If is first time, repeat is default on False"""

    if not repeat:
        time.sleep(a)
        print("?????????????????????????????????????????????????????????????????")
        time.sleep(a)
        print("?????????????????????????????????????????????????????????????????")
        time.sleep(a)
        print("??  ? ??? ?  ????????  ?  ????????             ????           ???")
        time.sleep(a)
        print("??  ?? ? ??  ???????  ???  ????????????????  ??????  ????????????")
        time.sleep(a)
        print("??  ??? ???  ??????  ?????  ??????????????  ???????  ????????????")
        time.sleep(a)
        print("??  ??? ???  ?????  ???????  ???????????  ?????????           ???")
        time.sleep(a)
        print("??  ???????  ????             ????????  ???????????  ????????????")
        time.sleep(a)
        print("??  ???????  ???  ???????????  ?????  ?????????????  ????????????")
        time.sleep(a)
        print("??  ???????  ??  ?????????????  ??              ???           ???")
        time.sleep(a)
        print("?????????????????????????????????????????????????????????????????")
        time.sleep(a)
        print("?????????????????????????????????????????????????????????????????")
        time.sleep(b)
        clear_console()

    play = choose_play()

    if play == "n":
        print("Freedom is on the other side of THE MAZE.")
        time.sleep(b)
        print("Try again when you are ready !")
        time.sleep(b)
        end()
        return

    print("Welcome my soldier...")

    username = intro_game()
    print()
    print(" ----------  "f"Welcome {username}""  ---------- ")

    option_one = level_one()

    if option_one == "l":
        left = left_side()
        if left == 'r':
            game_over()
            return
    else:
        right = right_side()
        if right == 'l':
            game_over()
            return

    option_two = level_two()

    if (option_one == "l" and option_two == "w") or (
            option_one == "r" and option_two == "g"):
        game_over()
        return

    option_three = level_three()

    if (option_one == "l" and option_three == "2") or (
            option_one == "r" and option_three == "1"):
        game_over()
        return

    option_four = level_four()

    if option_four == "c" or option_four == "b":
        game_over()
        return

    time.sleep(a)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    time.sleep(a)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    time.sleep(a)
    print("-----------------YOU WIN THE GAME ---------------------------")
    time.sleep(a)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    time.sleep(a)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    time.sleep(b)

    print("             Congratulations  "f"{username}""  !!!! ")
    time.sleep(b)
    print("-------------------YOU ARE FREE------------------------------")
    start(True)


start()
