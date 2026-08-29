chances = 6
correct_Letters = 0
cont_Var = 1
incorrect_Guess = []
used_Letters = []
secret_word = 'clown'



while cont_Var == 1:
    player_Guess = input("Please enter a letter (a-z): ")
    if player_Guess in used_Letters:
        print("Invalid letter, please try again.")
    elif player_Guess in secret_word:
        print("Good job! ", player_Guess, "is in the word")
        correct_Letters += 1
        cont_Var +=1
        used_Letters.append(player_Guess)
        
    
    else:
        print("sorry, ", player_Guess, "is not in the word")
        chances -= 1
        cont_Var+=1
        used_Letters.append(player_Guess)
        incorrect_Guess.append(player_Guess)





display_word = ""
for letter in secret_word:
    if letter in used_Letters:
        display_word += letter + " "
    else:
        display_word += "_ "
            
print("Word:", display_word)
print("Incorrect guesses:", incorrect_Guess)
print("Chances left:", chances)
