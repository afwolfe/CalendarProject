"""
Calendar
Name: 
Period/Core: 

For this assignment, you will create a calendar program that allows the user to enter a day, month, and year and then ask them if they'd like to know how many days are left in the month or how many are left in the year.
"""

import os
import importlib.util

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command) # Run pytest command

### BEGIN EDITING HERE
"""
You'll need to define your 3 functions here.
* `is_leap_year(year)`: This function should take the year entered by the user as a parameter. This function should return `True` if a year is a leap year, and `False` if it is not. This information will be used by other functions. [What is a Leap Year?](https://www.timeanddate.com/date/leapyear.html)
* `number_of_days(month, year)`: This function should take integers representing the month and year entered by the user as parameters. This function should return an integer with [how many days are in the given month](https://www.timeanddate.com/calendar/months/).
* `days_left_in_year(day, month, year)`: This function should take integers representing the day, month, and year entered by the user as parameters. This function should calculate the number of days left in the year, and return an integer with of number of days left. The date the user entered should **not** be included in the count of how many days are left.
"""

def main():
  """This function should contain the main code for your Calendar.
  Put the input prompts here and call your other functions from here.
  """
  x = int(input("How many numbers do you need to check?"))


  # Are the commands in your main function indented?

### STOP EDITING HERE

if __name__ == "__main__":
  main() # Call main function
  t = input("Run pytest? (y/n)").lower() # Ask to run Pytest
  if t == 'y':
    run_tests()
