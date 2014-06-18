#prime numbers

user_input = int(input("How many numbers would you like to check?: "))

for number in range(1, user_input): #Select numbers from 1 to 20
    for factor in range(2, number): #Checks through from 2 to our selected number -1
        if number%factor == 0:
            break #This triggers our code to go back to the first for loop, skipping an incorrect prime number print.

    else: #This acts differently than and If Else
        print(number, "is a prime number")
