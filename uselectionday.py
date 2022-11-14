#This finds the United States election day in a certain year. Congressional, presidential and, gubernatorial elections occur on this day
import datetime as dt

year = int(input("Enter year: "))

def first_tuesday_of_month(year, month):
  d = dt.datetime(year, month, 1)
  wd = d.weekday()
  # monday
  if wd == 0:
    return 2
  # tuesday
  if wd == 1:
    return 1
  # wensday
  if wd == 2:
    return 7
  # thursday
  if wd == 3:
    return 6
  # friday
  if wd == 4:
    return 5
  # saturday
  if wd == 5:
    return 4
  # sunday 6
  if wd == 6:
    return 3

if __name__ == "__main__":
    if first_tuesday_of_month(year, 11) == 1:
        print("November 8")
    else:
        print("November", first_tuesday_of_month(year, 11))
