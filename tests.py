import sol as Calendar

import random

import datetime, calendar

prompts = []
inputs = []

def mock_sample1_input(*args, **kwargs):
  return mock_cal_input(5,5,1984,1, args, kwargs)
  
def mock_sample2_input(*args, **kwargs):
  return mock_cal_input(21,6,2016,2, args, kwargs)

def mock_cal_input(d,m,y,mode,*args, **kwargs):
  """"""
  prompts.append(args[0])
  if prompts[-1]:
    if "day" in prompts[-1][0].lower():
      return d
    elif "month" in prompts[-1][0].lower():
      return m
    elif "year" in prompts[-1][0].lower():
      return y
    else:
      return mode
  else:
    return mode

def test_leap_years():
  """
  This test case runs the leap_year function with years ranging from 2000-2016.
  It expects True returned for leap years or False otherwise.
  """
  for year in range(2000, 2017):
    assert calendar.isleap(year) == Calendar.is_leap_year(year)

def test_number_of_days():
  """ 
  This test case runs number_of_days for all months.
  February is run twice, once with a leap year and once as a non-leap year.
  It checks that the number of days for all months are returned correctly.
  """

  for m in range(1,13):
    assert Calendar.number_of_days
    if m == 2:
      assert Calendar.number_of_days(m, 1999) == 28
      assert Calendar.number_of_days(m, 2000) == 29
    else:
      assert Calendar.number_of_days(m, 2000) == calendar.monthrange(2000, m)[1]

def test_random_days_left():
  """
  This test case runs days_left with various parameters and checks that the returned values are correct.
  """

  for m in range(1,13): # for each month
    if m == 2:
      days = random.sample(range(1, 29), 10)
      for d in days: # Check both leap year and non-leap year
        date = datetime.date(2000,m,d)
        assert Calendar.days_left(d, m, 2000) == (datetime.date(2000, 12, 31) - date).days
        date = datetime.date(1999,m,d)
        assert Calendar.days_left(d, m, 1999) == (datetime.date(1999, 12, 31) - date).days
    else:
      days = random.sample(range(1, calendar.monthrange(2000, m)[1]+1), 10)
      for d in days:
        date = datetime.date(2000,m,d)
        assert Calendar.days_left(d, m, 2000) == (datetime.date(2000, 12, 31) - date).days
  
def test_docstrings():
  """Checks for the existence of docstrings."""
  assert Calendar.is_leap_year.__doc__
  assert Calendar.number_of_days.__doc__
  assert Calendar.days_left.__doc__

def test_sample1(monkeypatch, capsys):
  """Using Sample Run 1 values, this test case checks for 31 in your program's output."""
  monkeypatch.setattr('builtins.input', mock_sample1_input)
  prompts.clear()
  inputs.clear() 

  Calendar.main()
  output = capsys.readouterr().out
  assert "31" in output

def test_sample2(monkeypatch, capsys):
  """Using Sample Run 2 values, this test case checks for 193 in your program's output."""
  monkeypatch.setattr('builtins.input', mock_sample2_input)
  prompts.clear()
  inputs.clear() 

  Calendar.main()
  output = capsys.readouterr().out
  assert "193" in output