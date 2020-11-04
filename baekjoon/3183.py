def dates(d, m, y):
    thirty_day = [4, 6, 9, 11]
    if m not in range(1, 13):
        return 'Invalid'

    # Not February
    if m != 2:
        if m in thirty_day:
            if d in range(1, 31):
                return 'Valid'
            else:
                return 'Invalid'
        else:
            if d in range(1, 32):
                return 'Valid'
            else:
                return 'Invalid'

    # February
    else:
        if leap_year(y):
            if d in range(1, 30):
                return 'Valid'
            else:
                return 'Invalid'
        else:
            if d in range(1, 29):
                return 'Valid'
            else:
                return 'Invalid'


def leap_year(y):
    if y % 400 == 0:
        return 1
    if y % 100 == 0:
        return 0
    if y % 4 == 0:
        return 1
    else:
        return 0


while True:
    day, month, year = map(int, input().split())
    if day == 0 and month == 0 and year == 0:
        break

    is_val = dates(day, month, year)
    print(is_val)
