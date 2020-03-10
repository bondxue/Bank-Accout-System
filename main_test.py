from account import Account
from time_zone import TimeZone


def main():
    a = Account('A100', 'Eric', 'Idle', timezone=TimeZone('MST', -7, 0), initial_balance=100)
    print(a.balance)
    print(a.deposit(150.02))
    print(a.balance)
    print(a.withdraw(0.02))
    print(a.balance)
    Account.set_interest_rate(1.0)
    print(a.get_interest_rate())
    print(a.pay_interest())
    print(a.balance)
    print(a.withdraw(1000))


if __name__ == '__main__':
    main()
