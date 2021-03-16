#Requesting a user input to the queston "What did I hear?" and storing in variable "hear"

hear = input("What did I hear?\n")

#Requesting a user input to the question "What did I see?" and storing it in variable "see"
see = input("\nWhat did I see?\n")

#Main program logic. The below statement checks if the users input matches the predefined parameters, and if it does, it prints th appropriate message.
if(hear == "grr") and (see == "two red eyes"):
    print("There is a scary creature. I should get out of here!")

#If the above check is false, the program prints the below message to the user
else:
    print("I am a little scared but I will continue.")