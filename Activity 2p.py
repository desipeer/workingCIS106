# a program that asks the user how old they are in years, and then calculate and display their approximate age in months, days, hours, and seconds.

import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime
print("Enter the year you were born:")
birthYear = (input())
print("Enter the month of " + str(birthYear) +
      " that you were born in. Use numbers only i.e., 1 for January, 2 for February, etc.:")
birthMonth = (input())
print("Enter the date of the month that you were born on:")
birthDate = (input())

now = datetime.now()

inYears = int(now.year)-int(birthYear)

print("Your age is " + str(inYears))

inMonths = (int(now.year) - int(birthYear)) * 12
print("Your age in months is " + str(inMonths))
birthday = datetime(int(birthYear), int(birthMonth), int(birthDate))
age = now-birthday

print("Your age in days, minutes, and seconds is " + str(age))

print("as of " + str(now))
