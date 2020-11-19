import mysql.connector

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