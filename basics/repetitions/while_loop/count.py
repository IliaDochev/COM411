#Requesting the number of live cables from the user and storing in in the integer "lcables"
lcables = int(input("How many live cables should I avoid?\n"))

#Declaring a counter and setting in to 0
count = 0

#Initializing the loop with condition that while "lcables" is bigger than the counter, the loop should keep running.
while lcables > count:
    #Printing the first statement to the user and ending in with the "end" parameter in order to keep the two print statements on one line.
    print("Avoiding...", end="")

    #Incrementing the "count" counter by 1
    count = count + 1
    #Printing the second print statement to the user.
    print("Done!",count, "live cables avoided!")

#After the loop has ended, the below print statement is printed to the console with two new line characters in front of it.
print("\n\nAll live cables have been avoided.")
