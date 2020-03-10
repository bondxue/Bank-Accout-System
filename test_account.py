from account import Account


def main():
    # test validate name property
    try:
        a = Account('12345', 'John', '')
    except ValueError as ex:
        print(ex)

    a = Account('12345', 'Alex', 'Martelli')
    print(a.first_name, a.last_name, a.full_name)

    # test adding preferred timezone property
    try:
        a = Account('123', 'John', 'Smith', '-7:00')
    except ValueError as ex:
        print(ex)

    a = Account('123', 'John', 'Smith')
    print(a.timezone)

    # test balance
    a = Account('1234', 'John', 'Smith', initial_balance=100)
    print(a.balance)

    # try to set balance, it should raise error
    try:
        a.balance = 200
    except AttributeError as ex:
        print(ex)

    # # test interest
    # a1 = Account(1234, 'Monty', 'Python', initial_balance=0)
    # a2 = Account(2345, 'John', 'Cheese', initial_balance=0)
    # print(a1.interest_rate, a2.interest_rate)
    #
    # Account.interest_rate = 0.025
    # print(a1.interest_rate, a2.interest_rate)

    # test class method of getter and setter for interest rate
    print(Account.get_interest_rate())

    Account.set_interest_rate(10)
    print(Account.get_interest_rate())

    try:
        Account.set_interest_rate(-10)
    except ValueError as ex:
        print(ex)

    try:
        Account.set_interest_rate(1 + 1j)
    except ValueError as ex:
        print(ex)


if __name__ == '__main__':
    main()
