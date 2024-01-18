import random
from random import randint as r
import time


attempts_list_randomgame = []
# --------------------------------
win_list_rolldices = []
lose_list_rolldices = []
draw_list_rolldices = []
# --------------------------------
win_list_RCB = []
# --------------------------------
win_list_bingo = [0]
lose_list_bingo = [0]
ran_nums_bingo = []

n = r(1,10)

print("Welcome to MultiTool by GodJiy!")

choice_program = float(input("\n Games: \n 1.1 - RandomGame \n 1.2 - RollDices \n 1.3 - RSP \n 1.4 - Bingo! \n  \n Actions with list(NOT WORKING): \n 2.1 - AVGlist \n 2.2 - DuplicateCounterList \n 2.3 - IndexMaxNumberList \n 2.4 - TwoIndexMaxNumberList \n 2.5 - UniqueCountList \n  \n Calculators: \n 3.1 - Calculator \n 3.2 - TicketCalculator \n 3.3 - TipCalculator \n  \n Programs: \n 4.1 - ToDo \n 4.2 - SetNumbers \n  \n Funny Programs: \n 5.1 - 1000-7 \n"))

def RandomGameShowScore():
    if not attempts_list_randomgame:
        print('There is currently no high score.')
    else:
        print(f'The current high score is {min(attempts_list_randomgame)} attempts')

