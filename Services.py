from db import create_table, user_not_present_db, update_entry_time_db, update_exit, get_entry_time, new_employee_db, delete_record_db, update_employee_details, user_not_present_db, show_details_one_emp
from datetime import datetime


def get_entry(employee_id):## function to record the employeee entry time
    # Check if the employee ID exists in the DataFrame
    if user_not_present_db(employee_id):
        print("Employee found.")
    
    entry_time = datetime.now().time()
    update_entry_time_db(employee_id, entry_time)
    return "Entry time recorded"


def get_exit(employee_id):
    update_exit(employee_id)
    return "Exit time recorded"
    
    


def new_employee():
        employeeid = int(input("plezz enter your employe id : "))##taking input from the user 
        name = input("plezz enter your Name :")
        Address = input("plezz enter the address :")
        Mobile_no = int(input("plezz enter your Mobile_no :"))
        Date = datetime.now().date()
        Entry_time = "none"
        Exit_time = "none"
        new_employee_db(employeeid, name, Address, Mobile_no, Date, Entry_time, Exit_time)
        return
        
        
        
        
        #df.loc[len(df)] = {'EmployeeID': employeeid , ##usicg loc function to select the row and add the values in the dataframe
        #'Name': name,
        #'Mobile_No': Mobie_no ,
        #'Date': "none"}
        #row = df.loc[index]
        #print(row)
        #return "New employee record is created sucessfully"##returning the value out:
    
    
    
#def check_user(employee_id):
    #if df[df['EmployeeID'] == employee_id].empty:###select the emoloyee id column and if it iis eyal to the employee id then print existing user
     #   print("New user")
      #  return new_employee()##return new employee funstion to record the data
    #else:
     #   print("Existing user")
        
        
#def existing_emp(employee_id):
    #if df[df['EmployeeID'] == employee_id].empty:###select the emoloyee id column and if it iis eyal to the employee id then print existing user
     #   print("Employee id is not Correct Plezz Enter the valid Id")
      #  return get_entry(employee_id)##return new employee funstion to record the data
    #else:
     #   print("Existing user")
        
        
        
        
        ## function to add store changes in the dataframe
#def save_changes():
    #df.sort_values('EmployeeID',inplace = True)
    #df.sort_index(inplace = True)
    
    #df.to_csv("attendance_data.csv",index =False)
    #return "Thank you "


def delete_record(employee_id):
    delete_record_db(employee_id)
    print("Employe details has been removed sucessfully")
    return "Employe details has been removed sucessfully"




#def update_detail():
    #employee_id = int(input("Enter your Employee ID: "))
    
    # Check if the employee ID is in the DataFrame
    #if employee_id not in df['EmployeeID'].values:
     #   print("Employee ID not found.")
    #else:
        # Get the index of the row with the specified Employee ID
     #   index = df[df['EmployeeID'] == employee_id].index[0]
        
        # Update the values
      #  name = input("Enter your Name: ")
       # mobile_no = int(input("Enter your Mobile Number: "))
        #date = input("Enter the Date: ")

        # Using .loc to update the values in the DataFrame
        #df.loc[index, ['Name', 'Mobile_No']] = [name, mobile_no]

        #print("Employee information updated successfully.")
        #row = df.loc[index]
        #print(row)
        
        
 
def update_details():
    employee_id = int(input("Enter your Employee ID: "))
    if not user_not_present_db(employee_id):
        print("Employee found.")
        new_name = input("Enter the new Name: ")
        new_mobile_no = int(input("Enter the new Mobile_no: "))
        
        update_employee_details(employee_id, new_name, new_mobile_no)
    
    
    
    else:
       print("employee details has been updated sucesfully")
        
    

def user_not_found(employee_id):
    user_not_present_db(employee_id)
    print("Employee found.")
    


def show_one_emp_detail():
    show_details_one_emp()
    return