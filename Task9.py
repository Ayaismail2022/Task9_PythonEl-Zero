"""
Task 9
"""
#التكليف الاول 
num1= int(input("Enter first number "))
num2= int(input("Enter second number "))
operation = input("choose your operation +, -, *, /, % ").strip()

if operation == "+":
    print(f"{num1} + {num1} = {num1+num2}")
elif operation == "-":
    print(f"{num1} - {num1} = {num1-num2}")
elif operation == "*":
    print(f"{num1} * {num1} = {num1*num2}")
elif operation == "/":
    print(f"{num1} / {num1} = {num1/num2}")
else:
    print(f"{num1} % {num1} = {num1%num2}")

print("-"*20)

# التكليف التاني
age = 17
if age > 16 : print("App is suitable for you ")
if age < 16 : print("App is not suitable for you ")

print("-"*20)


# التكليف التالت
myage = int(input("Enter your age: "))

months = myage * 12
weeks = months * 4
days = myage * 365
hours = days * 24
minutes = hours * 60
sec = minutes * 60 
if myage > 10 and myage < 100 :
    print(f"Your age \n in Months is {months} Months \n in weeks is {weeks} weeks \n in Days is {days} Days \n in Hours is {hours} Hours \n in Minunits is {minutes} Minunits \n in Seconds is {sec} Seconds")
else:
    print("Your age is not available")

print("-"*20)

# التكليف الرابع
countries = ["Egypt","Palestine","Syria","Yemen","KSA","USA","Bahrain","England"]
country = input("Input your Country: ").strip().capitalize()
price = 100
discount = 30

if country in countries:
    print(f"Your country \"{country}\" is Eligible for Discount and the price after discount is ${price - discount}")
else :
    print(f"Your country \"{country}\" not Eligible for Discount and the price is ${price}")
