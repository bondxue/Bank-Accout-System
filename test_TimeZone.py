from time_zone import TimeZone
from datetime import datetime


def main():
    tz1 = TimeZone('ABC', -2, -15)
    print(tz1.name)

    dt = datetime.utcnow()
    print(dt)
    print(dt + tz1.offset)

    try:
        tz = TimeZone('', 0, 0)
    except ValueError as ex:
        print(ex)

    try:
        tz = TimeZone('ABC', 18, 0)
    except ValueError as ex:
        print(ex)


if __name__ == '__main__':
    main()
