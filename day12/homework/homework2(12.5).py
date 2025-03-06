# 2) ჩამოწერეთ 5-5 მაგალითი შემდეგ ოპერატორებზე:  + , - , * , / , ** , %

1.
num1=10
num2=100
num3=1000

print(num1 + num2 > num3) #False
print(num2 - num3 < num1) #True
print(num3 * num1 >= num2) #True
print(num1 // num2 <=num3) #True
print(num2 ** num3 == num1) #False
print(num3 % num1 != num2) #True


2.
num1=1121
num2=1798

print(num1 > num2) #False
print(num2 < num1) #False
print(num1 >= num2) #False
print(num2 <=num1) #False
print(num2 == num1) #False
print(num1 != num2) #True


3.
num1=9
num2=27
num3=26

print(num3 - num1 > num2) #False
print(num2 + num3 < num1) #False
print(num1 // num2 >= num3) #False
print(num3 * num1 <=num2) #False
print(num2 ** num3 == num1) #False
print(num1 % num2 != num3) #True


4.
num1=1801
num2=1108

print(num1 > num2) #True
print(num1 < num2) #False
print(num1 >= num2) #True
print(num1 <=num2) #False
print(num1 == num2) #False
print(num2 != num1) #True


5.
num1=44
num2=16
num3=8

print(num2 % num1 > num3) #True
print(num3 ** num2 < num1) #False
print(num1 // num3 >= num2) #False
print(num2 * num1 <=num3) #False
print(num3 - num2 == num1) #False
print(num1 + num3 != num2) #True