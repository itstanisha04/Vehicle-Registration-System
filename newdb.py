import mysql.connector as myc
import os

mydb = myc.connect(host = "localhost", user = "root", passwd = "tanu@12345", database = "vehicle_sys")
mycursor = mydb.cursor()


#FOR REGISTERING A USER

def register():
    print("=================REGISTER====================")
    print("\nEnter the User Details\n")
    id = int(input("Enter vehicle id: "))
    type = input("Enter the vehicle type: ")
    no = input("Enter the vehicle no: ")
    name = input("Enter user's name: ")
    address = input("Enter the address: ")
    phone = int(input("Enter the mobile no.: "))
    sql = 'insert into vehicle values({}, "{}", "{}", "{}", "{}", {} )'.format(id, type, no, name, address, phone)
    mycursor.execute(sql)
    mydb.commit()


#FOR SEARCHING A USER

def search():
    print("=================SEARCH====================")
    id = int(input("Enter vehicle id: "))
    sql = 'select * from vehicle where vehicle.v_id = {}'.format(id)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    if data:
        print(data[0])
    else:
        print("\nUser not found \n")


#FOR MODIFYING THE USER DETAILS

def modify():
    print("=================MODIFY====================")
    id = int(input("Enter vehicle id: "))
    sql = 'select * from vehicle where vehicle.v_id = {}'.format(id)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    if data:
        print("\nOld details of the user are: ")
        print(data[0])
        print("\nEnter the new details of the user: ")
        type = input("Enter the vehicle type: ")
        no = input("Enter the vehicle no: ")
        name = input("Enter user's name: ")
        address = input("Enter the address: ")
        phone = int(input("Enter the mobile no.: "))
        sql = 'update vehicle set vehicle.v_type = "{}", vehicle.v_no = "{}", vehicle.u_name = "{}", vehicle.u_add = "{}", vehicle.u_phone = "{}" where vehicle.v_id = {}'.format(type, no, name, address, phone, id)
        #sql = 'update vehicle set vehicle.v_type = "{}", vehicle.v_no = "{}", vehicle.u_name = "{}", vehicle.u_add = "{}" where vehicle.v_id = {}'.format(type, no, name, id)
        mycursor.execute(sql)
        mydb.commit()
        print("\nDetails Modified\n")

    else:
        print("\nUser not found \n")


#FOR DELETING THE USER DETAILS

def delete():
    print("=================DELETE====================")
    id = int(input("Enter vehicle id: "))
    sql = 'select * from vehicle where vehicle.v_id = {}'.format(id)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    if data:
        sql = 'delete from vehicle where vehicle.v_id = {}'.format(id)
        mycursor.execute(sql)
        mydb.commit()
        print("\nDetails of the particular vehicle is deleted \n")
    else:
        print("\nUser not found \n")
    



#FOR DISPLAYING THE OVERALL DATA OF USERS

def total():
    print("=================ALL DETAILS====================")
    sql = 'select * from vehicle'
    mycursor.execute(sql)
    data = mycursor.fetchall()
    for row in data:
        print(row)

#THE MAIN FUNCTION FROM WHERE THE EXECUTION BEGINS

def main():

    print("=================MAIN MENU===================")
    print("1.Register")
    print("2.Search")
    print("3.Modify")
    print("4.Delete")
    print("5.Total")
    print("6.Exit")

    choice = int(input("\nEnter your choice: "))

    while choice!=6:
        
        if(choice == 1):
            register()
    
        elif(choice == 2):
            search()
    
        elif(choice == 3):
            modify()

        elif(choice == 4):
            delete()

        elif(choice == 5):
            total()

        n = input()
        os.system('cls')
        print("=================MAIN MENU===================")
        print("1.Register")
        print("2.Search")
        print("3.Modify")
        print("4.Delete")
        print("5.Total")
        print("6.Exit")
        choice = int(input("\nEnter your choice: "))
    
    print("================THANK YOU================")


main()

#PROGRAM ENDED
