import calendar

# Print calendar for a specific month
print(calendar.month(2026, 9))

# Print calendar for the entire year
print(calendar.calendar(2026))

# calendar.weekday(year, month, day): Returns the day of the week as an integer
# Monday is 0, Tuesday is 1, ..., Sunday is 6
day_num = calendar.weekday(2026, 9, 27)
print("Weekday index:", day_num)  # Output: 6 (Sunday)

# calendar.day_name: An array containing the names of the days of the week
print("Day name:", calendar.day_name[day_num])  # Output: Sunday

# calendar.month_name: An array containing the names of the months
print("Month name:", calendar.month_name[9])  # Output: September

# calendar.monthrange(year, month): Returns a tuple (first_day_of_month, number_of_days)
# first_day_of_month: 0 for Monday, 1 for Tuesday, etc.
first_day, total_days = calendar.monthrange(2026, 9)
print(f"Starts on weekday index: {first_day}, Total days: {total_days}")
# Output: Starts on weekday index: 1 (Tuesday), Total days: 30


# calendar.isleap(year): Returns True if the year is a leap year, False otherwise
print("Is 2024 a leap year?", calendar.isleap(2024))  # Output: True
print("Is 2026 a leap year?", calendar.isleap(2026))  # Output: False

# calendar.leapdays(year1, year2): Returns the number of leap years between year1 and year2
# Note: year2 is exclusive (not included in the count)
print("Leap years between 2000 and 2026:", calendar.leapdays(2000, 2026))  # Output: 7


#--------------------------------------------


# prmonth(year, month): Directly prints the month (no print() statement needed)
calendar.prmonth(2026, 9)

# prcal(year): Directly prints the calendar for an entire year
calendar.prcal(2026)

#--------------------------------------------

