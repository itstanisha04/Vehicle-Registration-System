
import pickle
import os

#FOR ENTERING THE DETAILS AND LOAD IT INTO A TEXT FILE
def enterDetails():
    print("Enter the User Details\n")
    name = input("Enter name: ")
    type = input("Enter the vehicle type: ")
    no = input("Enter the vehicle no: ")
    address = input("Enter the address: ")
    phone = input("Enter the mobile no.: ")

    fobj = open("myfile.txt", "ab")

    str_list = []
    str_list.append(name)
    str_list.append(type)
    str_list.append(no)
    str_list.append(address)
    str_list.append(phone)
    pickle.dump(str_list, fobj)

    fobj.close()


#FOR SHOWING THE DETAILS WHEN THE ENTRY MATCHES
def showDetails(list = []):
    print("Name: ", list[0])
    print("Vehicle type: ", list[1])
    print("Vehicle no.: ", list[2])
    print("Address: ", list[3])
    print("Phone no: ", list[4])


#FOR REGISTERING A USER

def register():
    print("=================REGISTER THE USER====================")
    enterDetails()
    print("\nUser registered succesfully.")


#FOR SEARCHING A USER

def search():
    print("=================SEARCH A USER====================")
    fobj2 = open("myfile.txt", "rb")
    
    str_read = []
    while 1:
        try:
            str_read.append(pickle.load(fobj2))
        except (EOFError, pickle.UnpicklingError):
            break
        
    print("Enter the details of the user to be searched: ")
    u_type = input("Enter the vehicle type: ")
    u_no = input("Enter the vehicle no.: ")
    flag=1
    for user in str_read:
        if(user[1]==u_type and user[2]==u_no):
            flag=0
            print("\nDetails of the User:\n ")
            showDetails(user)
            

    if(flag):
        print("The user not found.")


    fobj2.close()


#FOR MODIFYING THE USER DETAILS

def modify():
    print("=================MODIFY A USER====================")
    mod = open("myfile2.txt", "wb")
    read = open("myfile.txt", "rb")
    
    str_read = []
    while 1:
        try:
            str_read.append(pickle.load(read))
        except (EOFError, pickle.UnpicklingError):
            break

    print("Enter the details of the user to be modified: ")
    u_type = input("Enter the vehicle type: ")
    u_no = input("Enter the vehicle no.: ")
    flag=1
    for user in str_read:
        if(user[1]==u_type and user[2]==u_no):
            flag=0
            print("\nThe old details of the User are: ")
            showDetails(user)
            print("\n\nEnter the new details of User")
            name = input("Enter the name: ")
            type = input("Enter the vehicle type: ")
            no = input("Enter the vehicle no: ")
            address = input("Enter the address: ")
            phone = input("Enter the mobile no.: ")

            str_list = []
            str_list.append(name)
            str_list.append(type)
            str_list.append(no)
            str_list.append(address)
            str_list.append(phone)
            pickle.dump(str_list, mod)


        else:
            pickle.dump(user, mod)

    if(flag):
        print("The user not found.")  
    else:
        print("\nDetails modified.")      

    read.close()
    mod.close()
    os.replace("myfile2.txt", "myfile.txt")


#FOR DELETING THE USER DETAILS

def delete():
    print("=================DELETE A USER====================")
    erase = open("myfile2.txt", "wb")
    read = open("myfile.txt", "rb")
   
    str_read = []
    while 1:
        try:
            str_read.append(pickle.load(read))
        except (EOFError, pickle.UnpicklingError):
            break

    print("Enter the details of the user to be deleted: ")
    u_type = input("Enter the vehicle type: ")
    u_no = input("Enter the vehicle no.: ")
    flag=1
    for user in str_read:
        if(user[1]==u_type and user[2]==u_no):
            flag=0
            print("Details of the User: ")
            showDetails(user)
        else:
            pickle.dump(user, erase)

    if(flag):
        print("The user not found.")  
    else:
        print("\nDetails deleted.")       

    read.close()
    erase.close()
    os.replace("myfile2.txt", "myfile.txt")


#FOR DISPLAYING THE OVERALL DATA OF USERS

def total():
    print("=================TOTAL USERS REGISTERED====================")

    fobj2 = open("myfile.txt", "rb")

    total_users = 0
    str_read = []
    while 1:
        try:
            str_read.append(pickle.load(fobj2))
        except (EOFError, pickle.UnpicklingError):
            break
        total_users+=1

    print("Total users are: ",total_users)
    print("\nTheir details are as follows: \n")
    for i in str_read:
        showDetails(i)
        print()

    fobj2.close()



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
