# lambda

# f = lambda a,b : a+b
# result = f(4,5)

# print(result)

# ///////////////////////
# print shapes
# for i in range(4):
# 	for j in range(4-i):
# 		print('#', end='')

# 	print()



# /////////////////////////
# find the prime number
# num = 17

# for i in range(2,17):
# 	if num % i == 0:
# 		print('Not prime')

# 		break

# else:
# # 	print('prime')



# ///////////////////////////////
# array

# from array import *
# arr = array('i', [])

# n = int(input("enter the length of the array: "))

# for i in range(n):
# 	x = int(input('enter the next value'))
# 	arr.append(x)

# print(arr)

# val = int(input("enter the value for search"))

# k = 0
# for e in arr:
# 	if e == val:
# 		print(k)
# 		break
# 	k+=1

# print(arr.index(val))


# /////////////////////////////
# numpy

# from numpy import *
# arr = array([1,2,3,4.0,5], int)

# print(arr.dtype)

# arr = linspace(0,15)
# arr = arange(1,15,2)
# arr = logspace(1,40,5)
# arr = zeros(5)
# arr = ones(5, int)

# print(arr)


# /////////////////////////////
# from numpy import *

# arr = array(1,2,3,4,5)

# arr1 = array([1,2,3,4,5])
# arr2 = array([4,5,3,4,5])
# arr3 = arr1 + arr2

# arr4 = arr1
# arr5 = arr1.view()
# arr6 = arr1.copy()
# arr1[1] = 66

# print(concatenate([arr1, arr2]))
# print(arr4)
# print(id(arr4))
# print(id(arr1))
# print(id(arr5))
# print(arr6)


# //////////////////
# from numpy import *

# arr1 = array([
# 				# [1,2,4,2,7,5],
# 				# [3,4,5,4,5,6]
# [1,2,3,4],
# [3,4,5,6]

# 	])

# # arr2 = arr1.flatten()
# # print(arr2)

# arr3 = arr2.reshape(2,2,2)
# print(arr3)

# m1 = matrix('1,2,3; 4, 5, 6; 5, 6, 7')
# m2 = matrix('1,2,6; 4, 2, 6; 4, 2, 7')


# print(diagonal(m1))
# print(m1.min())
# print(m1.max())
# m3 = m1 * m2
# print(m3)

# /////////////////////////
# *kwargs
# def person(name, **data):

# 	print(name)

# 	for i, j in data.items():
# 		print(i, j)

# person('navin', age=23, city='NewYork', mob=12324)

# def person(name, **data):
# 	print(name)
# 	# print(data)
# 	for i,j in data.items():
# 		print(i, j)


# person('jiaxin')
# person('francis',job = 'developer', age = 23)



# ///////////////////////////////////
# global variables

# a = 10
# print(id(a))

# def something():

# 	a= 15 

# 	x = globals()['a']
# 	print(id(x))
# 	print('in fun', a)

# 	globals()['a'] = 15

# something()
# print(a)


# ////////////////////////////////////////
# odds and even numbers count

# def count(lst):

# 	even = 0
# 	odd = 0

# 	for i in lst:
# 		if i%2 == 0:
# 			even+=1
# 		else:
# 			odd+=1
# 	return even, odd


# lst = [23,22,25,56,12,13,45,66]

# even, odd = count(lst)

# result = f"even:{even}, odd {odd}"

# print(result)


# ////////////////////////////////////////
# fibonacci sequence

# def fib(n):
# 	a = 0
# 	b = 1

# 	if n == 1:
# 		print(a)
# 	else:
# 		print(a)
# 		print(b)
# 	print(a)
# 	print(b)

# 	for i in range(2,n):
# 		c = a + b
# 		a = b
# 		b = c 
# 		print(c)


# fib(5)



# //////////////////////////////////
# factorial 

# factorial of 5: 5! = 1*2*3*4*5

# def fact(n):

# 	f = 1

# 	for i in range(1, n+1):
# 		f*=i

# 	return f


# x = 10
# result = fact(x)
# print(result)

# ////////////////////////////////////
# iterator


# iterator
# i = 0
# def greet():
# 	global i
# 	i+=1

# 	print("Hello", i)
# 	greet()

# greet()
# ////////////////////////////////////////

# iterator
# def fact(n):
# 	if(n==0):
# 		return 1

# 	return n * fact(n-1)


# result = fact(5)
# print(result)


# /////////////////////////////////////

# def is_even(n):
# 	return  n%2 == 0

# from functools import reduce
# nums = [1,4,34,2,45,6,8,9]
# # evens = list(filter(is_even, nums))
# evens = list(filter(lambda n:n%2==0, nums))
# doubles = list(map(lambda n : n*2, evens))

# sum = reduce(lambda a,b : a+b,doubles)

# print(evens)
# print(doubles)
# print(sum)



# ////////////////////////////////////
# decorators

# def div(a, b):
# 	print(a/b)

# def smart_div(func):

# 	def inner(a,b):
# 		if a < b:
# 			a,b = b,a

# 		return  func(a,b)

# 	return inner

# div = smart_div(div)
# div(2,4)

# @smart_div
# def div(a, b):
# 	print(a/b)
# div(2,4)

# //////////////////////////////////////
# def square(x):
# 	return x*x

# def my_map(func, arg_list):
# 	result = []
# 	for i in arg_list:
# 		result.append(func(i))
# 	return result

# squares = my_map(square, [1,2,3,4])

# print(squares)

# ////////////////////////
# def outer_func():
# 	message = 'hi'

# 	def inner_func():
# 		print(message)

# 	return inner_func

# my_func = outer_func()

# print(my_func.__name__)

