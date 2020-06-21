import random


def play_game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = list(random.choice(word_list))
    covered_word = list((len(word) * '-'))
    num_tries = 0
    previous_attempts = []

    def validate_input(user_input):
        if len(user_input) != 1:
            print('You should input a single letter')
            return False
        if ord(user_input) not in range(97, 123):
            print('It is not an ASCII lowercase letter')
            return False
        if user_input in previous_attempts:
            print('You already typed this letter')
            return False
        else:
            return True

    print('H A N G M A N')
    while num_tries < 8:
        if '-' not in covered_word:
            print('You guessed the word!\nYou survived!')
            exit()
        print('\n')
        print("".join(covered_word))
        guess = input('Input a letter:')
        if not validate_input(guess):
            continue
        previous_attempts.append(guess)

        if guess not in word:
            num_tries += 1
            print('No such letter in the word')
        elif guess in covered_word:
            num_tries += 1
            print('No improvements')

        for i in range(0, len(word)):
            if word[i] == guess:
                covered_word[i] = guess

    print("You are hanged!\n")


while True:
    game_selection = input('Type "play" to play the game, "exit" to quit:')
    if game_selection == "exit":
        exit()
    elif game_selection == 'play':
        play_game()
    else:
        continue
