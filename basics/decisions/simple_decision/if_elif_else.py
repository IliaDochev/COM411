decision = str(input("Towards which direction should I paint (up, down, left or right)?\n")) #Asking the user for a direction for Beep to paint in and storing in in the variable "decision"

if (decision == "up"): #Performing the first check to see if the user has chosen the upward direction. If it's true, we run the below print statement. If not, we continue with the next check.
  print("I'm painting upwards.")

elif (decision == "down"): #Second check is to see if the user has chosen the downwards direction. If it's true we run the below print statement. If not, we continue with the next check.
  print ("I'm painting downwards")

elif (decision == "left"): #Third check is to see if the user has chosen the left direction. If it's true we run the below print statement. If not, we continue with the next check.
  print("I'm painting in the left direction")

elif (decision == "right"): #Forth check is to see if the user has chosen the right direction. If it's true we run the below print statement. If not, we continue to the default statement.
  print("I'm painting in the right direction.")

else: #If all other checks come back as false we run this default statement.
  print("Which way is that?")