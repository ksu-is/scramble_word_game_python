import quiz

while True:
    q = quiz.Quiz()
    q.show_option()

    game_over = input("want to play again? (y/n) ")
    if game_over == 'y':
        True
    else:
        print('Thank you for playing')
        exit()