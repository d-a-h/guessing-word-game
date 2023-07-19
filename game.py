secret_word = 'arshad'
guess = ''

guess_limit = 0
while guess != secret_word  and guess_limit < 3:
    guess = input('enter ur guess : ')
    
    guess_limit += 1
    if secret_word == guess:
        print('you won')
        break
    else:
    print('you lost the game')

