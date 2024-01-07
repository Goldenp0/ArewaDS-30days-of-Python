#print 'hello world' gives syntaxerror
print('hello world')

#print(age) NameError age is not defined
age = 25
print(age)

#numbers = [1, 2, 3, 4, 5]
#numbers[5] gives Indexerror list index out of range
numbers = [0, 1, 2, 3, 4]
numbers[4]

#import maths gives ModuleNotFoundError bcos of s added to maths
import math

#import math
#math.PI gives AttributeError bcos of PI
import math
math.pi

#users = {'name':'Asab', 'age':250, 'country':'Finland'}
#users['name']
#'Asab'
#users['county']
#'country' gives keyError

users = {'name':'Asab', 'age':250, 'country':'Finland'}
users['name']
'Asab'
users['country']

#4 + '3' #TypeError
4 + int('3')
7
4 + float('3')
7.0

#from math import power gives ImportError
from math import pow

#int('12a') gives ValueError

#1/0 gives ZeroDivisionError
