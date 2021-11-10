# message = '''bobby's world was a good
# cartoon in the 1990s'''

greeting = 'Hello'
name = 'Michael'

print(dir(name))
print(help(str))

# new_message = message.replace('world', 'universe')

# message = greeting + ' ' + name + ', welcome!'

message = '{}, {}. welcome!'. format(greeting, name.upper())

print(message)

message = f"{greeting},{name.upper()}. welcome!"
print(message)

