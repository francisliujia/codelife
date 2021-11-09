import datetime 
import pytz

# don't write unnecessary 0 like 07
# d = datetime.date(2016, 7, 24)

# tday = datetime.date.today()
# print(tday)
# print(tday.year)
# print(tday.month)
# print(tday.day)

#  get the day of the week

#  for weekday(): monday is 0 and sunday is 6
#  for isoweekday(): monday is 1 and sunday is 7 
# print(tday.weekday())
# print(tday.isoweekday())


# tdelta = datetime.timedelta(days=7)

# # what date is in one week
# print(tday + tdelta)

# # what date is one week before
# print(tday - tdelta)


# dete2 = date1 + timedelta
# timedelta = tate1 + date2
# bday = datetime.date(2022, 1, 27)
# till_bday = bday - tday
# print(till_bday)
# print(till_bday.total_seconds())


# t = datetime.time(9, 30, 45, 100000)
# print(t.hour)

# gives info only about day
# datetime.day

# gives info only about time
# datetime.time

# gives info about everything
# datetime.datetime

# dt = datetime.datetime(2021,7,25, 12, 30, 45, 100000)
# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)


# # a week into the feature
# # tdelta = datetime.timedelta(days=7)
# tdelta = datetime.timedelta(hours=7)

# print(dt + tdelta)


# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_uncnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_uncnow)


# dt = datetime.datetime(2021,7,27,12,30,45, tzinfo=pytz.UTC)
# print(dt)


# recommonded
# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)


# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

# dt_sh = dt_utcnow.astimezone(pytz.timezone('Asia/Shanghai'))
# print(dt_sh)

# dt_uncnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_uncnow)


# print out all the avaiable time zones
# for tz in pytz.all_timezones:
# 	print(tz)

# dt_sh = datetime.datetime.now()
# sh_tz = pytz.timezone('Asia/Shanghai')

# dt_sh = sh_tz.localize(dt_sh)
# dt_east = dt_sh.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

# print(dt_sh)


dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.isoformat())

print(dt_mtn.strftime('%B %d, %Y'))


dt_str = 'July 25, 2021'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)


# strftime --> datetime to a string
# strptime --> string to datetime





