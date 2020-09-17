import _sqlite3

def connection_object():
    try:
        conn = _sqlite3.connect("Python_School.sqlite")
        return conn
    except Exception as error:
        print(error)

def create_table(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        print("Created Student Records Table Successfully")
    except Exception as error:
        print(error)

def insert_table(conn, sql, param):
    try:
        cur = conn.cursor()
        cur.execute(sql, param)
        conn.commit()
        return cur.lastrowid
    except Exception as error:
        print(error)

def update_table(conn, sql, param):
    try:
        cur = conn.cursor()
        cur.execute(sql, param)
        conn.commit()
    except Exception as error:
        print(error)

def delete_all_records(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
    except Exception as error:
        print(error)

def delete_some_records(conn, sql, param):
    try:
        cur = conn.cursor()
        cur.execute(sql, param)
    except Exception as error:
        print(error)

def select_all_records(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as error:
        print(error)

def select_some_record(conn, sql, param):
    try:
        cur = conn.cursor
        cur.execute(sql, param)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as error:
        print(error)

# Global Connection Object (Python School Database)

conn = connection_object()


def Main_GUI_Controls():
    while True:
        print(
            '''
            Select the Operation You Want To Execute\n
            1. For Creating A Table\n
            2. For Inserting Student Records in a Table\n
            3. For Updating Student Records in a Table\n
            4. For Deleting All Student Records\n
            5. For Deleting Selected Student Records\n
            6. For Selecting All Student Records\n
            7. For Viewing A Particular Student Record\n
            '''
        )
        execution_choice = input()
        if execution_choice == "1":
            sql = '''
            create Table IF NOT EXISTS student_records
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name Text,
            last_name Text,
            email Text,
            phone Text,
            course Text,
            duration Text
            )
            '''
            create_table(conn, sql)
        elif execution_choice == "2":
            sql = '''
            Insert into student_records (first_name, last_name, email, phone, course, duration)
            values (?,?,?,?,?,?)
            '''
            print("Enter Student's First Name")
            first_name = input()
            print("Enter Student's Last Name")
            last_name = input()
            print("Enter Student's Email")
            email = input()
            print("Enter Student's Phone Number")
            phone = input()
            print("Enter Student's Course")
            course = input()
            print("Enter Student's Course Duration")
            duration = input()

            param = (first_name, last_name, email, phone, course, duration)
            student_records_id = insert_table(conn, sql, param)
            if student_records_id > 0:
                print("Student records have been successfully inserted")
        elif execution_choice == "3":
            print('''
            Choose data to update:\n
            1. Update First Name\n
            2. Update Last Name\n
            3. Update Email Address\n
            4. Update Phone Number\n
            5. Update Course\n
            6. Update Course Duration\n 
            ''')
            update_choice = input()
            col_to_update = "first_name"
            _new = ""
            if update_choice == "1":
                col_to_update = "first_name"
                print("Enter New First Name: ")
                _new = input()
                print("Enter ID: ")
                _id = int(input())
            elif update_choice == "2":
                col_to_update = "last_name"
                print("Enter New Last Name: ")
                _new = input()
                print("Enter ID: ")
                _id = int(input())
            elif update_choice == "3":
                col_to_update = "email"
                print("Enter New Email Address: ")
                _new = input()
                print("Enter ID: ")
                _id = int(input())
            elif update_choice == "4":
                col_to_update = "phone"
                print("Enter New Phone Number: ")
                _new = input()
                print("Enter ID: ")
                _id = int(input())
            elif update_choice == "5":
                col_to_update = "course"
                print("Enter New Course: ")
                _new = input()
                print("Enter ID: ")
                _id = int(input())
            elif update_choice == "6":
                col_to_update = "duration"
                print("Enter New Course Duration: ")
                _new = input()
                print("Enter ID: ")
                _id = int(input())
            else:
                print("Invalid Update Option Selected")
            sql = " Update student_records set " + col_to_update + "=? where id=? "
            param = (_new, _id)
            print(_new, col_to_update)
            update_table(conn, sql, param)
        elif execution_choice == "4":
            sql = "DELETE FROM student_records"
            delete_all_records(conn, sql)
        elif execution_choice == "5":
            print("Enter record ID to delete: ")
            _id = int(input())
            sql = "Delete from student_records where id=?"
            delete_some_records(conn, sql, _id)
        elif execution_choice == "5":
            sql = "select * from student_records"
            select_all_records(conn, sql)
        elif execution_choice == "6":
            print("Enter record ID to select and view: ")
            _id = int(input())
            sql = "select * from student_records where id=?"
            select_some_record(conn, sql, _id)

Main_GUI_Controls()