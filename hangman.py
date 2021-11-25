import random

life = 7
point = 0
word_list = ['house', 'cat', 'dog', 'human', 'laptop',
             'computer', 'car', 'boat', 'pig', 'chicken', 'football']
num_hint = 0
reveal_answer = []
alert_message = 0

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# reveal hint chartacters when start playing


def reveal_hint(n):
    global life
    reveal_pos = random.sample(char_pos, n)
    for i in reveal_pos:
        reveal_answer[i] = list_of_char[i]
        list_of_char[i] = 'X'


# pick random word from the list
chosen_word = random.choice(word_list)
list_of_char = []
list_of_char[:0] = chosen_word

reveal_answer.extend(['_' for i in range(len(chosen_word))])

# the list of order character
char_pos = [*range(0, len(chosen_word), 1)]
print(chosen_word)


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

print(reveal_answer)

while life > 0:
    if point == len(chosen_word) - num_hint and life == 7:
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
    guess_char = input("Guess a character : ").lower()

    # check the answer
    if guess_char in list_of_char:
        pos = list_of_char.index(guess_char)
        reveal_answer[pos] = list_of_char[pos]
        print(reveal_answer)
        list_of_char[pos] = 'X'
        point += 1
        alert_message = 0

    # if the guess is wrong output hangman
    else:
        alert_message += 1
        life -= 1
        print(HANGMANPICS[7-life-1])

    # if the player fail 3 time in a row alert "====Try Harder,You Can do It===="

    if alert_message > 0 and alert_message % 3 == 0:
        print()
        print("====Try Harder,You Can do It====")
        print(reveal_answer)
        print()

print()
print("============")
print("Game Over!!!")
print("============")
print()
print(f"The word is : {chosen_word} ")
