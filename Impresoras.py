def min_days_to_print(n):
    days = 0
    printers = 1
    statues = 0

    while statues < n:
        if printers >= (n - statues):
            days += 1
            break

        if printers * 2 <= (n - statues):
            printers *= 2
        else:
            statues += printers

        days += 1

    return days

n = int(input())
print(min_days_to_print(n))