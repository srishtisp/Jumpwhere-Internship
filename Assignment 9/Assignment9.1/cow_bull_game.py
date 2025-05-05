import random

def generate_number():

    number = random.sample(range(10), 4)  
    return ''.join(map(str, number))  

def cows_and_bulls(secret, guess):
    cows = 0
    bulls = 0
    
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    return cows, bulls

def main():
    print("Welcome to the Cows and Bulls Game!")
  
    secret_number = generate_number()
    
    guess_count = 0
    while True:
        guess = input("Enter a 4-digit number: ")
        
     
        if len(guess) != 4 or len(set(guess)) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number with no repeating digits.")
            continue
        
        guess_count += 1
        
        cows, bulls = cows_and_bulls(secret_number, guess)
        
    
        print(f"{cows} cows, {bulls} bulls")
        
     
        if cows == 4:
            print(f"Congratulations! You've guessed the number {secret_number} in {guess_count} guesses.")
            break

if __name__ == "__main__":
    main()
