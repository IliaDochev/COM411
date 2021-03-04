print("What is your name human?")
name=input()

print("How old are you? (In years)")
age = int(input())

print("How tall are you? (In meters)")
height = float(input())

print("How much do you weight (In kilograms)")
weight = float(input())

bmi = weight / (height ** 2)

print(name, "your age is" ,age, "and your bmi is {:.2f}".format(bmi))