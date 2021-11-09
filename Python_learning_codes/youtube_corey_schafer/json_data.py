'''JavaScript Object Notation'''
import json

people_string = '''
{
	"people":[
		{
		"name": "John Smith",
		"phone": "615-555-7164",
		"emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
		"has_liences": false 
		},
		{
		"name": "Jane Doe",
		"phone": "560-555-5153",
		"emails": null,
		"has_liences": true 
		}
	]
}
'''

data = json.loads(people_string)
# print(type(data))
# print(data)
# print(type(data['people']))

for person in data['people']:
	# print(person)
	print(person['name'])
	del person['phone']

# new_string = json.dumps(data)
# new_string = json.dumps(data, indent=2)
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)



