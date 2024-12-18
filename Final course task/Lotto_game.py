import random
from time import sleep
def random_numbers():
    return sorted(random.sample(range(1, 38), 6))
def check_winning_numbers(player_numbers, winning_numbers):
    return len(set(player_numbers) & set(winning_numbers))
def calculate_prize(matches):
    if matches == 6:
        return 1000000
    elif matches == 5:
        return 5000
    elif matches == 4:
        return 100
    elif matches == 3:
        return 10
    else:
        return 0
def play_lotto():
    print("Hi!\nWelcome to our brand new Lotto game.\n------------------------------")
    sleep(2)
    money = int(input("Each row costs 3 ILS.\nHow much money do you want to insert?\n"))
    rows_num = money // 3
    if money >= 3:
        print("Great! you have money for " + str(rows_num) + " row/s.\nYour change is: " + str(money % 3) + " ILS.\n------------------------------\nNow, let's check if you're a lucky person!")
        total_prize = 0
        for _ in range(rows_num):
            user_guess = []
            for i in range(6):
                num = int(input("Enter a number between 1-37: "))
                while not (1 <= num <= 37) or num in user_guess:
                    if num in user_guess:
                        num = int(input("Number already entered! Enter a different number between 1-37: "))
                    else:
                        num = int(input("Number out of range! Enter a number between 1-37: "))
                user_guess.append(num)
            print("------------------------------\nYour numbers: " + str(user_guess))
            winning_numbers = random_numbers()
            print("Winning numbers: " + str(winning_numbers))
            matches = check_winning_numbers(user_guess, winning_numbers)
            prize = calculate_prize(matches)
            total_prize += prize
            print("--------\nMatches: " + str(matches) + "\nPrize: " + str(prize) + " ILS")
        print("--------\nTotal prize won: " + str(total_prize) + " ILS")
    else:
        print("Unfortunately,\nyou didn't insert enough money.")
while True:
    play_lotto()
    sleep(2)
    play_again = input("--------\nDo you want to play again? yes/no: ")
    if play_again != 'yes':
        sleep(1)
        print("--------\nThank you! Bye Bye")
        break