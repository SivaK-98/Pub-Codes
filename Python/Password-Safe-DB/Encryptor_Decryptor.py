from cryptography.fernet import Fernet, MultiFernet
import sqlite3
from sqlite3 import Error

sqliteConnection = sqlite3.connect("/home/siva/Documents/Siva/Code/python/Tkinter-App/vault.db")
cursor = sqliteConnection.cursor()
print("Connected to SQLite")


def insert_entry():
    db_count = cursor.execute("select count(*) from DB_CRED;").fetchone()[0]
    id = db_count
    print("Number of entries found before inserting:", id)
    count = 1
    my_dbs = []
    my_creds = []
    my_keys = []
    temp_dbs = []
    temp_creds = []
    temp_keys = []
    dbs = int(input("Enter the number of items to be added..: "))
    while count <= dbs:
        dbname = input("Enter the db name (Example DEV1-AUTH-WCS): ").upper()
        my_dbs.append(dbname)
        dbpass = input("Note: The password you are entering will be encrypted and stored\nEnter the DB passwords: ").encode()
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted = f.encrypt(dbpass)
        my_creds.append(encrypted.decode())
        print("Password enrypted..")
        my_keys.append(key.decode())
        count += 1

    sqlite_insert_with_param = """INSERT INTO DB_CRED(id, DBNAME, PASSWORD, KEY) VALUES (?, ?, ?, ?);"""
    sqlite_replace_with_param = """INSERT or Replace into DB_CRED(id, DBNAME, PASSWORD, KEY) VALUES (?, ?, ?, ?);"""


    for (a,b,c) in zip(my_dbs,my_creds, my_keys):
        id += 1
        insert_list = []
        insert_list.append(id)
        insert_list.append(a)
        insert_list.append(b)
        insert_list.append(c)
        data_tuple = tuple(insert_list)
        try:
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into SqliteDb_developers table")
        except sqlite3.IntegrityError:
            choice = int(input("Entry already present..Do you want to update the entry? 1-Yes, 2-No: "))
            if choice == 1:

                cursor.execute(sqlite_replace_with_param, data_tuple)
                sqliteConnection.commit()
                print("Okay As you wish!! updated the entries")
            elif choice == 2:
                print("Got it.. entry not added..")
            else:
                print("Invalid choice of operation..")

def fetch_entry():

    dbname = input("Enter the db name: ").upper()

    try:
        db_fetch_name = cursor.execute(f"select * from DB_CRED where DBNAME = '{dbname}' ;").fetchone()[1]
        print("Match Found...")
        my_password = cursor.execute(f"select PASSWORD from DB_CRED where DBNAME = '{dbname}';").fetchone()[0]
        print(my_password)
        print(type(my_password))
        password = my_password.encode()
        print(type(password))
        print(password)
        key = cursor.execute(f" select KEY from DB_CRED where DBNAME = '{dbname}';").fetchone()[0]
        f = Fernet(key)
        decMessage = f.decrypt(password).decode()
        print("Password: ",decMessage)


    except TypeError:
        print("No Matchign records found...")



choice = int(input("Enter your choice 1-Add Items, 2-Fetch Password: "))
if choice == 1:
    insert_entry()
elif choice == 2:
    fetch_entry()
else:
    print("Check your choice")

cursor.close()
