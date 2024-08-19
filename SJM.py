# # a_b1 = int(input("enter the 1st value"))
# # b_a1 = int(input("enter the 2nd value"))

# # print(a_b1//b_a1)



# # age = "crystallize"

# # if "x" not in age :
# #     print("flase")

# # else:
# #     print("else")


# # elif age <=0:
# #      print("invalid")
# # else:
# #      print("not permitted")


# # a = "Crystallize Technologies"

# # b = 'Crystalize Technologies'
# # c = """ Crystallize 

# # Technologies"""



# a = "string of 6 character"

# # a[3] = "k"
# # print(a)
# # print(a[5:21:1])


# # print(a[::-1])


# lst = [1,2.3,True,"string"]


# lst.remove("string")
# lst.pop()
# lst.pop()

# # print(type(lst))
# # print(type(lst[2]))

# # lst.append([11,11.2,False])
# # lst.insert(2,"cry")
# lst.extend([11,11.2,False])
# # lst.reverse()
# # lst.clear()



# # print(lst)


# a = (1,2,232.0,"sting",[11,22,33],(1,2,.3))
# # print(a)
# # a = list(tpl)


# # a[2] = "String"
# a = "string"
# b = "tpl"

# # print(a+b)
# # b = (11,22,33)
# # print(a[0:2])


# a = {1,22,"string",True}

# b = {2,5,8,7,9,1,22}

# z=b.difference(a)
# # a.add("stri")
# # print(z)


# dct ={ 1:{1:"name",
#        2:"Age",
#        3:"State"},

#        2:{1:"name",
#        2:"Age",
#        3:"State"}}
# # st = {1:1,2:2,3:3} 
# print(dct)

# # print(type(st))
# dct["name"] = "string"
# # print(dct)

# # for i in range(0,11,2):
# #     print(i)

# a = "crystallize"

# # for i in a:
# #     print(i)

# # i = 0
# # while i<=11:
# #     print(i)
# #     i+=1
    











# #Factorial 
# # num =int(input())
# # factorial = 1

# # for i in range(1,num + 1):
# #     factorial = factorial*i
# # print("The factorial of",num,"is",factorial)










# # # # Fibonacci Series in Python Using For Loop
# # a, b = 0, 1
# # num = 18
# # print(a, b, end=' ')
# # for i in range(num):
# #     c = a + b
# #     print(c, end=' ')
# #     a = b
# #     b = c













# # # Reverse a number
# # num = 123456789
# # reversed_num = 0

# # while num != 0:
# #     digit = num % 10
# #     reversed_num = reversed_num * 10 + digit
# #     num //= 10

# # print("Reversed Number: " + str(reversed_num))

# # import  array

# # a = array.array('i',[1,2,3,4,5])

# # print(a[2])



# # def f_name(*a):
# #     print("done")

# # f_name(a="name",b="age")



# #lambda anonymous function

# # def f_name(a):
# #     return a+10

# # print(f_name(5))

# # x = lambda a: a+10
# # print(x(5))

# # a = 200 # global variable

# # def f_name():

# #     # a = 10 # local variable of this function

# #     print(a*a)


# # f_name()

# # non local variable

# # def outer ():
# #     x =  "local"

# #     def inner():
# #         nonlocal x
# #         x = "non local"
# #         print("inner : ", x)

# #     inner()
# #     print("outer: ", x)

# # outer()


# # Object oriented programming

# # class Dog:   #creation of a class

# #     #constructor 
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age

# #     def f_name (self):
# #         print("the name of the dog is: ", self.name)

# #     def f_age(self):
# #         print("the age is : ",self.age)

# # obj = Dog("Husky",12) #creation of an object


# # obj.f_name()
# # obj.f_age()

# # print("the name of the dog is: ",obj.name, "It`s age is: ",obj.age) # usage of the variable inside a class


# # class Parent:
# #     def func1(self):
# #         print("This function is in parent class.")

# # class Child(Parent):
# #     def func2(self):
# #         print("This function is in child class.") 

# # object = Child()
# # object.func1()
# # object.func2()


# # class Mother:
# #     mothername = ""

# #     def mother(self):
# #         print(self.mothername)
  
# # class Father:
# #     fathername = ""
 
# #     def father(self):
# #         print(self.fathername)
 
# # class Son(Mother, Father):
# #     def parents(self):
# #         print("Father :", self.fathername)
# #         print("Mother :", self.mothername)
 
# # s1 = Son()
# # s1.fathername = "RAM"
# # s1.mothername = "SITA"
# # s1.parents()


# # class School:
# #     def func1(self):
# #         print("This function is in school.")
 
# # class Student1(School):
# #     def func2(self):
# #         print("This function is in student 1. ")
 
# # class Student2(School):
# #     def func3(self):
# #         print("This function is in student 2.")
 
# # class Student3(Student1, School,Student2):
# #     def func4(self):
# #         print("This function is in student 3.")
 
