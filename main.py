# *****************************************************************************
# Author:           Zachary Foster
# Lab:              Lab 5
# Date:             5/19/2021
# Description:      A game of chance in the arena. Randomly generated health
#                   and attack values are used to fight an opponent in the
#                   arena. The match will start once you have chosen your
#                   character and type 'start'. The first player to lose all
#                   of their health loses.
# Input:            char_choice = Your character choice as an integer value
#                   start = Type start to begin the match.
#                   name = Type your name.
#                   home = Type where you are from.
#                   song = Enter your favorite song.
# Output:           -An introduction message welcoming you to the game that
#                   explains the characters
#                   -Once you have chosen a charter, you are asked to enter
#                   your name, land you hail from, and your favorite song. This
#                   information will be used as your introduction to the arena.
#                   Your health roll is then printed to the screen as well
#                   as your opponents health.
#                   -Once you type 'start' the battle begins. The attack
#                   damage done by both of you is printed to the screen
#                   as well as the resulting drop in health.
#                   -This continues until someones health drops to 0 or lower.
#                   -You will be asked if you would like to play again
# Sources:          Lab 5 specifications, Gaddis book, lesson 8 slides.
# *****************************************************************************

# Import random
# From time Import sleep
import random
from time import sleep

# Constant Integer ENEMY_ID = 4
# Constant Integer WARRIOR_ID = 1
# Constant Integer ROGUE_ID = 2
# Constant Integer MAGE_ID = 3
ENEMY_ID = 4
WARRIOR_ID = 1
ROGUE_ID = 2
MAGE_ID = 3


# Module main()
#   Call show_welcome
#   Declare Integer char_choice
#   Declare Integer char_health
#   Declare String char_string
#   Declare String play_again = "y"
#
#   While play_again == "y"
#       Set char_choice, char_string = charpick()
#       Call char_info()
#       Set char_health = health_roll(char_choice)
#       Set enemy_health = health_roll(ENEMY_ID)
#       Call arena(char_choice, char_health, enemy_health, char_string)
#       Set play_again = repeat_play()
#   End while
# End Module

def main():
    show_welcome()
    char_choice = 0
    char_health = 0
    char_string = ""
    play_again = "y"

    while play_again == "y":
        char_choice, char_string = char_pick()
        char_info()
        char_health = health_roll(char_choice)
        enemy_health = health_roll(ENEMY_ID)
        arena(char_choice, char_health, enemy_health, char_string)
        play_again = repeat_play()


# Function show_welcome()
#   Display "             ******Welcome to TEXT FIGHTER!******"
#   Display "A game of chance in the arena where a dice roll decides your
#   fate\n"
#   Display "Your choices in the arena are...."
#   Display "Warrior - High health chance (70-100) with light attacks (1-15)."
#   Display "Rogue - Medium health chance (40-70) with moderate attack power
#           (1-20)"
#   Display "Mage - Low health chance (30-50), but with a high attack power
#           (1-30)."
#   Display "Enter 1, 2, or 3 to choose your character.\n"
# End function

def show_welcome():
    print("             ******Welcome to TEXT FIGHTER!******")
    print("A game of chance in the arena where a dice roll decides your "
          "fate.\n")
    print("Your choices in the arena are....")
    print("Warrior - High health chance (70-100) with light attacks (1-15).")
    print("Rogue - Medium health chance (40-70) with moderate attack power"
          "(1-20).")
    print("Mage - Low health chance (30-50), but with a high attack power"
          "(1-30).")
    print("Enter 1, 2, or 3 to choose your character.\n")

# Function String char_info()
#   Constant Integer SIZE = 3
#   Declare String char_questions[SIZE] = "What is your name?: ",
#                                         "Where are you from?: ",
#                                         "What is your favorite song?: "
#   Declare String char_information[SIZE]
#   Declare String answer
#
#   For question = 0 to SIZE - 1
#       Display char_questions[question]
#       Input answer
#       char_information.append(answer)
#   Display "\n" + char_information[0], "the brave is entering the arena."
#   Display "He hails from the land of", char_information[1] + "."
#   Display "and his favorite song is", char_information[2] + ".\n"

def char_info():
    SIZE = 3
    char_questions = ["What is your name?: ",
                      "Where are you from?: ",
                      "What is your favorite song?: "]
    char_information = []
    answer = ""

    for question in char_questions:
        answer = input(question)
        char_information.append(answer)
    print("\n" + char_information[0], "the brave is entering the arena.")
    print("He hails from the land of", char_information[1] + ".")
    print("and his favorite song is", char_information[2] + ".\n")


# Function Integer health_roll(Integer char_id)
#   Declare Integer roll
#
#   If char_id == WARRIOR_ID Then
#       Set roll = random.randint(70, 100)
#       Display f"\nYou have chosen a warrior with a health roll of {roll}.\n"
#       Return roll
#   Else
#   If char_id == ROGUE_ID Then
#       Set roll = random.randint(40, 70)
#       Display f"\nYou have chosen a rogue with a health roll of {roll}.\n"
#       Return roll
#   Else
#   If char_id == MAGE_ID Then
#       Set roll = random.randint(30, 50)
#       Display f"\nYou have chosen a mage with a health roll of {roll}.\n"
#       Return roll
#   Else
#   If char_id == ENEMY_ID Then
#       Set roll = random.randint(50, 90)
#       Display f"Your enemy enters the arena with a health roll of {roll}."
#       Return roll
#   End if
# End function

