import random

num = random.randint(1, 10000)
guess = 0

while guess != num:
    guess = int(input("Enter your guess: "))
    if guess != num:
        if guess > num:
            print("Lower!")
        elif guess < num:
            print("Higher!")

print(f"You got it right! {num} was the right answer.")

# HOW did I make this first try no bugs i am really pro wtf
