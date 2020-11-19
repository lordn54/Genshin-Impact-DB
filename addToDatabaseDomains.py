import mysql.connector

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