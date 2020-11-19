import mysql.connector

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