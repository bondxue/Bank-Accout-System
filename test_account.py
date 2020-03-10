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


if __name__ == '__main__':
    main()