# # object = Student3()
# # object.func1()
# # object.func2()
# # object.func3()



# # class employee:
# #       def __init__(self, name, age):
# #             self.name=name 
# #             self.age=age

# # class employee:
# #       def __init__(self, name, age):
# #             self.__name=name # private attribute   #name mangling
# #             self.__age=age # protected attribute

# # obj = employee("abc",12)
# # print(obj.__name)

# #Polymorphism

# # multiple forms



# # "+"


# # print(2+3)

# # print("2"+"3")

# # a = "string"

# # b = ["apple",12,23.5,True,"apples"]


# # print(len(a))

# # print(len(b))


# #abstraction

# # from abc import ABC, abstractmethod

# # class demo(ABC):
# #    @abstractmethod
# #    def method1(self):
# #       print ("abstract method")
# #       return
# #    def method2(self):
# #       print ("concrete method")


# # obj = demo()

# # obj.method1()
# # obj.method2()




# #Errors

# # # zero division error
# # m = 1000

# # a = m/0

# # print(a)


# #type error
# # x = 5

# # y = "sjm"

# # print(x+y)



# # def f_name(a):
# #     if a<4:
# #         b= a/(a-3)
# #     print("value of b = ",b)

# # try:
# #     f_name(3)
# #     f_name(5)

# # except ZeroDivisionError:
# #     print("Zero division error has occured")

# # except NameError:
# #     print("Name error has occured")


# # finally :
# #     print("errors have been handled")


# #file handling


# # file = open('hello.txt','r')
# # print(file.read(5))


# # with open("hello.txt") as file:
# #     data = file.read()

# # print(data)

# # for each in file:
# #     print(each)


# # file  = open("hello.txt","w")
# # file.write("this is in write mode ")

# # file.write("we are from sjm")

# # file.close()

# # file = open("hello.txt","a")
# # file.write("this is an append mode")

# # file.close()



# # class Dog:

# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age


# #     def fun(self):
# #         print("the name is : ",self.name, " age is : ",self.age)


# # obj = Dog("Husky",12)

# # obj.fun()

# import datetime

# date = datetime.datetime.now()

# print(date)


# Python Numpy

# pypi numpy


# import numpy

# # a = numpy.array([1,2,3,4,5])


# print(numpy.__version__)


# 0-d arrays




# print(a.dtype)

# i,b,f,S,O



# f = np.array([3,2,0,1])

# n = np.sort(f)
# print(n)


# new = np.array_split(f,4)

# print(new)


# g = np.array([7,8,9,10,11,12])


# h = np.stack((f,g),axis=1)

# print(h)


# new = f.reshape(3,4)
# print(new)

# for i in f:
#     print(i)


# import numpy as np

# from numpy import *

#0,1

# print(a)

# while True:
#     a = random.rand()
#     print(a)


#pandas 

# pip install pandas 


# import pandas as pd





# a = ["apple","orange","mango","banana"]


#series 

# b = pd.Series(a)


# print(b)


# b = pd.Series(a, index=["a","b","c","d"])

# # labels

# print(b)



# var = {1:"monday",2:"Tuesday",3:"Wed",4:"Thu"}

# print(pd.Series(var))

# data = {

#     "a":[100,200,300],
#     "b":[50,60,70]
# }

# df = pd.DataFrame(data) 


# print(df)



# df = pd.DataFrame(data, index=["num1","num2","num3"])

# print(df)
# print(df.loc["num1"])

import pandas as pd

# a = {
#     1:"a",2:"b",3:"c"
# }


# print(pd.Series(a))
# a = [1,2,3,4,5]

# b =pd.Series(a, index=["a","b","c","d","e"])
# print(b)



#labels



# print(b["b"])




#dataframes


# a = {
#     1:["a","b","c"],
#     2:["d","e","f"]

# }

# b = pd.DataFrame(a,index=[1,2,3])
# print(b.loc[3])

# print()

# csv

# a = pd.read_csv("data.csv")


# # print(a.tail())
# # print(a.head())
# # print(a.info())
# # print(a.to_string())

# # b = a.dropna()

# # print(b.to_string())


# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([3,8,6,7,5,10])
# x = np.array([1,2,3,4,5])
# y = np.array([3,8,7,6,10])

# plt.plot(x,y)

# font1 = {'family':'Times New Roman','color':'blue','size':20}

# plt.title("this is title", fontdict=font1, loc='left')
# plt.xlabel("this is xlabel",fontdict=font1)
# plt.ylabel("this is ylabel", fontdict=font1)


# plt.grid()
# plt.plot(y,marker= '*', ms = 30) #r,g,b, cyan, magenta , y, w, k = black,
# plt.show()



# import pandas as pd

# a = pd.read_json("data.json")


# print(a.tail(50))

# python -m pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6])
y = np.array([10,20,30,40,50,60])


plt.title("this is a title")
plt.xlabel("H label")
plt.ylabel("V label")
plt.plot(x,y)

plt.show()

