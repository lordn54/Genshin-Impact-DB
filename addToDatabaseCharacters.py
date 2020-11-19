import mysql.connector

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