import mysql.connector

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