from datetime import datetime, timedelta
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_previous_byday(dayname, start_date=None):
	if start_date is None:
		start_date = datetime.today()
	day_num = start_date.weekday()
	day_num_target = weekdays.index(dayname)
	days_age = (7+ day_num - day_num_target) % 7

	if days_ago == 0:
		days_ago = 7
	target_date = start_date - timedelta(days=days_ago)
	return target_date


datetime.today()
