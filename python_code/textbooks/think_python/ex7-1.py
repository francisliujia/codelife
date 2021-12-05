import math

def my_sqrt(a):
    x = a / 2
    while True:
        estimated_root = (x + a/x) / 2
        if estimated_root == x:
            return estimated_root
            break
        x = estimated_root
    
def test_square_root(list_of_a):
    line1a = 'a'
    line1b = 'mysquart(a)'
    line1c = 'math.sqrt(a)'
    line1d = 'diff'
    
    line2a = '-'
    line2b = '----------'
    line2c = '-------------'
    line2d = '----'

    spacing1 = ' '
    spacing2 = ' '* 3
    spacing3 = ''

    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)

    for a in list_of_a:
        col1 = float(a)
        col2 = my_sqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(my_sqrt(a) - math.sqrt(a))

        print(col1, "{:<13f}".format(col2), "{:<13f}".format(col3), col4)
test_square_root(range(1, 10))


