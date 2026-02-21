
def show_balance(balance):
    print(f'Your current bank account balance is: ${balance:.2f}')

def main():
    balance = 0
    is_running = True

    while is_running:
        print('\n --- Welcome to Wells Fargo Bank ---')
        print('Select an option:')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

        choice = input('Pick an option (1-4) ')

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            amount = float(input('Enter the amount you would like to deposit: '))
            if amount < 0:
                print('DEPOSIT INVALID')
            else:
                balance += amount
                print(f'{amount:.2f} deposited!')
        elif choice == '3':
            amount = float(input('Enter amount to withdraw: '))
            if amount > balance:
                print(f'DECLINED, Your current balance is ${balance:.2f}')
            elif amount < balance:
                balance -= amount
                print(f'${amount:.2f} withdrawn!')
        elif choice == '4':
            is_running = False
            print('Thank you for using our bank!')
        else:
            print('Invalid Choice!')

if __name__ == '__main__':
    main()







