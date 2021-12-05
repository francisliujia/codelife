import datetime
import calendar

balance = 5000

interest_rate = 13 * .01
monthly_payment = 500

today = datetime.date.today()
# print(today)

# return the first day of the month(in this example; 6 means satursay) in that week and the days of the month
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
# print(days_in_current_month)

days_till_end_month = days_in_current_month - today.day
# print(days_till_end_month)

start_date = today + datetime.timedelta(days = days_till_end_month +1)
print(start_date)

end_date = start_date±

while balance > 0:
	interest_charge = (interest_rate / 12) * balance
	balance += interest_charge
	balance -= monthly_payment

	balance = round(balance, 2)	
	if balance < 0:
		balance = 0

	# balance = 0 if balance< 0 else round(balance, 2)
	print(end_date, balance)

	days_in_current_month = calendar.monthrange(today.year, today.month)[1]
	start_date = today + datetime.timedelta(days = days_till_end_month)



