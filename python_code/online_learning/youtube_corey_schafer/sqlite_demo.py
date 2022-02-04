import sqlite3
from employee import *

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
# 	first text,
# 	last text,
# 	pay integer
# 	)""")


def insert(emp):
	with conn:
		c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})
	


def get_emps_by_name(lastname):
	c.execute("SELECT * FROM employees WHERE last=:last", {"last":'lastname'})
	return c.fetchall()




def update_pay(emp, pay):
	with conn:
		c.execute("""UPDATE employees SET pay=:pay
			WHERE first=:first AND last=:last""",
			{'first':emp.first, 'last':emp.last, 'pay':emp.pay})


def remove_emp(emp):
	with conn:
		c.execute("DELETE from employees WHERE first AND last=:last",
			{'first':emp.first, 'last':emp.last, 'pay':emp.pay})



emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)

# ////////////1/////////
# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()

# # ///////////////2//////////
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

# conn.commit()


# # ///////////////3////////////
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})

# conn.commit()


# c.execute("INSERT INTO employees VALUES ('Marry', 'Schafer', 50000)")


# c.execute("SELECT * FROM employees WHERE last='Schafer'")
c.execute("SELECT * FROM employees WHERE last=?", ("Schafer",))
print(c.fetchall())


c.execute("SELECT * FROM employees WHERE last=:last", {"last":'Doe'})
print(c.fetchall())

# c.fetchmany(5)
# c.fetchall()

conn.commit()

conn.close()