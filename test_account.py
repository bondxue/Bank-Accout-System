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


if __name__ == '__main__':
    main()
