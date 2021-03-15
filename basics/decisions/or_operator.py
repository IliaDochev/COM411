adv = input("What type of adventure should I have?\n") #Requesting the type of adventure from the user

if (adv == "scary") or (adv == "short"): #If the user has entered either "scary" or "short", the below statement is printed
  print("\nEntering the dark forest!")

elif(adv == "safe") or (adv == "long"): #Check if the user has entered either "safe" or "long", and if he has, the below statement is printed.
  print("\nTaking the safe route!")

else: #Default statement if the user has chosen to have any other type of advanture.
  print("\nNot sure which route to take.")