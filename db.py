## connectind Database
import mysql.connector
from datetime import datetime

def connect_db():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Ritik@1234",
        database = "proffessor",

    )
    print(mydb)
    return mydb

#cursor.execute("CREATE TABLE Epmloyee_details")

def create_table():
    mydb = connect_db()
    cursor = mydb.cursor()

    create_query = """CREATE TABLE Employee_details(
    Employee_id INTEGER PRIMARY KEY,
    Name VARCHAR(255),
    Address VARCHAR(255),
    Mobile BIGINT,
    Date VARCHAR(255),
    Entry_time VARCHAR(255),
    Exit_time VARCHAR(255)
    );"""
    cursor.execute(create_query)
    cursor.close()
       
        

def user_not_present_db(employee_id):
    mydb = connect_db()
    cursor = mydb.cursor()

    
    # Assuming db is your database connection and cursor is your cursor object
    select_query = f"SELECT * FROM Employee_details WHERE Employee_id = '{employee_id}'"
    
    cursor.execute(select_query)
    data = cursor.fetchone()

    if not data:
        # Employee does not exist
        print(f"Employee ID {employee_id} does not exist in Employee_details.")
    cursor.close()
    mydb.close()


def update_entry_time_db(employee_id, entry_time):
    mydb = connect_db()
    cursor = mydb.cursor()

    update_query = "UPDATE Employee_details SET Entry_time = %s WHERE Employee_id = %s"
    cursor.execute(update_query, (entry_time, employee_id))
    print(f"Entery time recorded for {employee_id} Sucessfully")
    mydb.commit()
    show_details(employee_id)
    cursor.close()
    mydb.close()
    
    
  
def update_exit(employee_id):
    mydb = connect_db()
    try:
    
        cursor = mydb.cursor()

            # Check if the entry time is present for the employee
        entry_time = get_entry_time(employee_id)
        
        if entry_time is not None:
            # Entry time is present, record exit time
            exit_time = datetime.now().time()
            update_exit_query = "UPDATE Employee_details SET Exit_time = %s WHERE employee_id = %s"
            cursor.execute(update_exit_query, (exit_time, employee_id))
            mydb.commit()
            print("Exit time recorded.")
            show_details(employee_id)
        else:
            # Entry time is not present
            print("Entry time is not recorded for the employee.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        mydb.close()
    
  
def get_entry_time(employee_id):
    mydb = connect_db()
    cursor = mydb.cursor()

    # Fetch the entry time for the employee
    try:
        select_query = "SELECT Entry_time FROM Employee_details WHERE Employee_id = %s"
        cursor.execute(select_query, (employee_id,))
        entry_time = cursor.fetchone()
        #print(entry_time)
        return entry_time

    except Exception as e:
        #print(e)
        return e



def new_employee_db(employee_id, name, Address, Mobile_no, Date, Entry_time, Exit_time):
    mydb = connect_db()
    cursor = mydb.cursor()

    insert_query = """INSERT INTO Employee_details (employee_id, Name, Address, Mobile, Date, Entry_time, Exit_time) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    values = (employee_id, name, Address, Mobile_no, Date, Entry_time, Exit_time)

    cursor.execute(insert_query, values)
    mydb.commit()
    print ("New employee record is created sucessfully")
    show_details(employee_id)
    cursor.close()
    mydb.close()
    
    
    
def delete_record_db(employee_id):
    mydb=connect_db()
    cursor = mydb.cursor()
    delete_data = "DELETE FROM Employee_details Where employee_id = 104"
    cursor.execute(delete_data)
    cursor.close()
    mydb.close()
    
    
    

def update_employee_details(employee_id, new_name, new_mobile_no):
    mydb=connect_db()
    cursor = mydb.cursor()
    
    update_query = "UPDATE Employee_details SET Name = %s, Mobile = %s WHERE employee_id = %s"
    values = (new_name, new_mobile_no, employee_id)
    
    cursor.execute(update_query, values)
    mydb.commit()
    show_details(employee_id)

    print(f"Employee details with ID {employee_id} updated successfully.")


    #update_employee_details(employee_id, new_name, new_mobile_no)
    
def show_details(employee_id):
    mydb=connect_db()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * from Employee_details WHERE employee_id = %s", (employee_id,))
    data_fetch =  cursor.fetchone()
    print(data_fetch)
    cursor.close()
    mydb.close()
    return data_fetch



def show_details_one_emp():
    mydb=connect_db()
    cursor = mydb.cursor()
    try:
        employee_id = int(input("Enter your Employee id"))
        cursor.execute(f"SELECT * from Employee_details WHERE employee_id = %s", (employee_id,))
        data_fetch =  cursor.fetchone()
        print(data_fetch)
    except Exception as e:
        print(f" error:{e}")
    finally:
        cursor.close()
        mydb.close()
        
    
    

