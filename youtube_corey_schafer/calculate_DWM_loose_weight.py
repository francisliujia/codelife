import datetime
current_weight = 220
goal_weighgt = 180

avg_labs_week = 2

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weighgt:
	end_date += datetime.timedelta(days=7)
	current_weight -= avg_labs_week

print(f'Reached goal in {(end_date - start_date).days // 7} weeks.')
