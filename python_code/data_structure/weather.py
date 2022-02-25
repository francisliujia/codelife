

weather_dict = {}
weather_list = []
with open('nyc_weather.csv') as f:
	lines = f.readlines()
	print('lines:', lines)
	for line in lines[1:]:

		date, temp = line.split(',')
		# temp.replace('\n', '')
		weather_list.append(int(temp))
		print(date, temp)
		weather_dict[date] = temp
print(weather_dict)
print(weather_list)
	# for line in lines:
	# 	weather_dict[line[0]] = line[1]
	# print(weather_dict)

first_week_avg = round(sum(weather_list[0:7])/ 7, 2)
print('==> First week average temp for Jan:',first_week_avg, 'degree.')
print('==> The highest temp is:',max(weather_list))
print('the temp on Jan 9 is:', weather_dict['Jan 9'])
print('the temp on Jan 4 is:', weather_dict['Jan 4'])




