"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime
from datetime import date


# jar = input("Enter comma-separated numbers: ").split(',')

# jar= input('Enter comma separated numbers:').split(',') 
today=date.today()
print(f' today: {today}')

# if no input on file call print calendar for current  month
# how to print current month
# how to print a calendar by parameter

# how to accept inputs on the initial call of a file
# if use passes in a single argument assume its for the month print that months calendar for this year


# if user passes in two arguments on initial file call assume they passed in both the month and the year render a calendar for that month/year combo

# otherwise print a usage statement to the terminal indicating the format this program expects arguments to be passed in and then exit the program
# I.E. tell the user how to run the program correectly then close so they can try again




currentMonth  = datetime.now().month
currentYear   = datetime.now().year
selectedMonth = currentMonth
selectedYear  = currentYear
currentMonthCal      = f'Showing Calendar for the current month\n{calendar.month(currentYear,currentMonth)}'

if len(sys.argv)>1:
  selectedMonth
  selectedMonth= int(sys.argv[1])
  selectedMonthCal     = f'Showing Calendar for the selected month\n{calendar.month(currentYear,selectedMonth)}'
if len(sys.argv)>2:
  selectedYear
  selectedYear=  int(sys.argv[2])
  selectedYearMonthCal = f' Showing Calendar for the selected year and month:\n{calendar.month(selectedYear,selectedMonth)}'


def printCalendar():
    if len(sys.argv) ==1:
      print(f'zero args{True} \n {currentMonthCal}')
    elif len(sys.argv) ==2:
      print(  f'one arg{True}  \n {selectedMonthCal}')
    elif len(sys.argv)==3:
      print( f'two args{True}  \n {selectedYearMonthCal}')
    elif len(sys.argv)>=4:
      print( f'This program accepts user input of the form\n\'14_cal.py [month] [year]\'\nand does the following:\n - If the user doesn\'t specify any input, program  will print the calendar for the current month. \n - If the user specifies one argument, it will be assumed to be a month and will render the calendar for that month of the current year.\n - If the user specifies two arguments, they will be assumed to be both the month and the year. The Program will render the calendar for that month and year.\n - More than 2 arguments will print a usage statement to the terminal indicating the format this program expects arguments to be given.'
      )
printCalendar()