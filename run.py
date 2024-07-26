# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def deposit():

    print('Enter the amount you would like to deposit:')
    amount = float(input('>> '))
    
    if amount <= 0:
        print('You cannot deposit a negative or zero value...')
    else:
        return amount

def withdraw():
    pass


def show_balance():
    print(f'Your current balance is €{balance:.2f}')


balance = 0
is_running = True


while is_running:
    print('Welcome to The Bank!')
    print('[1] Deposit')
    print('[2] Withdraw')
    print('[3] Show balance')
    print('[4] Exit')

    print('Please enter your choice (1-4):')
    choice = input('>> ')

    if choice == '1':
        balance =+ deposit()
        print(f'Thank you for your deposit! Your new balance is €{balance:.2f}')
    elif choice == '2':
        withdraw()
    elif choice == '3':
        show_balance()
    elif choice == '4':
        is_running = False
    else:
        print('That is not a valid choice!')


print('Thank you! Have a nice day!')