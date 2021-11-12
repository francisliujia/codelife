'''
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("\n")
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
''

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + " now.")
alien_0['color'] = 'yelow'
print("The alien is " + alien_0['color'] + "now.")
''
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Origianl position: {alien_0['x_position']} now.")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
''

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
''

favorite_languages = {
    'plamena': 'python',
    'isebella': 'C',
    'khran': 'ruby',
    'emily': 'python',

}
language = favorite_languages['plamena'].title()
print(f"Plamena's favorite language is {language}.")
'''

alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0.get('points', 'No points value assigned.'))

point_value = alien_0.get('points', 'no points value assigned.')
print(point_value)
'''
