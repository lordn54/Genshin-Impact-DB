import mysql.connector

def add_to_database_elemental():
    element1 = raw_input("Element 1 is? ")
    element2 = raw_input("Element 2 is? ")
    name = raw_input("Name of Interaction is? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        add_elemental_interaction = ("INSERT INTO Elemental_Interactions "
                                                   "(element1, element2, name) "
                                                   "Values (%s, %s, %s)")
        data_elemental = (element1, element2, name)
        cursor.execute(add_elemental_interaction, data_elemental)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()

def add_to_database_enemy():
    name = raw_input("Name of enemy is? ")
    element = raw_input("Element is? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        add_enemy = ("INSERT INTO Enemies "
                                                   "(name, element) "
                                                   "Values (%s, %s)")
        data_enemy = (name, element)
        cursor.execute(add_enemy, data_enemy)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()
        
def add_to_database_elite():
    name = raw_input("Name of enemy is? ")
    element = raw_input("Element is? ")
    xp = raw_input("XP amount is? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        add_elite = ("INSERT INTO Enemies "
                                                   "(name, element) "
                                                   "Values (%s, %s)")
        data_elite = (name, element)
        cursor.execute(add_elite, data_elite)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()
        
def add_to_database_characters():
    name = raw_input("Name of Character? ")
    element = raw_input("Element of Character? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        add_character = ("INSERT INTO Characters "
                                                   "(name, element) "
                                                   "Values (%s, %s)")
        data_character = (name, element)
        cursor.execute(add_character, data_character)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()

def add_to_database_domains():
    name = raw_input("Name of Domain? ")
    element = raw_input("Element of Domain? ")
    xp = raw_input("XP of Domain? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        add_domain = ("INSERT INTO Domains "
                                                   "(name, element, xp) "
                                                   "Values (%s, %s, %s)")
        data_domain = (name, element, xp)
        cursor.execute(add_domain, data_domain)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()

def add_to_database_rewards():
    name = raw_input("Name of Reward? ")
    min_level = raw_input("Minimum level? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        add_reward = ("INSERT INTO Rewards "
                                                   "(name, min_level) "
                                                   "Values (%s, %s)")
        data_reward = (name, min_level)
        cursor.execute(add_reward, data_reward)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()