#1 
def func(a,b):
    return format(a,b)
a=145
b='o'
result=func(a,b)
print(result)
# """The representation used here is octal representation """

#2
"""r-->radius
   pi-->3.14
   ws-->water in square meter
   a-->area of pond
   tw-->total water in pond"""
r=84
pi=3.14
a=(pi*(r**2))
print("Area of pond",a)
ws=1.4
tw=int(a*ws)
print("Total water in pond",tw)


#3
""" d-->distance
    t-->time"""
d=490
t=7
print("Speed = ",int(d/t))