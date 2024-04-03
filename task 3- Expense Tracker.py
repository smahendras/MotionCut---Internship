def printMenu():
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
    print("S-NO. " , " Amount" , " Category")
    for expense in expenses:
        print("#", counter , "-" , expense["amount"] ,"-" ,expense["category"])
        counter +=1

    print("\n\n")

def removeExpense():
    while True:
        listExpenses()
        print("which Expense whould like to remove?")

        try:
            expensetoRemove = int(input("> "))
            del expenses[expensetoRemove]
        except:
            print("Invalid Entry , Please try again!!!")



if __name__ == "__main__":
    while True:
        #promt the user
        printMenu()
        optionSelected = input("> ")

        if(optionSelected == '1'):
            print("how much was this expense?")

            while True:
                try:
                    amounttoAdd = input("> ")
                    break

                except:
                    print("Invalid Entry , Please try again!!!")

            print("what is the category of this expense")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                    print("Invalid Entry , Please try again!!!")

            addExpense(amounttoAdd,category)

        elif(optionSelected == '2'):
            removeExpense()

        elif(optionSelected == '3'):
            listExpenses()

        else:
            print("invalid selection , try again")
