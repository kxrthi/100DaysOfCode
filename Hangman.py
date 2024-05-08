import random

movie_list = ["inception" , "pirates of the caribbean" , "the revenant"]
movie = random.choice(movie_list)
toGuess = []
for i in movie:
    toGuess.append('-')
    
chance = 7
notWon = True

while(chance > 0 and notWon):
    guess = input("Enter a letter : ").lower()
    if guess in movie:
        for i in range(len(movie)):
            if toGuess[i] == guess:
                print("Already Guessed! chances left : ",chance)
                chance -= 1
                notWon = False
            if movie[i] == " ":
                toGuess[i] = " "
            elif movie[i] == guess:
                toGuess[i] = movie[i]
        if toGuess.count('-') == 0:
            print("Congratulations : The movie is : ",movie)
            break
        else:
            print(*toGuess )
    else:
        chance -= 1
        print("Letter not found. chances left : ",chance)
    print()
        

        