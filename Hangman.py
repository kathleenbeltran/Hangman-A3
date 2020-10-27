import random #Ability to choose random word
from words import words #Importing list of words

def get_valid_word():
    word = random.choice(words)
    return word.upper()

def play(word):
    word_completion = '-' * len(word)
    guessed = False
    used_letters = []
    used_words = []
    user_name = []
    lives = 10
    print("Let's play Hangman!") #Start Screen
    print(show_hangman(lives))
    print(word_completion)
    print("\n")
    user_name = input("What is your name?").upper() #Welcoming User
    print("Welcome", user_name, "! Let's Play Hangman!")
    while not guessed and lives > 0: #Guess the Letter:
        guess = input("Guess a Letter:").upper()
        print("Used Letters:", " , ".join(used_letters)) #Showing used letters
        if len(guess) == 1 and guess.isalpha():
            if guess in used_letters: #Already guessed this letter
                print("You have already guessed the letter", guess, " ")
                
            elif guess not in word: #If user plays word that's not in word
                print(guess, "is not in word. Please Try Again.")
                lives -= 1
                used_letters.append(guess)

            else:
                print("Good Job", guess, "is in the word") #If user plays word that is in word
                used_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha(): 
            if guess in used_words: #If user guess's word again
                print("You already guessed the word", guess)
            elif guess != word: #If user guesses incorectly
                print(guess, "is not in word. Please Try Again.")
                lives -= 1
                used_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Invalid Character, Please try again.") #If user guesses a character that isn't a letter
        print(show_hangman(lives))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratualtions,", user_name, "You've Won! Thank you for Playing!") #User Win
    else:
        print("Sorry, you died. The word was", word, "Try Again next time!") #User Lost


def show_hangman(lives): #Hangman in Stages of Lives
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   ---
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   ---
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   ---
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   ---
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   ---
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   ---
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   ---
                   """, 
                   """ 
                   --------
                   |      
                   |      
                   |
                   |
                   |
                   ---
                   """,  
                   """ 
                   
                   |      
                   |      
                   |
                   |
                   |
                   ---
                   """, 
                   """
                   
                        
                        
                
                   
                   
                   ---
                   """,   
                   """
                   
                        
                        
                
                   
                   
                   
                   """,      
    ] 
    return stages[lives]

def show_usedletters(used_letters):
    print("Guessed Letters:", " , ".join(used_letters)) #Used Letters


def main():
    word = get_valid_word()
    play(word)
    while input("Again? (Y/N) ").upper() == "Y": #Play Again Feature
        word = get_valid_word()
        play(word)


if __name__ == "__main__":
    main()                    
