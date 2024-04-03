def printManu():
    print("What whould you like to do Choose an option...")
    print("1. Add an expense.")
    print("2. Remove an expense.")
    print("3. View all expenses.")


expenses = []
def addExpense(amount,category):
    expense = {'amount' : amount ,'category' : category}
    expenses.append(expense)

def listExpenses():

    print("\n Here is the list of expenses.")
    print("------------------------------------")
    counter=0
    print("S-NO." , "Amount" , "Category")
    for expense in expenses:
        print("#", counter , "-" , expense["amount"] ,"-" ,expense["category"])

