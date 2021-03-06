print(
    "What type of cover does the book have? (hard or soft)"
)  #Requesting from the user to input the type of cover the book has and storing it in the string variable "cover"
cover = input()

if (
        cover == "soft"
):  #Performing the first check to see if the user has entered the word "soft" in the console and it he has, the program runs the below code.

    print(
        "Is the book perfect-bound?"
    )  #Asking the user if the book is perfect-bound, and storing it in the string variable "bounding" below.
    bounding = input()

    if (bounding == "yes"):  #Check if the book is perfect-bound
        print("Soft cover, perfect bound books are very popular!"
              )  #If the above is true, the program prints this message.

    else:  #If the above is false the program prints this default message.
        print("Soft covers with coils or stitches are great for short books")

elif (
        cover == "hard"
):  #Checking if the users choice of book cover is "hard" and if it is the below piece of code is ran.
    print("Books with hard covers can be more expensive!")
