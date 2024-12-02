
#1
pi=22/7
"""To find the data type of variable we use type keyword"""
print("Type of variable pi is : ",type(pi))

#2
"""We are assinging the value to the variable called for and seeing its nature"""
# for = 4
# In the above problem we will getting a syntax error the reason for this error is: here assing value to the 
# variable called for but for is already present in keyword. we cannot use keywords as variables in python.
"""To do it in a without any errors we can do the following"""
for_value=4
print("Value of for :",for_value)

#3
"""Here we are calculating simple interest by taking all the values
   p-->principal amount
   r-->rate of interest
   t-->time
   si-->simple interest"""
p=100000
r=5
t=1
si=p*r*t/100
print("Simple Interest = ",si)