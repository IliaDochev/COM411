# Asking the user for location within the house and storing the choice in variable "location"
location = input("Where should I look?\n") 

#First check if the user has chosen "in the bedroom".
if(location == "in the bedroom"): #If this check is true, the below code is being ran.
  bedloc = input("\nWhere in the bedroom should I look?\n") #Asking the user where in the bathroom to look.
  if(bedloc =="under the bed"):  #Asking the user where in the bedroom to look.
    print("Found some shoes but no battery.") #Printing the result if the user has chosen "under the bed"
  else: #If the user has chosen some other spot in the bedroom, the below statement is printed
    print("Found some mess but no battery.") 

elif(location == "in the bathroom"): #Second check is to see if the user has chosen to look "in the bathroom"
  bathloc = input("\nWhere in the bathroom should I look?\n") #Asking the user where in the bathroom to look
  if(bathloc == "in the bathtub"): #If the user has chosen to look "in the bathtub", the below statement is printed.
    print("Found a rubber duck but no battery")
  else: #If the user has chosen any other place in the bathroom, the below statement is printed.
    print("Found a wet surface but no battery.")
    
elif(location == "in the lab"): #Check if the user has chosen to look "in the lab", and if he has, the below piece of code is ran.
  labloc = input("\nWhere in the lab should I look?\n") #Asking the user for a location inside the lab
  if(labloc == "on the table"): #Check if the user has typed "on the table", and if he has, the below statement is printed.
    print("Yes! I found my battery!")
  else: #Default statement if the user has chosen any other location inside the lab
    print("Found some tools but no battery.")

else: #Default statement if the user has chosen to look in any other place in the house insted of the above stated ones.
  print("I do no know where that is but I will keep looking.")


  