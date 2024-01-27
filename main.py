import random
from words import word_list


def choose_word():
  word = random.choice(word_list)
  return word.upper()


def play(word):
  current_progress = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  lives_left = 6
  print("Let's play Hangman!")
  print(hangman_stage(lives_left))
  print(current_progress)
  print("\n")
  while not guessed and lives_left > 0:
    guess = input("Please guess a letter or word: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("You already guessed the letter", guess)
      elif guess not in word:
        print(guess, "is not in the word.")
        lives_left -= 1
        guessed_letters.append(guess)
      else:
        print("Good job,", guess, "is in the word!")
        guessed_letters.append(guess)
        word_as_list = list(current_progress)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        current_progress = "".join(word_as_list)
        if "_" not in current_progress:
          guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("You already guessed the word", guess)
      elif guess != word:
        print(guess, "is not the word.")
        lives_left -= 1
        guessed_words.append(guess)
      else:
        guessed = True
        current_progress = word
    else:
      print("Not a valid guess.")
    print(hangman_stage(lives_left))
    print(current_progress)
    print("\n")
  if guessed:
    print("Congrats, you guessed the word! You win!")
  else:
    print("Sorry, you ran out of tries. The word was " + word +
          ". Maybe next time!")


def hangman_stage(tries):
  stages = [  # Final State 
      """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    """,
      # 5th State
      """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    """,
      # 4th State
      """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    """,
      # 3rd State
      """
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    """,
      # 2nd State
      """
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    """,
      # 1st State
      """
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    """,
      # Initial Empty State
      """
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    """
  ]
  return stages[tries]


def play_hangman():
  # ASCII art banner for the game
  print("""
  ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
  ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
  ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
  ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
  ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
    """)
  word = choose_word()
  play(word)
  while input("Play Again? (Y/N) ").upper() == "Y":
    word = choose_word()
    play(word)


if __name__ == "__main__":
  play_hangman()
