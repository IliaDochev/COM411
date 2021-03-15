print("Program started")

user_input = input("Please enter a letter: ")

if (len(user_input) != 1):
  print("You were supposed to enter a single character only, you clever hunan!")

else:
  print("Thank you, we will now process your input")

  x = ord(user_input)

  print("The ASCII character for the letter that you entered is: ", x)