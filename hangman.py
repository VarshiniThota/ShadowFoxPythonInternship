import random

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

word_list = [
    ("hello", "A greeting"),
    ("python", "A programming language"),
    ("elephant", "A large animal"),
    ("hangman", "The name of the game")
]

def display_hangman(attempts_left):
    print(HANGMAN_STAGES[len(HANGMAN_STAGES) - attempts_left - 1])

def hangman():
    choice1, hint = random.choice(word_list)
    attempts = len(HANGMAN_STAGES) - 1
    guessed_word = ['_'] * len(choice1)
    guessed_letters = set()
    
    print("Welcome to Hangman!")
    print(f"Hint: {hint}")
    print("Guess the word:")
    print(" ".join(guessed_word))
    
    while attempts > 0:
        print("\n")
        display_hangman(attempts)
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in choice1:
            for i, letter in enumerate(choice1):
                if letter == guess:
                    guessed_word[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")
        
        print(" ".join(guessed_word))
        
        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word:", choice1)
            return
    
    display_hangman(0)
    print("\nYou ran out of attempts! The word was:", choice1)


hangman()