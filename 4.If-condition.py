#1
#h-->height,w-->weight,
h=float(input("Enter height in meters"))
w=float(input("Enter weight in kilograms"))
BMI=(w/h**2)
if BMI >=30 :
    print("Obesity")
elif 25<= BMI < 30 :
    print("Overweight")
elif 18.5<= BMI <25:
    print("Normal")
else:
    print("Underweight")

#2
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
n=input("Enter a city name:")
if n in Australia :
    print("Australia")
elif n in UAE :
    print("UAE")
elif n in India :
    print("India")
else :
    print("Another country")    

#3
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
n=input("Enter first city name:")
m=input("Enter second city name :")
if n in Australia and m in Australia :
    print("Both cities are in Australia")
elif n in UAE and m in UAE :
    print("Both cities are in UAE")
elif n in India and m in India :
    print("Both cities are in India")
else :
    print("They don't belong to the same country")    

