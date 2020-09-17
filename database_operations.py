import _sqlite3

def connection():
    try:
        conn = _sqlite3.connect("Music.sqlite")
        return  conn
    except Exception as error:
        print(error)

def create_table(conn, sql):
    try:
       cur = conn.cursor()
       cur.execute(sql)
       print("Table Successfully created!")
    except Exception as error:
        print(error)

def insert_records(con, sql, param):
    try:
        cur = con.cursor()
        cur.execute(sql, param)
        con.commit()
        return cur.lastrowid
    except Exception as error:
        print(error)

def update_records(con, sql, param):
    try:
       cur = con.cursor()
       cur.execute(sql, param)
       con.commit()
       return "Updated Successfully"
    except Exception as error:
        print(error)

def delete_all_records(con, sql):
    try:
       cur = con.cursor()
       cur.execute(sql)
    except Exception as error:
        print(error)

def delete_some_records(con, sql, param):
    try:
        cur = con.cursor()
        cur.execute(sql, param)
    except Exception as error:
        print(error)

def select_all_records(con, sql):
    print("Printing All Records...")
    try:
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except Exception as error:
        print(error)

def select_some_records(con, sql, param):
    print("Retriving Records of Input Id... ")
    try:
       cur = con.cursor()
       cur.execute(sql, param)
       rows = cur.fetchall()
       for row in rows:
         print(row)
    except Exception as error:
        print(error)




# A global connection object (Music Database)
conn = connection()

def Main():
    while True:
        print("Select The Operation You Want To Execute: "
              "1. For Create Table\n"
              "2. For Inserting Records\n"
              "3. For Updating Records\n"
              "4. For Deleting All Records\n"
              "5. For Deleting Selected Records\n"
              "6. For Viewing All Records\n"
              "7. For Viewing A Particular Record\n")
        choice = input()
        if choice == "1":
            sql = '''
                create table IF NOT EXISTS Track
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                track_name Text,
                track_genre Text,
                artiste Text,
                producer Text,
                duration Text
                )
                '''
            create_table(conn, sql)
        elif choice == "2":
            sql = '''
                INSERT INTO Track (track_name, track_genre, artiste, producer, duration)
                values(?, ?, ?, ?, ?)
            '''
            print("Enter Track Name")
            track_name = input()
            print("Enter Track Genre")
            genre = input()
            print("Enter Artiste")
            artiste = input()
            print("Enter Producer")
            producer = input()
            print("Enter Duration")
            duration = input()

            param = (track_name, genre, artiste, producer, duration)
            record_id = insert_records(conn, sql, param)
            if record_id > 0:
                print("Records Successfully Inserted: ", record_id)
        elif choice == "3":
            print("What record do you want to update\n"
                  "\n 1. for track_name"
                  "\n 2. for track_genre"
                  "\n 3. for artiste"
                  "\n 4. for producer"
                  "\n 5. for duration")
            choice_update = input()
            col_to_update = "track_name"
            _new = ""
            if choice_update == "1":
                col_to_update = "track_name"
                print("Enter New Track Name: ")
                _new = input()
                print("Enter ID: ")
                _id = input()
            elif choice_update == "2":
                col_to_update = "track_genre"
                print("Enter New Track Genre: ")
                _new = input()
                print("Enter ID: ")
                _id = input()
            elif choice_update == "3":
                col_to_update = "artiste"
                print("Enter New Artiste Name: ")
                _new = input()
                print("Enter ID: ")
                _id = input()
            elif choice_update == "4":
                col_to_update = "producer"
                print("Enter New Producer Name: ")
                _new = input()
                print("Enter ID: ")
                _id = input()
            elif choice_update == "5":
                col_to_update = "duration"
                print("Enter New Duration: ")
                _new = input()
                print("Enter ID: ")
                _id = input()
            else:
                print("Invalid Option Selected")
            sql = " Update Track set "+ col_to_update+"=? where id=? "
            param = (_new, _id)
            print(_new, col_to_update)
            update_records(conn, sql, param)
        elif choice=="4":
            delete_all_records(conn, "DELETE FROM track")
        elif choice=="5":
            print("Input Id of Track you want to delete: ")
            _id = input()
            delete_some_records(conn, "DELETE FROM track where id=?", _id)
        elif choice=="6":
            select_all_records(conn, "select * from track")
        elif choice=="7":
            sql_statement ="SELECT * FROM Track where id=?"
            print("Input an ID OF record to view: ")
            _id = input()
            select_some_records(conn, sql_statement, _id)
Main()