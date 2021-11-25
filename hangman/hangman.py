import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import HANGMANPICS


lives = 7
point = 0
num_hint = 0
display = []
alert_message = 0


print(logo)

# reveal hint chartacters when start playing


def reveal_hint(n):
    reveal_pos = random.sample(char_pos, n)
    for i in reveal_pos:
        display[i] = list_of_char[i]
        list_of_char[i] = 'X'


# pick random word from the list
chosen_word = random.choice(word_list)
list_of_char = []
list_of_char[:0] = chosen_word

# the list of character position
char_pos = [*range(0, len(chosen_word), 1)]

# testing code
print(chosen_word)

# create blanks
display.extend(['_' for i in range(len(chosen_word))])


# if lenght of the word greater than 5 reveal 2 letters, greater than 8 reveal 3 letters
if len(chosen_word) < 5:
    num_hint = 1
    reveal_hint(num_hint)
elif len(chosen_word) >= 5 and len(chosen_word) < 8:
    num_hint = 2
    reveal_hint(num_hint)
elif len(chosen_word) >= 8:
    num_hint = 3
    reveal_hint(num_hint)

print()
print(display)

while lives > 0:
    if point == len(chosen_word) - num_hint and lives == 7:
        print()
        print("===========================")
        print("You nailed it perfectly !!!")
        print("===========================")
        quit()
    elif point == len(chosen_word) - num_hint:
        print()
        print("==========")
        print("You won!!!")
        print("==========")
        quit()

    # Get input from user
    print()
    guess_char = input("Guess a letter : ").lower()

    # check the answer
    if guess_char in list_of_char:
        pos = list_of_char.index(guess_char)
        display[pos] = list_of_char[pos]
        print()
        print(display)
        list_of_char[pos] = 'X'
        point += 1
        alert_message = 0

    # if the guess is wrong output hangman
    else:
        alert_message += 1
        lives -= 1
        print()
        print(
            f"You guessed {guess_char}, that's not in the word, You have {lives} lives left")
        print(HANGMANPICS[7-lives-1])

    # if the player fail 3 time in a row alert "====Try Harder,You Can do It===="

    if alert_message > 0 and alert_message % 3 == 0:
        print()
        print("====Try Harder,You Can do It====")
        print()
        print(display)
        print()

print()
print("============")
print("Game Over!!!")
print("============")
print()
print(f"The word is : {chosen_word} ")
