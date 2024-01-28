import pandas as pd
import pandas as pd
import mysql.connector
from datetime import datetime
from db import (
    connect_db, 
    create_table, 
    user_not_present_db, 
    update_entry_time_db,
    update_exit, 
    get_entry_time, 
    new_employee_db, 
    delete_record_db,
    update_employee_details,
    show_details,
    show_details_one_emp
    
)



from Services import get_entry, get_exit, update_details, new_employee, delete_record, user_not_found, show_one_emp_detail




#pyif __name__ =='__main__':
def main():
    connect_db()
    #create_table()
    #file_path= 'attendance_data.csv'
    #df = pd.read_csv(file_path)
    print("Hello Gentleman Welcome")
    print("################ Main Menu ####################")
    #df['Date'] =  datetime.now().date()
    try:
        entry_type = int(input("Please select below\n1. Log In\n2. Registration\n3. Update Details\n4. Exit\n"))
    except ValueError :
            return "Value entered is not correct plezz enter a valid Input"
    if entry_type == 1:
        employee_id = int(input("Enter the Employee Id : "))
        if user_not_found(employee_id):
            main()
        
        else:
            Employee_choise = int(input("Welcome Team Mate\nChosse From Below\n1.Entry Time\n2.Exit Time\n3.Delete Details\n4.Show Employee details\n5.Go Back To Main Menu\n6. Exit\n"))
            if Employee_choise == 1:
                return get_entry(employee_id)
            elif Employee_choise == 2:
                return get_exit(employee_id)
            elif Employee_choise ==3:
                return delete_record(employee_id)
            
            elif(Employee_choise == 4):
                user_details = show_details_one_emp() 
                print(user_details)


            elif Employee_choise == 5:
                return main()
            elif Employee_choise == 6:
                return
        #df.sort_values('EmployeeID',inplace = True)
        #return save_changes()

    elif entry_type == 2:
        print("######### REgistration ###############")
        return  new_employee()

    elif entry_type == 3:
                update_details()


    elif entry_type == 4:  
        return "Thankyou for Visit"
    else:
        return show_details

main()