"""
This file is for hangman game
Ceated by: Arman Hovhannisyan
Date 29 april 2024
"""
def game(word, secret):
    """
    Function: game
    Params: word: The word  to guess, secret: coded type of the word 
    Brief: prints the final staate of the word after the game
    """
    count = -1
    while "-" in secret and count < 6:
        print(secret)
        letter = input("Enter a letter: ").lower()
        
        if letter.isalpha() and len(letter) == 1:
            if letter in word:
                for i in range(len(word)):
                    if letter == word[i]:
                        secret = secret[:i] + letter + secret[i+1:]
            else:
                print(f"Incorrect. Try again")
                count += 1
                if count < 6:
                    hangman(count)
        else:
            print("Invalid input!")
    if count == 6:
        hangman(count)
        print("Game over. Word was:", word)
    else:
        print("You win:", word) 


def hangman(count):
    """
    Function: hangman
    Params: count: The count of wrong answers
    Brief: Showing pictures of hangman
    """
    pictures = [
        """
        ------
        |    |
        |
        |
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |    |
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        -
        """
    ]
    
    print(pictures[count])


def main():
    """
    qunction: main
    Brief: Entery point
    """
    word = "something"
    secret = "-" * len(word)
    game(word, secret)
    

if __name__ == "__main__":
    main()
