from addToDatabase import *
from deleteFromDatabase import *
from search import *

def add_to_database():
    print("List of available tables: ")
    print("    1. Elemental_Interactions")
    print("    2. Enemies")
    print("    3. Elites")
    print("    4. Domains")
    print("    5. Characters")
    print("    6. Rewards")
    print("    7. Back")
    user = int(input("Which table would you like to insert into? "))
    if user == 1:
        add_to_database_elemental()
        add_to_database()
    elif user == 2:
        add_to_database_enemy()
        add_to_database()
    elif user == 3:
        add_to_database_elite()
        add_to_database()
    elif user == 4:
        add_to_database_domains()
        add_to_database()
    elif user == 5:
        add_to_database_characters()
        add_to_database()
    elif user == 6:
        add_to_database_rewards()
        add_to_database()
    elif user != 7:
        print("Invalid number try again")
        add_to_database()
    
def delete_from_database():
    print("List of available tables: ")
    print("    1. Elemental_Interactions")
    print("    2. Enemies")
    print("    3. Elites")
    print("    4. Domains")
    print("    5. Characters")
    print("    6. Rewards")
    print("    7. Back")
    user = int(input("Which table would you like to remove from? "))
    if user == 1:
        delete_from_elemental()
        delete_from_database()
    elif user == 2:
        delete_from_enemy()
        delete_from_database()
    elif user == 3:
        delete_from_elite()
        delete_from_database()
    elif user == 4:
        delete_from_domains()
        delete_from_database()
    elif user == 5:
        delete_from_characters()
        delete_from_database()
    elif user == 6:
        delete_from_rewards()
        delete_from_database()
    elif user != 7:
        print("Invalid number try again.")
        delete_from_database()

def start_up_manager():
    print("What would you like to do?")
    print("     1. Search the database")
    print("     2. Add to the database")
    print("     3. Remove from the database")
    print("     4. Exit")
    user = int(input("Enter the number of your choice: "))
    if user == 1:
        search()
        start_up_manager()
    elif user == 2:
        add_to_database()
        start_up_manager()
    elif user == 3:
        delete_from_database()
        start_up_manager()
    elif user == 4:
        print("Thanks for using the database!")
    else:
        print("Invalid number try again.")
        start_up_manager()
    
def start_up_user():
    print("What would you like to do?")
    print("     1. Search the database")
    print("     2. Exit")
    user = int(input("Enter the number of your choice: "))
    if user == 1:
        search()
        start_up_user()
    elif user == 2:
        print("Thanks for using the database!")
    else:
        print("Invalid number try again.")
        start_up_user()

def start_up():
    print("Are you a user or a manager?")
    x = raw_input("U/M ")
    if x.lower() == "u":
        start_up_user()
    elif x.lower() == "m":
        start_up_manager()

start_up()