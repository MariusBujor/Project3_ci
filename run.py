import os 
import time


def clear_console():

    """ Clear the console. """

    os.system('cls' if os.name == 'nt' else 'clear')


def choose_play():

    """ Prints message and ask for user input """

    print("Are you ready to start \n   THE MAZE GAME ? \n    (Y or N) ")

    while True:

        answer = input("Type you choice : \n>> ")
        if answer.lower() != 'y' and answer.lower() != 'n':
            print("Incorrect answer.")

        else:

            return answer.lower()


def intro_game():

    """ Prints message and ask for user input """ 
    print("What is your name ?")

    while True:

        answer = input(">> ")
        if answer.strip() == '':
            print("Name cannot be empty!")

        else:

            return answer.capitalize()


def level_one():

    """ Prints message and ask for user input """

    print("We are searching your name in our data base...")
    print("SEARCHING...")
    print("Results confirms that this is your life history...")
    print("You have been born in a Robots world and during the time you")
    print("fight to survive and find freedom that is in a parallel world.")
    print("Unfortunately our data base confirms,")
    print("that  you are the only human that survived so far,")
    print("but finally you found  the secret secured Maze")
    print("The Maze is the pass between the Robots world and Normal world")
    print("If you succeed  you will be free in a normal world.")
    print("You are wakilng towords the entrance of the Maze.....")
    print("You arrived and you are realeasing that")
    print(" you need to choose between to dark ways..")
    print("One corridor on the Left and on corridor on Right")
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
    print("Good Choice ...")
    print("Are you scared ?....No worries..")
    print("There is no danger yet but you can hear the noise made")
    print("by the robots that are patroling in the maze , going forward you")
    print("arrived in front of one door of Red colour and one Lift")
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
    print("Good Choice ...")
    print("Are you scared?....No worries..")
    print("There is no danger yet but you can hear the noise made")
    print("by the robots that are patroling in the maze, going forward you")
    print("arrived in front of two colored doors : one Red and one Blue")
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
    print("Run forward to find the next two doors.")
    print("You are in front of the second door choice challange")
    print("What door you choose to open ? ")
    print("The Green or the White door")

    while True:

        answer = input("Type you choice :\nW or G : \n>> ")
        if answer.lower() != 'w' and answer.lower() != 'g':
            print("Incorrect answer!")

        else:

            return answer.lower()


def level_three():
    
    print("Good choice - You are so lucky !")
    print("Running forword you found the next two doors that are black.")
    print("On each door is a number...1...and...2.")

    while True:

        answer = input("Type you choice :\n1 or 2 : \n>> ")
        if answer != '1' and answer != '2':
            print("Incorrect answer!")

        else:

            return answer


def level_four():

    print("Good choice - You are so lucky!")
    print("Run forward to find the last challange.")
    print("You are in front of the last door...that has a panel new to it")
    print("Panel has three options from where  you need to chose only one")
    print("It has one wire / one emergency glass button/ and a switch")
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
    print("Seems that you took a wrong choice")
    print("All robots are coming towards you")
    print("No way to escape")
    print("You meet one of the robots but you did not")
    print("had any chance againts and you have been killed")
    print("Game over!")
    print("Do you want to start again?")
    start_again = input("Y or N\n>> ").lower().strip()

    if start_again == "y":
        start()

    else:

        end()


def end():

    clear_console()
    print("Sorry to see you leaving. Hope you enjoyed the game.")

    quit()


def start():

    '''Start the  Game'''

    print("?????????????????????????????????????????????????????????????????")
    print("?????????????????????????????????????????????????????????????????")
    print("??  ? ??? ?  ????????  ?  ????????             ????           ???")
    print("??  ?? ? ??  ???????  ???  ????????????????  ??????  ????????????")
    print("??  ??? ???  ??????  ?????  ??????????????  ???????  ????????????")
    print("??  ??? ???  ?????  ???????  ???????????  ?????????           ???")
    print("??  ???????  ????             ????????  ???????????  ????????????")
    print("??  ???????  ???  ???????????  ?????  ?????????????  ????????????")
    print("??  ???????  ??  ?????????????  ??              ???           ???")
    print("?????????????????????????????????????????????????????????????????")
    print("?????????????????????????????????????????????????????????????????")

    play = choose_play()

    print("Welcome my soldier...")
    if play == "n":
        print("Freedom is on the other side of THE MAZE.")
        print("Try again when you are ready !")
        game_over()
        return

    username = intro_game()

    print(" ----------  "f"Welcome {username}""  ---------- ")

    option_one = level_one()

    if option_one == "l":
        l = left_side()
        if l == 'r':
            game_over()
            return
    else:
        r = right_side()
        if r == 'l':
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
    # option_four() = level_four()

    # if option_four == "c" or option_four == "b":
    #     game_over()
	# 	return
        
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("-----------------YOU WIN THE GAME ---------------------------")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    print("             Congratulations  "f"{username}""  !!!! ")
    print("-------------------YOU ARE FREE------------------------------")

start()

