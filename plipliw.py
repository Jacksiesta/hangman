# clear
import os
os.system("clear")

# initialize game
word = "UBUNTU"
guess = "------"
wrong_letters = ""

# print header
print("HANGMAN\n")

# main game loop
while True:
    print("Current Guess: {}".format(guess))
    print("Wrong Guesses: {}".format(wrong_letters))
    letter = input("Please enter a letter. > ").upper()

    #check if letter in word + form temp str
    if letter in word:
        temp = ""
        for i in range(len(word)):
            if letter == word[i]:
                temp += letter
            # already found the letter
            elif guess[i] != "-":
                temp += guess[i]
            else:
                temp += "-"
        guess = temp
    else:
        wrong_letters += letter

    #check for winner
    if word == guess:
        print("gg wp")
        exit()
    #check loser
    #if len(wrong_letters) == 5:
    #    print("LOSER")
    #    exit()
    #print the hangman
    if len(wrong_letters) == 6:
        print("""
---------
|       O
|      /|""" + chr(92) + """
|       |
|      / """ + chr(92) + """
|-------------""")
    if len(wrong_letters) == 5:
        print("""
---------
|       O
|      /|""" + chr(92) + """
|       |
|      / 
|-------------""")
    if len(wrong_letters) == 4:
        print("""
---------
|       O
|      /|""" + chr(92) + """
|       |
| 
|-------------""")
    if len(wrong_letters) == 3:
        print("""
---------
|       O
|       |""" + chr(92) + """
|       |
|
|-------------""")
    if len(wrong_letters) == 2:
        print("""
---------
|       O
|       |
|       |
|
|-------------""")
    if len(wrong_letters) == 1:
        print("""
---------
|       O
|
|
|
|-------------""")