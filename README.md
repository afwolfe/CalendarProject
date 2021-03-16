# Calendar

## Description:
For this assignment, you will create a calendar program that allows the user to enter a day, month, and year in three separate variables as shown below.

```
Please enter a date
Day: 
Month: 
Year:
```

Then, your program should ask the user to select from a menu of choices using this formatting:

```
Menu:
1) Calculate the number of days in the given month.
2) Calculate the number of days left in the given year.
```
If a user chooses option one, the program should display how many days are in the month that they entered. If a user chooses option two, the program should display how many days are left in the year from the date that they entered.


## Functions

Your program must include the three following functions:

* `is_leap_year(year)`: This function should take the year as an integer parameter. This function should return `True` if a year is a leap year, and `False` if it is not. This information will be used by other functions. [What is a Leap Year?](https://www.timeanddate.com/date/leapyear.html)
* `number_of_days(month, year)`: This function should take integers representing the month and year entered by the user as parameters. This function should return an integer with [how many days are in the given month](https://www.timeanddate.com/calendar/months/).
* `days_left_in_year(day, month, year)`: This function should take integers representing the day, month, and year entered by the user as parameters. This function should calculate the number of days left in the year, and return an integer with of number of days left. The date the user entered should **not** be included in the count of how many days are left.

You should write well-formatted docstrings that explain the purpose, parameters, and return values of your functions.

## Hints

1. Start by defining your variables, using comments. You will need a separate variable for `day`, `month`, and `year` that store numbers input from the user.
2. Make sure to name your three functions exactly as they are named above, and pass the parameters exactly in the order specified below:
   * `is_leap_year(y)`
   * `number_of_days(m, y)`
   * `days_left_in_year(d, m, y)`
3. Make sure you write docstrings explaining what each function does.
4. Once you have `is_leap_year()` finished, that function should be called within your `number_of_days()` function. February can have either 28 or 29 days, so your `number_of_days()` function needs to take into account whether or not it is a leap year.
5. Once you have a function that calculates the number of days in a given month, that function should be called within your `days_left_in_year()` function. Different months have different numbers of days, so your `days_left_in_year()` function needs to take into account what month of the year it is.

## Sample Run 1
```
Please enter a date
Day: 5
Month: 5
Year: 1984
Menu:
1) Calculate the number of days in the given month.
2) Calculate the number of days left in the given year.
1
31
```


## Sample Run 2
```
Please enter a date
Day: 21
Month: 6
Year: 2016
Menu:
1) Calculate the number of days in the given month.
2) Calculate the number of days left in the given year.
2
193
```


## Enhancements
Add at least two of the following enhancements or come up with your own!
* Add data validation to your inputs to keep repeating until the user inputs a valid day, month, year, and mode.
* Add an additional mode and write an additional function to add features such as:
  * Calculate the number of days until a certain date or holiday. (You can do multiple special dates.)
  * Calculate the day of the week for the date. 
    * [ArtOfMemory "Mind Performance Hacks"](https://artofmemory.com/blog/how-to-calculate-the-day-of-the-week-4203.html)
    * [John Conway's Doomsday Algorithm](https://www.timeanddate.com/date/doomsday-weekday.html)
  * ???