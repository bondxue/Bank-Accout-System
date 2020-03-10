from account import Account


def main():
    try:
        a = Account('12345', 'John', '')
    except ValueError as ex:
        print(ex)

    a = Account('12345', 'Alex', 'Martelli')
    print(a.first_name, a.last_name, a.full_name)

if __name__ == '__main__':
    main()
