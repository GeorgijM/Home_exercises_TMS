def create_calendar_page(month, year):
    day = 1  # First date in a month
    weekdays = 'MO TU WE TH FR SA SU'

    days_quantity_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    month_before_change = month  #Will use it for getting dict items after changing value in variable 'month'.
    # Changing quantity in february for leap year.
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days_quantity_in_month[2] = 29

    days = weekdays + '\n'  # New string for print
    # Will find which day of the week on the first month day, 1 - monday.. 5 - friday .. 0 - sunday.
    if month < 3:
        year -= 1
        month += 10
    else:
        month -= 2

    first_day_in_the_week = (day + 31 * month // 12 + year + year // 4 - year // 100 + year // 400) % 7
    # Adding spaces, zeros and new strings before date numbers.
    if first_day_in_the_week > 1:
        for j in range(1, first_day_in_the_week):  # Printing spaces for starting in right place.
            days += '   '
    for i in range(1, 10):
        days += '0' + str(i) + ' '  # Adding zeros for printing 01, 02..09 instead of 1, 2..9
        if first_day_in_the_week + i == 8:
            days += '\n'  # new string for printing in calendar table
    for i in range(1, days_quantity_in_month[month_before_change] - 8):
        if (first_day_in_the_week + 7 + i) % 7 == 0:
            days += '\n'
        days += str(i + 9) + ' '
    return days

(print(create_calendar_page(8, 2022)))
#(print(create_calendar_page(2, 2000)))
#(print(create_calendar_page(2, 1900)))

