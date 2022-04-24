def is_leap(year):
  '''Take a year and check if it is a leap year.'''
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  '''Take a year and a month and tell you how many days are there in the month'''
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year):
      days = month_days_leap[month-1]
  else:
      days = month_days[month-1]
  return days
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
