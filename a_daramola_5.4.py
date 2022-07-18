#Akinola Daramola Jr
#Programming Exercise 5.4
#Due Date: 07/12/2022

"""
Automobile Costs
Write a program that asks the user to enter the monthly costs
for the following expenses incurred from operating his or her automobile:
loan payment, insurance, gas, oil, tires, and maintenance.
The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.
"""



def main():
    caluclate()

    
#Defining functions
def caluclate():
    
    #Declaring value of varibales
    months = 12 
    loan_payment = float(input("Enter loan payment amount: "))
    insurance_payment = float(input("Enter insurance payment amount: "))
    gas = float(input("Enter gas amount: "))
    oil = float(input("Enter oil amount: "))
    tires = float(input("Enter tires amount: "))
    maintenance = float(input("Enter maintenance amount: "))
    
    #Calculating value of all monthly expenses
    total_monthly_cost = loan_payment + insurance_payment + gas + oil + tires + maintenance
    
    #Calculating value of annual expenses
    total_annual_expense = total_monthly_cost * months

    #Displaying total amount of monthly expenses
    print(f"Total Monthly Expense: ${total_monthly_cost:,.2f}")
    
    #Displaying total amount of annual expenses
    print(f"Total Annual Expense: ${total_annual_expense:,.2f}")

#Calling function
main()
    
