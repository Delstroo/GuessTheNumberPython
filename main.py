import random

def guess_the_number_game():
    print("Welcome to 'Guess the Number'!")
    
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    if upper_bound <= lower_bound:
        print("The upper bound must be greater than the lower bound. Try again.")
        return

    target_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    
    while True:
        guess = input(f"Guess a number between {lower_bound} and {upper_bound}: ")
        
        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        # check the guess
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number_game()
