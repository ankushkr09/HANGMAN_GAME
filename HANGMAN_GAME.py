import random
import hangman_art
import hangman_words

#print hangman logo from hangman_art module:
print(hangman_art.logo)

#assign words list from hangman_module to word_list:
word_list = hangman_words.word_list

#Generate a random word from hangman_words module:
chosen_word = random.choice(word_list)
print(chosen_word)

#assign length of word chosen to variable word_length:
word_length = len(chosen_word)

#take 6 lives for user and assign false to end of game variable
lives = 6
end_of_game = False

#create an empty list and fill them with '_':
display = []
for letter in range(word_length):
    display.append('_')
#take user input one by one until they win or loose:
while not end_of_game:
    guess = input("Enter a word: ").lower()
    #if guess is already guessed before print them a message:
    if guess in display:
        print(f"You already guessed '{guess}' before.")
    #to check guessed word in there in chosen word or not:
    for position in range(word_length):
        letter = chosen_word[position]

        #if guessed word is present in chosen word:
        if guess == letter:
            display[position] = letter
            
            if '_' not in display:
                end_of_game = True
                print("You Won!")
    print(f"{' '.join(display)}")
    #when guessed word not in chosen word:
    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not present in word.")
        #reduce the life by 1
        lives -= 1
        print(f"You lost '1' life. You have '{lives}' life left.")
        if lives == 0:
            end_of_game = True
            print("You Lost!")
        #print different stages of hangman on every mistake on position of lives.
        print(hangman_art.stages[lives])

