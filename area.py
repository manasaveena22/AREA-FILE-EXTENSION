from math import pi

r = float(input("input the radius of the circle: "))

area = pi * r**2

print("The Area of the circle with radius " , r ,"is:", area)

fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])
