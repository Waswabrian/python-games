#My expense tracker project via freecode camp
def add_expense(expenses, amount, item):
    expenses.append({'amount': amount, 'item': item})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, item: {expense["item"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_item(expenses, item):
    return filter(lambda expense: expense['item'] == item, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by item')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            item = input('Enter item: ')
            add_expense(expenses, amount, item)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_item = filter_expenses_by_item(expenses, item)
            print_expenses(expenses_from_item)

        elif choice == '5':
            print('Exiting the program.')
            break

if __name__ == '__main__':
    main()