def start_up_manager():
    print("What would you like to do?")
    print("     1. Search the database")
    print("     2. Add to the database")
    print("     3. Remove from the database")
    print("     4. Exit")
    user = int(input("Enter the number of your choice: "))
    while user != 0:
        if user == 1:
        elif user == 2:
        elif user == 3:
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