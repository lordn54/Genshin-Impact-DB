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