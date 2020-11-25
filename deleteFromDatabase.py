import mysql.connector

def delete_from_elemental():
    element1 = raw_input("Element 1 is? ")
    element2 = raw_input("Element 2 is? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        delete_elemental_interaction = ("DELETE FROM Elemental_Interactions "
                                                   "WHERE (element1 = %s AND element2 = %s)")
        data_elemental = (element1, element2)
        cursor.execute(delete_elemental_interaction, data_elemental)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()
        
def delete_from_enemy():
    name = raw_input("Name is? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        delete_enemy = ("DELETE FROM Enemies "
                                                   "WHERE (name = %s")
        data_enemy = (name)
        cursor.execute(delete_enemy, data_enemy)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()
        
def delete_from_elite():
    name = raw_input("Name is? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        delete_elite = ("DELETE FROM Elites "
                                                   "WHERE (name = %s")
        data_elite = (name)
        cursor.execute(delete_elite, data_elite)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()
        
def delete_from_characters():
    name = raw_input("Name is? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        delete_character = ("DELETE FROM Characters "
                                                   "WHERE (name = %s")
        data_character = (name)
        cursor.execute(delete_charater, data_character)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()
       
def delete_from_domain():
    name = raw_input("Name is? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        delete_domain = ("DELETE FROM Domains "
                                                   "WHERE (name = %s")
        data_domain = (name)
        cursor.execute(delete_domain, data_domain)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()
        
def delete_from_rewards():
    name = raw_input("Name is? ")
    try:
        mydb = mysql.connector.connect(
         host='localhost',
         user='lordn2',
         password='May301999',
         database='lordn2_db',
         unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        delete_reward = ("DELETE FROM Rewards "
                                                   "WHERE (name = %s")
        data_reward = (name)
        cursor.execute(delete_reward, data_reward)
        mydb.commit()
       
    except mysql.connector.Error as error:
        print(error)
    finally:
      if mydb.is_connected():
        cursor.close()
        mydb.close()