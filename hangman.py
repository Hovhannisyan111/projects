def game(word, secret):
    count = 7
    while "-" in secret and count > -1:
        print(secret)
        letter = input("Enter a letter: ").lower()
        
        if letter.isalpha() and len(letter) == 1:
            if letter in word:
                for i in range(len(word)):
                    if letter == word[i]:
                        secret = secret[:i] + letter + secret[i+1:]
            else:
                print(f"Incorrect. You got {count} try")
                count -= 1
        else:
            print("Invalid input!")
    return secret

def check(secret, word):
    if "-" not in secret:
        print("You Won.", word)
    else:
        print("You lose. Word was", word)

def main():
    word = "something"
    secret = "-" * len(word)
    secret = game(word, secret)
    check(secret, word)

if __name__ == "__main__":
    main()