def RandomGame():
    num = random.randint(1, 100)
    attempts = 0
    print("Hello player! Welcome to RandomNumberGuessGame!")
    player_name = input("Enter your name: ")
    wanna_play = input(f"Hi, {player_name}, would you like to play the game? (Enter Yes/No): ")

    if wanna_play.lower() != "yes":
        print("That\'s cool, Thanks!")
        exit()
    else:
        RandomGameShowScore()

    while wanna_play.lower() == "yes":
        try:
            guess = int(input("Pick a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                raise ValueError("Please guess a number within the given range")

            attempts += 1
            attempts_list_randomgame.append(attempts)

            if guess == num:
                print("Nice! You got it!")
                print(f"It took you {attempts} attempts")
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("That\'s cool, have a good one!")
                    break
                else:
                    attempts = 0
                    num = random.randint(1,100)
                    RandomGameShowScore()
                    continue

            else:
                if guess > num:
                    print('It\'s lower')
                if num > guess:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no! That is not a valid value. Try again!')
            print(err)

def RollDicesShowScore():
    if not win_list_rolldices:
        print("You don't have wins!")
    if not draw_list_rolldices:
        print("You don't have draws!")
    if not lose_list_rolldices:
        print("You don't have loses!")
    else:
        print(f"Now you have {max(win_list_rolldices)} wins, {max(draw_list_rolldices)} draws, {max(lose_list_rolldices)} loses.")

def RollDices():
    wins = 0
    lose = 0
    draws = 0
    player_name = input("Enter your name: ")
    wanna_play = input(f"Hello {player_name}! Would you like to play RollDices? (Enter Yes/No): ")

    if wanna_play.lower() != "yes":
        print("That\'s cool, Thanks!")
        exit("Bye!")
    else:
        RollDicesShowScore()

    while wanna_play.lower() == "yes":
        try:
            die_1 = r(1,6)
            die_2 = r(1,6)
            sum_1 = die_1 + die_2
            if sum_1 > 12:
                raise ValueError("Oops, you rolled more than 12!")
            print("You rolled: ", sum_1)

            die_3 = r(1,6)
            die_4 = r(1,6)
            sum_2 = die_3 + die_4
            if sum_2 > 12:
                raise ValueError("Oops, enemy rolled more than 12!")
            print("Enemy rolled: ", sum_2)
            if sum_1 > sum_2:
                wins += 1
                win_list_rolldices.append(wins)
                print("Congratulate! You win!")
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("That\'s cool, Thanks!")
                    break
                else:
                    RollDicesShowScore()
                    continue
            if sum_2 > sum_1:
                lose += 1
                lose_list_rolldices.append(lose)
                print("You lose, don\'t give up. Try again!")
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("That\'s cool, Thanks!")
                    break
                else:
                    RollDicesShowScore()
                    continue
            if sum_1 == sum_2:
                draws += 1
                draw_list_rolldices.append(draws)
                print("Draw! Try again!")
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("That\'s cool, Thanks!")
                    break
                else:
                    RollDicesShowScore()
                    continue
        except ValueError as err:
            print('Error!')
            print(err)

def RCBShowScore():
    if not win_list_RCB:
        print("You currently don't have wins!")
    else:
        print("You have:",max(win_list_RCB), "wins!")

def RCB():
    wins = 0
    user_name = input("Enter your name: ")
    wanna_play = input(f"Hello {user_name}, do you want play? (Enter Yes/No): ")

    while wanna_play.lower() == "yes":
        try:
            if wanna_play.lower() != "yes":
                print("Okay, goodbye!")
                exit()
            if wanna_play.lower() == "yes":
                print(" Rock - 1 \n Scissors - 2 \n Paper - 3")
                choice = int(input("Enter your item: "))

            if choice < 1 or choice > 3:
                raise ValueError("Please, enter valid number")

            print(" ")

            if choice == 1:
                print(f"{user_name} choose rock")
            if choice == 2:
                print(f"{user_name} choose scissors")
            if choice == 3:
                print(f"{user_name} choose paper")

            pc_choice = r(1,3)

            if pc_choice == 1:
                print("PC choose rock")
            if pc_choice == 2:
                print("PC choose scissors")
            if pc_choice == 3:
                print("PC choose paper")

            print(" ")

            if pc_choice == 1 and choice == 3:
                print(f"{user_name} wins!")
                wins += 1
                win_list_RCB.append(wins)
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Ok, goodbye!")
                    break

                else:
                    pc_choice = r(1, 6)
                    RCBShowScore()
                    continue
            elif pc_choice == 2 and choice == 1:
                print(f"{user_name} wins!")
                wins += 1
                win_list_RCB.append(wins)
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Ok, goodbye!")
                    break

                else:
                    pc_choice = r(1, 6)
                    RCBShowScore()
                    continue
            elif pc_choice == 3 and choice == 2:
                print(f"{user_name} wins!")
                wins += 1
                win_list_RCB.append(wins)
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Ok, goodbye!")
                    break

                else:
                    pc_choice = r(1, 6)
                    RCBShowScore()
                    continue
            elif choice == 1 and pc_choice == 3:
                print("PC wins!")
                win_list_RCB.append(wins)
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Ok, goodbye!")
                    break

                else:
                    pc_choice = r(1, 6)
                    RCBShowScore()
                    continue
            elif choice == 2 and pc_choice == 1:
                print("PC wins!")
                win_list_RCB.append(wins)
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Ok, goodbye!")
                    break

                else:
                    pc_choice = r(1, 6)
                    RCBShowScore()
                    continue
            elif choice == 3 and pc_choice == 2:
                print("PC wins!")
                win_list_RCB.append(wins)
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Ok, goodbye!")
                    break

                else:
                    pc_choice = r(1, 6)
                    RCBShowScore()
                    continue
            elif choice == 1 and pc_choice == 1:
                print("Draw!")
                win_list_RCB.append(wins)
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Ok, goodbye!")
                    break

                else:
                    pc_choice = r(1, 6)
                    RCBShowScore()
                    continue
            elif choice == 2 and pc_choice == 2:
                print("Draw!")
                win_list_RCB.append(wins)
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Ok, goodbye!")
                    break

                else:
                    pc_choice = r(1, 6)
                    RCBShowScore()
                    continue
            if choice == 3 and pc_choice == 3:
                print("Draw!")
                win_list_RCB.append(wins)
                wanna_play = input("Would you like to play again? (Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Ok, goodbye!")
                    break

                else:
                    pc_choice = r(1, 6)
                    RCBShowScore()
                    continue
        except ValueError as err:
            print("Oh no! That is not valid value. Try again!")
            print(err)

def Bingo():

    wins = 0
    lose = 0

    player_name = input("Enter your name: ")
    wanna_play = input(f"Hello {player_name}, would you like to play? (Enter Yes/No): ")

    if wanna_play.lower() != "yes":
        print("Bye!")
        exit()

    while wanna_play.lower() == "yes":
        try:

            for i in range(n):
                ran_nums_bingo.append(r(1, 99))

            guess = int(input("Enter your number: "))

            if 1 > guess or guess > 99:
                raise ValueError("Enter valid number(1 to 99)")

            else:

                if guess in ran_nums_bingo:
                    print("You win!")
                    wins += 1
                    win_list_bingo.append(wins)
                    wanna_play = input("Would you like play again? (Enter Yes/No): ")

                    if wanna_play.lower() != "yes":
                        BingoShowScore()
                    if wanna_play.lower() == "yes":
                        BingoShowScore()
                        continue
                else:
                    print("You lose...")
                    lose += 1
                    lose_list_bingo.append(lose)
                    wanna_play = input("Would you like play again? (Enter Yes/No): ")

                    if wanna_play.lower() != "yes":
                        BingoShowScore()
                    if wanna_play.lower() == "yes":
                        BingoShowScore()
                        continue

        except ValueError as err:
            print("Error!")
            print(err)

def BingoShowScore():
    if not win_list_bingo:
        print("You don't have wins!")
    if not lose_list_bingo:
        print("You don't have loses!")
    else:
        print(f"You have {max(lose_list_bingo)} loses and {max(win_list_bingo)} wins.")

def Calculator():
    wanna_continue = input("Would you like continue? (Enter Yes/No): ")

    if wanna_continue.lower() != "yes":
        print("Okay, see you later!")
        exit()

    while wanna_continue.lower() == "yes":

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        symbol = input("Enter symbol(*,:,+,-): ")
        if symbol == "*":
            print("You selected multiply. Your result: ")
            result = num1 * num2
            print(result)
            wanna_continue = input("Would you like continue? (Enter Yes/No): ")

            if wanna_continue.lower() != "yes":
                print("Okay, see you later!")
                exit()
            else:
                continue

        if symbol == ":":
            print("You selected divide. Your result: ")
            result = num1 / num2
            print(result)
            wanna_continue = input("Would you like continue? (Enter Yes/No): ")

            if wanna_continue.lower() != "yes":
                print("Okay, see you later!")
                exit()
            else:
                continue

        if symbol == "+":
            print("You selected plus. Your result: ")
            result = num1 + num2
            print(result)
            wanna_continue = input("Would you like continue? (Enter Yes/No): ")

            if wanna_continue.lower() != "yes":
                print("Okay, see you later!")
                exit()
            else:
                continue

        if symbol == "-":
            print("You selected minus. Your result: ")
            result = num1 - num2
            print(result)
            wanna_continue = input("Would you like continue? (Enter Yes/No): ")

            if wanna_continue.lower() != "yes":
                print("Okay, see you later!")
                exit()
            else:
                continue

def TicketCalculator():

    wanna_continue = input("Would you like continue?(Enter Yes/No): ")

    if wanna_continue.lower() != "yes":
        print("Okay, see you later!")
        exit()

    while wanna_continue.lower() == "yes":

        count_peoples = int(input("How much peoples: "))
        price_ticket = int(input("How much ticket cost: "))
        kid_peoples = input("Do you have children?(Enter Yes/No): ")
        if kid_peoples.lower() == "yes":
            count_kid_peoples = int(input("Enter how much children: "))
            kid_ticket_price = int(input("Enter price kid ticket: "))

        if kid_peoples.lower() == "yes":
            peoples_result = count_peoples * price_ticket
            kid_result = count_kid_peoples * kid_ticket_price
            total_result = peoples_result + kid_result
            print(total_result)
            wanna_continue = input("Would you like continue?(Enter Yes/No): ")

            if wanna_continue.lower() != "yes":
                print("Okay, see you later!")
                exit()
            if wanna_continue.lower() == "yes":
                continue
        if kid_peoples.lower() != "yes":
            result = count_peoples * price_ticket
            print(result)
            wanna_continue = input("Would you like continue?(Enter Yes/No): ")

            if wanna_continue.lower() != "yes":
                print("Okay, see you later!")
                exit()
            if wanna_continue.lower() == "yes":
                continue

def TipCalculator():
    wanna_continue = input("Would you like continue?(Enter Yes/No): ")

    if wanna_continue.lower() != "yes":
        print("Okay, see you later!")
        exit()
    while wanna_continue.lower() == "yes":

        tip = float(input("Enter percent of tip(IN FLOAT): "))
        bill = int(input("How much you spend: "))

        result = bill * tip
        print(result)
        wanna_continue = input("Would you like continue?(Enter Yes/No): ")

        if wanna_continue.lower() != "yes":
            print("Okay, see you later!")
            exit()
        if wanna_continue.lower() == "yes":
            continue

def SetNumbers():

    print("Welcome to SetNumbers(RECODE)")

    file_accept = input("Do you want to create file? " + "\n")

    if file_accept == "Да":
        file_name = input("Enter name file: " + "\n")

    print(" 1 - SetNumbers \n 2 - Check file \n 3 - Check file name \n 4 - Simple SetNumbers \n 5 - Exit" + "\n")
    choice = int(input("Select category: "))


    while choice == 1:
        full_name = str(input("Enter first name and surname: " + "\n"))
        estimation = str(input("Enter number: " + "\n"))
        choice_1_reason = input("Does number have a reason?(Enter Yes/No): " + "\n")
        if choice_1_reason.lower() == "yes":
            reason = str(input("Enter reason: "))
            choice_1_item = input("This is school, lesson, item? (Enter Yes/No): " + "\n")
            if choice_1_item.lower() == "yes":
                item_type = str(input("Enter category of number(lesson,item):  " + "\n"))
                item = str(input("Enter " + item_type + ": " + "\n"))
        date = str(input("Enter date in format xx.xx.xx: " + "\n"))

        choice_file_save = str(input("Would you like to save information in file? " + "\n"))

        if choice_file_save.lower() == "yes":
            if choice_1_reason == "yes":
                three = "For the: " + reason + "\n"
            if choice_1_item.lower() == "yes":
                fourth = item_type + ": " + item + "\n"
            if choice_file_save.lower() == "yes":
                one = "-------=" + "[" + full_name + "]" + "=-------" + " \n"
                two = "Number: " + estimation + " \n"
                fiveth = "--------=" + "[" + date + "]" + "=--------" + "\n"

            with open(file_name, "a", encoding='utf-8') as f:
                f.write(one)
                f.write(two)
                if choice_1_reason.lower() == "yes":
                    f.write(three)
                if choice_1_item.lower() == "yes":
                    f.write(fourth)
                f.write(fiveth)

                print("Save is successful! All information save in file. File has name:" + file_name + "\n")

        if choice_file_save.lower() == "no":
            if choice_1_reason.lower() == "yes":
                three = "For the: " + reason + "\n"
            if choice_1_item.lower() == "yes":
                fourth = item_type + ": " + item + "\n"
            one = "-------=" + "[" + full_name + "]" + "=-------" + " \n"
            two = "Number: " + estimation + " \n"
            fiveth = "--------=" + "[" + date + "]" + "=--------" + "\n"

            print(one)
            print(two)
            if choice_1_reason.lower() == "yes":
                print(three)
            if choice_1_item.lower() == "yes":
                print(fourth)
            print(fiveth)

        repeat_choice = input("Would you like continue? " + "\n")

        if repeat_choice.lower() == "yes":
            continue
        else:
            break

    if choice == 2:
        with open(file_name, "r", encoding="utf-8") as f1:
            for line in f1:
                print(line.strip())

    if choice == 3:
        if file_accept.lower() == "yes":
            print(file_name)
        else:
            print("Error, you don't have a file name!")

    if choice == 4:
        print("Welcome to SimpleSetNumbers!" + "\n")
        s_choice_reason = input("Does number have a reason?(Enter Yes/No): " + "\n")
        if s_choice_reason.lower() == "yes":
            s_accept_reason = input("Would you like enter reason previously?(Enter Yes/No): " + "\n")
            if s_accept_reason.lower() == "yes":
                s_reason = str(input("Enter reason of number: " + "\n"))
        s_accept_item = input("Would you like enter item, lesson previously?(Enter Yes/No): " + "\n")
        if s_accept_item.lower() == "yes":
            s_choice_item = input("This is item, lesson(Enter Yes/No): " + "\n")
            if s_choice_item.lower() == "yes":
                s_item_type = str(input("This is item, lesson? " + "\n"))
                s_item = str(input("Enter " + s_item_type + ": " + "\n"))
            if s_choice_item.lower() == "no":
                s_unknown_item_type = str(input("Enter what is this: " + "\n" ))
        s_choice_date = input("Would you like enter date previously?(Enter Yes/No): " + "\n")
        if s_choice_date.lower() == "yes":
            s_date = input("Enter date in format xx.xx.xx: " + "\n")
        while True:
            s_fullname = str(input("Enter first name and surname: " + "\n"))
            s_number = str(input("Enter number: " + "\n"))
            if s_choice_date.lower() == "no":
                s_date = str(input("Enter date in format xx.xx.xx: " + "\n"))
            if s_accept_reason.lower() == "no" and s_choice_reason.lower() == "yes":
                s_reason = str(input("Enter reason: " + "\n"))
            if s_accept_item.lower() == "no":
                s_choice_item = input("This is school item, lesson?(Enter Yes/No): " + "\n")
                if s_choice_item.lower() == "yes":
                    s_item_type = str(input("This is item,lesson? " + "\n"))
                    s_item = str(input("Enter " + s_item_type + ": " + "\n"))
                if s_choice_item.lower() == "no":
                    s_unknown_item_type = str(input("Enter what is this: " + "\n"))
                    s_item = str(input("Enter " + s_item_type + ": " + "\n"))

            s_accept_file_save = input("Would you like to save all information in file?(Enter Yes/No): " + "\n")
            if s_accept_file_save.lower() == "yes":
                if s_choice_reason.lower() == "yes" and s_accept_reason.lower() == "yes" or s_accept_reason.lower() == "no":
                    three = "For the: " + s_reason + "\n"
                if s_accept_item.lower() == "yes" and s_choice_item.lower() == "yes":
                    fourth = s_item_type + ": " + s_item + "\n"
                elif s_choice_item.lower() == "no":
                    fourth = s_unknown_item_type + ": " + s_item + "\n"
                if s_choice_date.lower() == "yes" or s_choice_date.lower() == "no":
                    fiveth = "--------=" + "[" + s_date + "]" + "=--------" + "\n"
                one = "-------=" + "[" + s_fullname + "]" + "=-------" + " \n"
                two = "Number: " + s_number + " \n"

                with open(file_name, "a", encoding='utf-8') as f:
                    f.write(one)
                    f.write(two)
                    if s_choice_reason.lower() == "yes" and s_accept_reason.lower() == "yes" or s_accept_reason.lower() == "no":
                        f.write(three)
                    if s_accept_item.lower() == "yes" and s_choice_item.lower() == "no":
                        f.write(fourth)
                    elif s_choice_item.lower() == "no":
                        f.write(fourth)
                    if s_choice_date.lower() == "yes" or s_choice_date.lower() == "no":
                        f.write(fiveth)

                    print("Save is successfully! All information save to file. File has name: " + file_name + "\n")

            if s_accept_file_save.lower() == "no":
                if s_choice_reason.lower() == "yes" and s_accept_reason.lower() == "yes" or s_accept_reason.lower() == "no":
                    three = "For the: " + s_reason + "\n"
                if s_accept_item.lower() == "yes" or s_accept_item.lower() == "no" and s_choice_item.lower() == "yes":
                    fourth = s_item_type + ": " + s_item + "\n"
                elif s_choice_item.lower() == "no":
                        fourth = s_unknown_item_type + ": " + s_item + "\n"
                if s_choice_date.lower() == "yes" or s_choice_date.lower() == "no":
                    fiveth = "--------=" + "[" + s_date + "]" + "=--------" + "\n"
                one = "-------=" + "[" + s_fullname + "]" + "=-------" + " \n"
                two = "Number: " + s_number + " \n"

                print(one)
                print(two)
                if s_choice_reason.lower() == "yes" and s_accept_reason.lower() == "yes" or s_accept_reason.lower() == "no":
                    print(three)
                if s_accept_item.lower() == "yes" or s_accept_item.lower() == "no" and s_choice_item.lower() == "yes":
                    print(fourth)
                elif s_choice_item.lower() == "no":
                    print(fourth)
                if s_choice_date.lower() == "yes" or s_choice_date.lower() == "no":
                    print(fiveth)

            s_repeat_choice = input("Would you like continue? " + "\n")

            if s_repeat_choice.lower() == "yes":
                continue
            else:
                break

    if choice == 5:
        exit()

def todo_list():
    tasks = []

    while True:
        print("1. Add task \n")
        print("2. See tasks \n")
        print("3. Remove task \n")
        print("4. Exit \n")

        choice = input("Enter your choice: \n")

        if choice == '1':
            task = input("Enter task: \n")
            tasks.append(task)
        elif choice == '2':
            if tasks:
                print("Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks here.")
        elif choice == '3':
            if tasks:
                task = input("Enter task for remove: ")
                if task in tasks:
                    tasks.remove(task)
                    print("Task has been removed.")
                else:
                    print("Task is not found.")
            else:
                print("No tasks.")
        elif choice == '4':
            break
        else:
            print("Wrong choice. Try again.")

def ghoul():
    for i in range(1000, 0, -7):
        time.sleep(0.01)
        print(i - 7)

if choice_program == 1.1:
    RandomGame()
if choice_program == 1.2:
    RollDices()
if choice_program == 1.3:
    RCB()
if choice_program == 1.4:
    Bingo()
if choice_program == 3.1:
    Calculator()
if choice_program == 3.2:
    TicketCalculator()
if choice_program == 3.3:
    TipCalculator()
if choice_program == 4.1:
    todo_list()
if choice_program == 4.2:
    SetNumbers()
if choice_program == 5.1:
    ghoul()