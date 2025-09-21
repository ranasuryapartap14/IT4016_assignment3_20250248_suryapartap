#This IS A program which collects staff information  and automatically 
#generates a unique requisition ID for each of the entry. 
#after that it collect which definde staff id information
# after generate the unique id then print the collect information 
def Staff_Info():
    global Requisition_ID_counter
    
    Staff_Date = input("Enter staff date (dd/mm/yy): ")
    Staff_ID = input("Enter staff ID: ")
    Staff_Name = input("Enter Staff Name: ")
    
    Requisition_ID_counter += 1
    Requisition_ID = Requisition_ID_counter

    print("\nStaff Information")
    print(f"Staff Date: {Staff_Date}")
    print(f"Staff ID: {Staff_ID}")
    print(f"Staff Name: {Staff_Name}")
    print(f"Requisition ID: {Requisition_ID}")

    return Staff_Date, Staff_ID, Staff_Name, Requisition_ID

from assignmet_A import *
# This program collects staff information and requisition items and it also calculate the total cost of all requitions itme.
# it will import the information from the assignment_A and then it calluclate the total requition value.
#after that ask how many requition item will be entered and show the loop through each item and and its price to the total.
#then display the final, total.
def Requisitions_Total():
    Staff_Date, Staff_ID, Staff_Name, Requisition_ID = Staff_Info()
    
    num_items = int(input("How many requisition items? "))
    total = 0
    
    for i in range(num_items):
        item_name = input(f"Enter item {i+1} name: ")
        item_price = float(input(f"Enter {item_name} price: $"))
        total += item_price
    
    print(f"\nTotal Requisition Value: ${total}")
    
    return Staff_Date, Staff_ID, Staff_Name, Requisition_ID, total 

from assignment_task2 import *
# This program is checking that if a requisition is approved based on the total value 
# and it show if the total requition value is less then 500 it is aproved automatically.
# and approval reference number is generated using the staff id.
# and it is import the information form the assignment_task2 requition_approval().
# then default the status and approval reference and create the approval condition if total is more then 500.
#after that  display the result.
def Requisition_Approval():
    Staff_Date, Staff_ID, Staff_Name, Requisition_ID, total = Requisitions_Total()
    
    status = "Pending"
    approval_ref = "N/A"
    
    if total < 500:
        status = "Approved"
        approval_ref = Staff_ID + str(Requisition_ID)[-3:]
    
    print(f"\nTotal: ${total}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {approval_ref}")
    
    return Staff_Date, Staff_ID, Staff_Name, Requisition_ID, total, status, approval_ref 

#This program displays the complete requisition details and it calls the requition approval to get staff 
# information and requition detail, staff id and total and finally it print all of the information in clear format.

from assignment_task3 import *

def Display_Requisitions():
    Staff_Date, Staff_ID, Staff_Name, Requisition_ID, total, status, approval_ref = Requisition_Approval()
    
    print("\nPrinting Requisitions:")
    print(f"Date: {Staff_Date}")
    print(f"Requisition ID: {Requisition_ID}")
    print(f"Staff ID: {Staff_ID}")
    print(f"Staff Name: {Staff_Name}")
    print(f"Total: ${total}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {approval_ref}")

Display_Requisitions()
