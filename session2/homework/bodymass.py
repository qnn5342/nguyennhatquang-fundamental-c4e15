print ("Hello, welcome to Body Mass Index calculation")

mass = int(input("Please enter your mass in kg: "))
height = int(input("Please enter your height in cm: "))/100

BMI = mass / (height **2)

if BMI <16:
    print ("sorry you're severly underweight, eat more please")
elif BMI <= 18.5:
    print ("you're still a bit underweight, eat a bit more")
elif BMI <=25:
    print ("you're normal and sexy")
elif BMI <= 30:
    print ("you're a bit overweight")
else:
    print ("You're too fat to ignore")