# my_func()
# my_func()
# my_func()
# ///////////////////////////////////


# def decorator_function(original_function):
# 	def wrapper_function():
# 		return original_function()

# 	return wrapper_function

# def display():
# 	print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()


# @decorator_function
# def display():
# 	print('display function ran')

# decorated_display()

# print(__name__)



# /////////////////////////////////
# class

# class Student:
# 	def __init__(self, s1, s2):
# 		self.s1 = s1
# 		self.s2 = s2


# 	def sum(self, a, b, c):

# 		s = a + b + c
# 		return s

# m1 = Student(12,21)
# print(m1.sum(12,21,23))

# /////////////////////////

# class Student:
# 	def __init__(self, m1, m2):
# 		self.m1 = m1
# 		self.m2 = m2

# 	def sum(self, a=None, b=None, c=None):
# 		s = 0
# 		if a!=None and b!=None and c!=None:
# 			s = a+b+c
# 		elif a!=None and b!=None:
# 			s = a+b
# 		else:
# 			s = a
# 		return s 

# s1 = Student(45,22)

# print(s1.sum(23,32,23))

# ///////////////////////
# class A:

# 	def show(self):
# 		print("in A show")


# class B(A):
	
# 	def show(self):
# 		print("in B show")

# a1 = B()
# a1.show()
# ////////////////////////////////


# from abc import ABC, abstractmethod

# class Computer(ABC):

# 	@abstractmethod
# 	def process(self):
# 		pass

# class Laptop(Computer):
# 	def process(self):
# 		print("it's running")

# com = Computer()
# com1 = Laptop()
# com.process()

# import sys
# print(sys.version)
# //////////////////////////////



# ////////////////////////
# generator

# nums = [1,2,4,5,6]

# it = iter(nums)
# print(it.__next__())

# print(next(it))
# for i in nums:
# 	print(i)


# ////////////////
# class TopTen:
# 	def __init__(self):
# 		self.num = 1

# 	def __iter__(self):
# 		return self

# 	def __next__(self):

# 		if self.num <= 10:
# 			val = self.num
# 			self.num += 1

# 			return val
# 		else:
# 			raise StopIteration

# values = TopTen()

# print(next(values))

# for i in values:
# 	print(i)

# ////////////////////////////////

# Exception

# a = 5
# b = 0

# try:
# 	print(a/b)
# except Exception as e:
# 	print("You cannot do it.", e)


# threading
# ///////////////////
# from threading import *
# from time import sleep

# class Hello(Thread):
# 	def run(self):
# 		for i in range(5):
# 			print("Hello")



# class Hi(Thread):
# 	def run(self):
# 		for i in range(5):
# 			print("Hi") 

# t1 = Hello()
# t2 = Hi()

# t1.run()
# t2.run()
# /////////////////////////


# /////////////////////////////
# liner search
# pos = -1

# def search(list, n):
# 	i = 0
# 	while i<len(list):
# 		if list[i] == n:
# 			globals() ['pos'] = i
# 			return True
# 		i+=1
# 	return False


# list = [5,3,6,34,7,8,9]
# n = 9

# if search(list, n):
# 	print("Found at", pos)
# else:
# 	print("not Found")


# ///////////////////
# binary searh
# pos = -1

# def search(list, n):
# 	l = 0
# 	u = len(list)-1

# 	while l <= u:
# 		mid = (l+u) // 2

# 		if list[mid] == n:
# 			globals()['pos'] = mid
# 			return True
# 		else:
# 			if list[mid] < n:
# 				l = mid+1
# 			else:
# 				u = mid-1
# 	return False

# list = [1,2,4,5,3,5,3,24,54]
# n = 24

# if search(list, n):
# 	print("fount at", pos+1)
# else:
# 	print("not found")

# //////////////////////////////////
# bubble sort

# def sort(nums):
# 	for i in range(len(nums)-1,0,-1):
# 		for j in range(i):
# 			if nums[j]>nums[j+1]:
# 				temp = nums[j]
# 				nums[j] = nums[j+1]
# 				nums[j+1] = temp


# nums = [5,3,6,7,9,8]
# sort(nums)

# print(nums)


# ///////////////////////////
# selection sort
# def sort(nums):
	
# 	for i in range(5):
# 		minpos = i
# 		for j in range(i,6):
# 			if nums[j] < nums[minpos]:
# 				minpos = j

# 				temp = nums[i]
# 				nums[i] = nums[minpos]
# 				nums[minpos] = temp

# 				print(nums)

# nums = [9,6,5,3,53,56]
# sort(nums)
# print(nums)


# ////////////////////////////
# mysql and python


# import mysql.connector

# mydb = mysql.connector.connect(host='localhost', user='root', passwd='572433_Fl', database='learning')

# mycursor = mydb.cursor()

# mycursor.execute("select * from student")

# result = mycursor.fetchone()


# for i in result:
# 	print(i)


# names = ['frank', 'lee']
# marks = ['23', '34']

# zipped = dict(zip(names, marks))
# print(zipped)
 

# /////////////////////////
# *args and **kwargs

# def foo(required, *args, **kwargs):
# 	print(required)
# 	if args:
# 		print(args)
# 	if kwargs:
# 		print(kwargs)


# foo('Hello')
# foo('hello', 1,2,4)
# foo('hello', 1,2,3, key1='value', keys=333)


# ///////////////////////////
# import matplotlib.pyplot as plt
# def graph_operation(x, y):
# 	print('function that graph {} and {}'.format(str(x), str(y)))
# 	plt.plot(x,y)
# 	plt.show()

# x1 = [1,2,3]
# y1 = [2,3,5]

# graph_me = [x1, y1]
# graph_operation(*graph_me)













