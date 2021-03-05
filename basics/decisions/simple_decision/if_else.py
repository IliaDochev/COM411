# The below line requests from the user to enter an activity and stores it
print("Please enter the activity you wish Beep to perform:")
activity = input() 


if (activity == "calculate"): #This line checks to see if the user choice is to calculate and if it matches, it runs the below code
    print("\n\nPerforming calculations...")
else: #If the above check comes out as false it prints the below line of code
    print("\nPerforming activity...")

#Informing the user that whichever activity he chose is complete
print("\n\n\nActivity completed!")
