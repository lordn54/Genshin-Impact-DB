import mysql.connector

domains = {"Hidden Palace of Lianshan Formula","Cecilia Garden","Forsaken Rift","Taishan Mansion"}
elites = {"Anemo Hypostasis","Electro Hypostasis","Geo Hypostasis","Oceanid","Pyro Regisvine","Cryo Regisvine","Stormterror","Andrius","Tartaglia"}
characters = {"Amber","Barbara","Beidou","Bennett","Chongyun","Diluc","Diona","Fischl","Jean","Kaeya","Keqing","Klee","Lisa","Mona","Ningguang","Noelle","Qiqi","Razor","Sucrose","Tartaglia","Venti","Xiangling","Xingqiu"}

def search():
    print("""What are you looking for?
             1. Enemy
             2. Character
             3. Domain
             4. Elite
             5. Item
             6. Back
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
        search_elite()
        search()
    elif (choice == '5'):
        search_item()
        search()
    elif (choice != '6'):
        print("\nPlease enter a valid option\n")
        search()
    
def search_enemy():
    enemy = raw_input("\nEnter the case-sensitive name of the enemy: ")
    try:
        mydb = mysql.connector.connect(
          host='localhost',
          user='prescott',
          password='embryriddle',
          database='lordn2_db',
          unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor(dictionary=True)
        args = [enemy]
        cursor.callproc("search_enemy", args)
        print("\n{} drops the following:\n".format(enemy))
        for result_cursor in cursor.stored_results():
            for row in result_cursor:
                if (row[1] == 0):
                    print("  {}\n".format(row[0]))
                else:
                    print("  {} when encountered at or above level {}\n".format(row[0], row[1]))
    except mysql.connector.Error as error:
        print(error)
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()

def search_character():
    character = raw_input("\nEnter the case-sensitive name of the character: ")
    if character in characters:
        try:
            mydb = mysql.connector.connect(
              host='localhost',
              user='prescott',
              password='embryriddle',
              database='lordn2_db',
              unix_socket='/var/lib/mysql/mysql.sock'
            )
            cursor = mydb.cursor(dictionary=True)
            args = [character]
            cursor.callproc("search_character", args)
            print("\n{} requires the following ascension materials:\n".format(character))
            for result_cursor in cursor.stored_results():
                for row in result_cursor:
                    print("  {}\n".format(row[0]))
        except mysql.connector.Error as error:
            print(error)
        finally:
            if mydb.is_connected():
                cursor.close()
                mydb.close()
    else:
        print("\nPlease try again. Character name entered invalid.\n")

def search_domain():
    domain = raw_input("\nEnter the case-sensitive name of the domain: ")
    if domain in domains:
        try:
            mydb = mysql.connector.connect(
              host='localhost',
              user='prescott',
              password='embryriddle',
              database='lordn2_db',
              unix_socket='/var/lib/mysql/mysql.sock'
            )
            cursor = mydb.cursor(dictionary=True)
            args = [domain]
            cursor.callproc("search_domain", args)
            print("\n{} rewards 100 Adventure Rank experience and the following:\n".format(domain))
            for result_cursor in cursor.stored_results():
                for row in result_cursor:
                    print("  {} starting at Adventure Rank {}\n".format(row[0], row[1]))
            cursor.callproc("characters_by_element", args)
            print("Consider using one or more of the following characters:\n")
            for result_cursor in cursor.stored_results():
                for row in result_cursor:
                    print("  {} to cause the {} elemental reaction.\n".format(row[0], row[1]))
        except mysql.connector.Error as error:
            print(error)
        finally:
            if mydb.is_connected():
                cursor.close()
                mydb.close()
    else:
        print("\nPlease try again. Domain name entered invalid.\n")
            
def search_elite():
    elite = raw_input("\nEnter the case-sensitive name of the elite: ")
    if elite in elites:
        try:
            mydb = mysql.connector.connect(
              host='localhost',
              user='prescott',
              password='embryriddle',
              database='bellb18_db',
              unix_socket='/var/lib/mysql/mysql.sock'
            )
            cursor = mydb.cursor(dictionary=True)
            args = [elite]
            cursor.callproc("search_elite", args)
            print("\n{} drops the following:\n".format(elite))
            for result_cursor in cursor.stored_results():
                for row in result_cursor:
                    if row[1] > 0:
                        print("  {} when fought at level {}.\n".format(row[0], row[1]))
                    else:
                        print("  {}.\n".format(row[0]))
            cursor.callproc("characters_by_element", args)
            print("Consider using one or more of the following characters:\n")
            for result_cursor in cursor.stored_results():
                for row in result_cursor:
                    print("  {} to cause the {} elemental reaction.\n".format(row[0], row[1]))
        except mysql.connector.Error as error:
            print(error)
        finally:
            if mydb.is_connected():
                cursor.close()
                mydb.close()
    else:
        print("Please try again. Elite name entered invalid.\n")

def search_item():
    item = raw_input("\nEnter the case-sensitive name of the item: ")
    print("")
    try:
        mydb = mysql.connector.connect(
          host='localhost',
          user='prescott',
          password='embryriddle',
          database='lordn2_db',
          unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor(dictionary=True)
        args = [item]
        cursor.callproc("search_item", args)
        charFlag = False
        for result_cursor in cursor.stored_results():
            for row in result_cursor:
                if (row[0] in domains):
                    print("  It drops from {} starting at Adventure Rank {}\n".format(row[0], row[1]))
                elif (row[0] in elites and not charFlag):
                    if (row[1] == 0):
                        print("  {} drops it\n".format(row[0]))
                    else:
                        print("  {} drops it starting at level {}\n".format(row[0], row[1]))
                elif (row[0] in characters):
                    charFlag = True
                    print("  {} requires it for ascension\n".format(row[0]))
                else:
                    if (row[1] == 0):
                        print("  {}s drop it\n".format(row[0]))
                    else:
                        print("  {}s drop it starting at level {}\n".format(row[0], row[1]))
    except mysql.connector.Error as error:
        print(error)
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
