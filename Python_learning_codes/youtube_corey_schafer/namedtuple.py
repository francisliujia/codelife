from collections import namedtuple
import sys

print(sys.executable)
print(sys.version, '\n')

print (sys.version)

# color = (55, 155, 255)
color = {'red': 55, 'green': 155, 'blue': 255}
print (color['red'])


color = namedtuple('color', ['red', 'green', 'blue'])
color = color(55,155,255)


print (color.red)