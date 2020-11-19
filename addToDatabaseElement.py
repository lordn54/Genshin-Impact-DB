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