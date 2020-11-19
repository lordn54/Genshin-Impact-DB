import mysql.connector

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