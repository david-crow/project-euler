# You are given the following information, but you may prefer to do some research for yourself.
    # 1 Jan 1900 was a Monday.
    # Thirty days has September,
    # April, June and November.
    # All the rest have thirty-one,
    # Saving February alone,
    # Which has twenty-eight, rain or shine.
    # And on leap years, twenty-nine.
    # A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

day, count, days_for_months = (1 + 365) % 7, 0, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year in range(1901, 2001):
    for month in range(12):
        if day % 7 == 0: count += 1
        day = day + days_for_months[month] + \
            (1 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month == 1 else 0)

print(count)
