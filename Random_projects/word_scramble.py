import random

print("Welcome to word scramble game")
def rules():
    print("Rules of the game:")
    print("1. You will be given a scrambled word.")
    print("2. You need to guess the correct word.")
    print("3. You have 3 attempts to guess the word.")
    print("4. If you guess correctly, you win!")
    print("5. If you run out of attempts, you lose.")

def word_generator():
    words = [
        "python", "programming", "computer", "science", "algorithm",
        "database", "keyboard", "software", "hardware", "network",
        "variable", "function", "terminal", "compiler", "internet",
        "security", "developer", "framework", "debugging", "interface",
        "elephant", "mountain", "universe", "treasure", "adventure",
        "calendar", "notebook", "triangle", "library", "journey",
    ]
    return random.choice(words)

def scrambler(word):
    if len(word) <= 1:
        return word

    chars = list(word)
    while "".join(chars) == word:
        random.shuffle(chars)
    return "".join(chars)
def menu():
    print("Please select an option from the following: ")
    print("1. Type play to start the game")
    print("2. Type rules to print the rules of the game")
    print("3. Type score to check the number of successful attempts")
    print("4. Type fail to check the number of failed attempts")
    print("5. Type exit to exit the game")

def user_choice():
    print("Please enter your choice: ")
    return input().strip().lower()
def word_checker(guess, word1):
    guess_return = list()
    word = list(word1)
    for i in range(len(word)):
        if guess [i]==word[i]:
            guess_return.append(guess[i])
        else:
            guess_return.append("_")

    print("Current guess status: " + ''.join(guess_return))
    return guess == word1


def main():
    successful_attempts = 0
    failed_attempts = 0
    menu()
    while True:
        user_input = user_choice()
        if user_input == "rules":
            rules()
        elif user_input == "play":
            result = play_game()
            if result:
                successful_attempts += 1
            else:
                failed_attempts += 1
        elif user_input == "score":
            print(f"Number of successful attempts: {successful_attempts}")
        elif user_input == "fail":
            print(f"Number of failed attempts: {failed_attempts}")
        elif user_input == "exit":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue




def play_game():
    word = word_generator()
    scrambled_word = scrambler(word)
    attempts = 3

    print(f"Scrambled word: {scrambled_word}")

    while attempts > 0:
        guess = (input("Your guess: ").strip()).lower()
        if len(guess) == len(word):
            flag = word_checker(guess, word)
            if flag:
                print("Congratulations! You guessed the correct word.")
                return True
            else:
                attempts -= 1
                print(f"Incorrect guess. You have {attempts} attempts left.")
        else:
            print(f"Your guess must be {len(word)} characters long. Please try again.")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct word was '{word}'.")
        return False
if __name__ == "__main__":
    main()