def health_roll(char_id):
    roll = 0

    if char_id == WARRIOR_ID:
        roll = random.randint(70, 100)
        print(f"\n**You have chosen a warrior with a health roll of {roll}.\n")
        return roll
    elif char_id == ROGUE_ID:
        roll = random.randint(40, 70)
        print(f"\n**You have chosen a rogue with a health roll of {roll}.\n")
        return roll
    elif char_id == MAGE_ID:
        roll = random.randint(30, 50)
        print(f"\n**You have chosen a mage with a health roll of {roll}.\n")
        return roll
    elif char_id == ENEMY_ID:
        roll = random.randint(50, 90)
        print(f"**Your enemy enters the arena with a health roll of {roll}.")
        return roll


# Function Integer char_pick()
#   Declare Integer char_choice
#   Declare Boolean done
#
#   While not done
#       Display "Choose your character:"
#       Display "1. Warrior"
#       Display "2. Rogue"
#       Display "3. Mage"
#       Display "> "
#       Input char_choice
#       If char_choice == "1" Then
#           done = True
#           Return WARRIOR_ID, "Warrior"
#       Else
#       If char_choice == "2" Then
#           done = True
#           Return ROGUE_ID, "Rogue"
#       Else
#       If char_choice == "3" Then
#           done = True
#           Return MAGE_ID, "Mage"
#       Else
#           Display "Not a valid entry. Please try again.\n"
#       End if
#   End while
# End function

def char_pick():
    char_choice = 0
    done = False

    while not done:
        print("Choose your character:")
        print("1. Warrior")
        print("2. Rogue")
        print("3. Mage")
        char_choice = input("> ")

        if char_choice == "1":
            done = True
            return WARRIOR_ID, "Warrior"
        elif char_choice == "2":
            done = True
            return ROGUE_ID, "Rogue"
        elif char_choice == "3":
            done = True
            return MAGE_ID, "Mage"
        else:
            print("Not a valid entry. Please try again.\n")


# Function Integer attack_roll(Integer char_id)
#   Declare Integer damage_amount
#
#   If char_id == WARRIOR_ID Then
#       Set roll = random.randint(1, 15)
#       Return roll
#   Else
#   If char_id == ROGUE_ID Then
#       Set roll = random.randint(1, 20)
#       Return roll
#   Else
#   If char_id == MAGE_ID Then
#       Set roll = random.randint(1, 30)
#       Return roll
#   Else
#   If char_id == ENEMY_ID Then
#       Set roll = random.randint(0, 17)
#       Return roll
#   End if
# End function

def attack_roll(char_id):
    damage_amount = 0

    if char_id == WARRIOR_ID:
        roll = random.randint(1, 15)
        return roll
    elif char_id == ROGUE_ID:
        roll = random.randint(1, 20)
        return roll
    elif char_id == MAGE_ID:
        roll = random.randint(1, 30)
        return roll
    elif char_id == ENEMY_ID:
        roll = random.randint(0, 17)
        return roll


# Function arena(Integer char_pick, char_health, enemy_health, String
# char_string)
#   Declare Boolean start
#
#   While not start
#       Display "Type 'start' to begin the battle...: "
#       Input start
#       If start_cond.lower() == "start" Then
#           start = True
#       Else
#           Display "\nNot a valid entry. Try typing 'start'.\n"
#   Call sleep(1)
#   While True
#       Set player_dmg = attack_roll(char_pick)
#       Set enemy_dmg = attack_roll(ENEMY_ID)
#       Display f"The {char_string} attacks dealing {player_dmg} damage to
#       the enemy"
#       Set enemy_health -= player_dmg
#       If enemy_health <= 0 Then
#           Display "Your opponent has been defeated!"
#           break
#       Display f"Your opponents health falls to {enemy_health}"
#       Call sleep(1)
#       Display f"Your opponent fights back and deals {enemy_dmg} damage to
#       you."
#       Set char_health -= enemy_dmg
#       Display f"Your health falls to {char_health}"
#       If char_health <= 0 Then
#           Display "You have been defeated by your opponent! =("
#           break
#       Display f"Your health falls to {char_health}"
#       Call sleep(1)


def arena(char_pick, char_health, enemy_health, char_string):
    start = False

    while not start:
        start_cond = input("Type 'start' to begin the battle...: ")
        if start_cond.lower() == "start":
            start = True
        else:
            print("\nNot a valid entry. Try typing 'start'.\n")
    sleep(1)
    while True:
        player_dmg = attack_roll(char_pick)
        enemy_dmg = attack_roll(ENEMY_ID)
        print(f"The {char_string} attacks dealing {player_dmg} "
              "damage to the enemy")
        enemy_health -= player_dmg
        if enemy_health <= 0:
            print("Your opponent has been defeated!\n")
            break
        print(f"Your opponents health falls to {enemy_health}\n")
        sleep(1)
        print(f"Your opponent fights back and deals {enemy_dmg} damage to you")
        char_health -= enemy_dmg
        if char_health <= 0:
            print("You have been defeated by your opponent! =(\n")
            break
        print(f"Your health falls to {char_health}\n")
        sleep(1)


# Function String repeat_play()
#   Declare String repeat
#   While repeat != "y" or "n"
#       Display "Would you like to play again?(y/n): "
#       Input repeat
#       If repeat == "y" Then
#           Return "y"
#       Else
#       If repeat == "n" Then
#           Return "n"
#       Else
#           Display "Not a valid entry. Try again."

def repeat_play():
    repeat = ""
    while repeat != "y" or "n":
        repeat = input("\nWould you like to play again?(y/n): ")
        if repeat.lower() == "y":
            return "y"
        elif repeat.lower() == "n":
            return "n"
        else:
            print("Not a valid entry. Try again.")


# Call main
main()


