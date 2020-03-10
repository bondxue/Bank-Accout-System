from account import Account
from time_zone import TimeZone

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

    # # test for transaction
    # a = Account('A100', 'John', 'Cleese', initial_balance=100)
    # print(a.make_transaction())

    # # test parse confirmation code
    # a = Account('A100', 'John', 'Cleese', initial_balance=100)
    # conf_code = a.make_transaction()
    # print(conf_code)
    #
    # print(Account.parse_confirmation_code(conf_code))

    # # test parse confirmation code with timezone
    # print(Account.parse_confirmation_code(conf_code, TimeZone('MST', -7, 0)))
    #
    # try:
    #     Account.parse_confirmation_code('X-A100-asdasd-123')
    # except ValueError as ex:
    #     print(ex)

    # test transaction methods
    a = Account('A100', 'Eric', 'Idle', TimeZone('MST', -7, 0), 100.0)
    print(a.balance)

    a.deposit(100)
    print(a.balance)

    a.withdraw(100)
    print(a.balance)


if __name__ == '__main__':
    main()
