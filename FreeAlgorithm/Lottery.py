import random

print("Enter six numbers separated by space:")
guess = [0] * 6

# Get user input for six numbers
for i in range(6):
    guess[i] = int(input(f"{i+1}. Enter a number: "))

# Generate a list of six random numbers between 1 and 49
lottery_numbers = [random.randint(1, 49) for _ in range(6)]

counter = 0
correct_numbers = [0] * 6

# Check how many guessed numbers match the randomly generated lottery numbers
for i in range(6):
    for t in range(6):
        if guess[i] == lottery_numbers[t]:
            correct_numbers[i] = lottery_numbers[t]
            counter += 1

print()
if counter < 3:
    print("You didn't win.")
else:
    print(f"Congratulations! You guessed {counter} numbers :)")

print()
for i in range(6):
    if correct_numbers[i] != 0:
        print(correct_numbers[i], end=" ")

print()
for i in range(6):
    print(lottery_numbers[i], end=" ")
