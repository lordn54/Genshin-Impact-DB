import mysql.connector

domains = {"Hidden Palace of Lianshan Formula","Cecilia Garden","Forsaken Rift","Taishan Mansion"}
elites = {"Anemo Hypostasis","Electro Hypostasis","Geo Hypostasis","Oceanid","Pyro Regisvine","Cryo Regisvine","Stormterror","Andrius","Tartaglia"}
characters = {"Amber","Barbara","Beidou","Bennett","Chongyun","Diluc","Diona","Fischl","Jean","Kaeya","Keqing","Klee","Lisa","Mona","Ningguang","Noelle","Qiqi","Razor","Sucrose","Tartaglia","Venti","Xiangling","Xingqiu"}

def search():
    print("""What are you looking for?
             1. Enemy
             2. Character
             3. Domain
             4. Item
             5. Go Back
             """)
    choice = raw_input('\n')
    if (choice == '1'):
        search_enemy()
        search()
    elif (choice == '2'):
        search_character()
        search()
    elif (choice == '3'):
        search_domain()
        search()
    elif (choice == '4'):
        search_item()
        search()
    elif (choice != '5'):
        print("\nPlease enter a valid option\n")
        search()
    
def search_enemy():
    enemy = raw_input("\nEnter the case-sensitive name of the domain: ")
    try:
        mydb = mysql.connector.connect(
          host='localhost',
          user='prescott',
          password='embryriddle',
          database='lordn2_db',
          unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("""SELECT Rewards.name AS Name, min_level AS Level FROM Enemies
                               JOIN Enemy_Rewards USING (enemy_id) 
                               JOIN Rewards USING (reward_id)
                               WHERE Enemies.name = {}""".format(enemy))
        print("\n{} drops the following:\n")
        for result in cursor.fetchall():
            if (result['Level'] == 0):
                print("  {}\n".format(result['Name']))
            else:
                print("  {} when encountered at or above level {}\n".format(result['Name'], result['Level']))
    except mysql.connector.Error as error:
        print(error)
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()

def search_character():
    character = raw_input("\nEnter the case-sensitive name of the domain: ")
    try:
        mydb = mysql.connector.connect(
          host='localhost',
          user='prescott',
          password='embryriddle',
          database='lordn2_db',
          unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("""SELECT Rewards.name AS Name FROM Characters
                               JOIN Character_Rewards USING (character_id) 
                               JOIN Rewards USING (reward_id)
                               WHERE Characters.name = {}""".format(character))
        print("\n{} requires the following ascension materials:\n")
        for result in cursor.fetchall():
            print("  {}\n".format(result['Name']))
    except mysql.connector.Error as error:
        print(error)
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()

def search_domain():
    domain = raw_input("\nEnter the case-sensitive name of the domain: ")
    try:
        mydb = mysql.connector.connect(
          host='localhost',
          user='prescott',
          password='embryriddle',
          database='lordn2_db',
          unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("""SELECT Rewards.name AS Name, min_level AS Level FROM Domains
                               JOIN Domain_Rewards USING (domain_id) 
                               JOIN Rewards USING (reward_id)
                               WHERE Domains.name = {}""".format(domain))
        print("\n{} rewards 100 Adventure Rank experience and the following:\n")
        for result in cursor.fetchall():
            print("  {} starting at Adventure Rank {}\n".format(result['Name'], result['Level']))
    except mysql.connector.Error as error:
        print(error)
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()

def search_item():
    item = raw_input("\nEnter the case-sensitive name of the item: ")
    try:
        mydb = mysql.connector.connect(
          host='localhost',
          user='prescott',
          password='embryriddle',
          database='lordn2_db',
          unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("""SELECT * FROM 
                          (SELECT Enemies.name AS Name, min_level AS Level FROM Rewards 
                               JOIN Enemy_Rewards USING (reward_id) 
                               JOIN Enemies USING (enemy_id)
                               WHERE Rewards.name = {}
                           UNION
                           SELECT Domains.name AS Name, min_level AS Level FROM Rewards 
                               JOIN Domain_Rewards USING (reward_id) 
                               JOIN Domains USING (domain_id)
                               WHERE Rewards.name = {}
                           UNION
                           SELECT Elites.name AS Name, min_level AS Level FROM Rewards 
                               JOIN Elite_Rewards USING (reward_id) 
                               JOIN Elites USING (elite_id)
                               WHERE Rewards.name = {}
                           UNION
                           SELECT Characters.name AS Name, min_level AS Level FROM Rewards 
                               JOIN Character_Rewards USING (reward_id) 
                               JOIN Characters USING (character_id)
                               WHERE Rewards.name = {}
                           )""".format(item, item, item, item))
        charFlag = False
        for result in cursor.fetchall():
            if (result['Name'] in domains):
                print("  It drops from {} starting at Adventure Rank {}\n".format(result['Name'], result['Level']))
            elif (result['Name'] in elites and not charFlag):
                if (result['Level'] == 0):
                    print("  {} drops it\n".format(result['Name']))
                else:
                    print("  {} drops it starting at level {}\n".format(result['Name'], result['Level']))
            elif (result['Name'] in characters):
                charFlag = True
                print("  {} requires it for ascension\n".format(result['Name']))
            else:
                if (result['Level'] == 0):
                    print("  {}s drop it\n".format(result['Name']))
                else:
                    print("  {}s drop it starting at level {}\n".format(result['Name'], result['Level']))
    except mysql.connector.Error as error:
        print(error)
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
