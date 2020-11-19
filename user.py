from addToDatabaseElement import *
from addToDatabaseEnemies import *
from addToDatabaseElites import *
from addToDatabaseDomains import *
from addToDatabaseCharacters import *
from addToDatabaseRewards import *
from deleteFromElement import *
from deleteFromEnemies import *
from deleteFromElites import *
from deleteFromDomains import *
from deleteFromCharacters import *
from deleteFromRewards import *

def add_to_database():
    print("List of available tables: ")
    print("    1. Elemental_Interactions")
    print("    2. Enemies")
    print("    3. Elites")
    print("    4. Domains")
    print("    5. Characters")
    print("    6. Rewards")
    print("    0. To Quit")
    user = int(input("Which table would you like to insert into? "))
    if user == 1:
        add_to_database_elemental()
    elif user == 2:
        add_to_database_enemy()
    elif user == 3:
        add_to_database_elite()
    elif user == 4:
        add_to_database_domains()
    elif user == 5:
        add_to_database_characters()
    elif user == 6:
        add_to_database_rewards()
    if user == 0:
        print("     Goodbye.")
        start_up_manager()
    
def delete_from_database():
    print("List of available tables: ")
    print("    1. Elemental_Interactions")
    print("    2. Enemies")
    print("    3. Elites")
    print("    4. Domains")
    print("    5. Characters")
    print("    6. Rewards")
    print("    0. To Quit")
    user = int(input("Which table would you like to insert into? "))
    if user == 1:
        delete_from_elemental()
    elif user == 2:
       delete_from_enemy()
    elif user == 3:
        delete_from_elite()
    elif user == 4:
        delete_from_domains()
    elif user == 5:
        delete_from_characters()
    elif user == 6:
        delete_from_rewards()
    if user == 0:
        print("     Goodbye.")
        start_up_manager()

def start_up_manager():
    user = 5
    while user != 0:
        print("What would you like to do?")
        print("     1. Search the database")
        print("     2. Add to the database")
        print("     3. Remove from the database")
        print("     4. Exit")
        user = int(input("Enter the number of your choice: "))
        if user == 1:
            print()
        elif user == 2:
            add_to_database()
            user = 0
        elif user == 3:
            delete_from_database()
            user = 0;
        elif user == 4:
            print("Thanks for using the database!")
            user = 0
        else:
            print("Invalid number try again.")
    
def start_up_user():
    print("What would you like to do?")
    print("     1. Search the database")
    print("     2. Exit")
    user = int(input("Enter the number of your choice: "))
    while user != 0:
        if user == 1:
            print("hello")
        elif user == 2:
            print("Thanks for using the database!")
            user = 0
        else:
            print("Invalid number try again.")

def start_up():
    print("Are you a user or a manager?")
    x = raw_input("U/M ")
    if x.lower() == "u":
        start_up_user()
    elif x.lower() == "m":
        start_up_manager()

start_up()