# No starter code provided — write the full program yourself.
#
# Requirements recap:
secret_number = 7 #(store it in a variable)
# - Prompt must be exactly: "Guess the number: "
# - If guess > secret_number: "Too high!"
# - If guess < secret_number: "Too low!"
# - If guess == secret_number: "Correct! You guessed the number." then stop
# - Must use a while loop, no for loop, no functions

while True:
    guess = int(input("Guess the number: "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct! You guessed the number.")
        break