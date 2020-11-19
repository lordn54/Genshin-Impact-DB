import mysql.connector

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