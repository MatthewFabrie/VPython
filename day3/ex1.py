import random
import time

def tugOfWar():
    counter = 0
    score = 0
    board = '|               *               |'

    print('               START               ')
    while (score < 15 and score > -15):
        coin = random.randint(0, 1)
        if coin == 0:
            score -= 1
            star_position = board.find('*')
            if star_position > 1:
                new_board = list(board)
                new_board[star_position], new_board[star_position - 1] = new_board[star_position - 1], new_board[star_position]
                board = "".join(new_board)
        else:
            score += 1
            star_position = board.find('*')
            if star_position < len(board) - 2:
                new_board = list(board)
                new_board[star_position], new_board[star_position + 1] = new_board[star_position + 1], new_board[star_position]
                board = "".join(new_board)
        counter += 1
        if (score < 1):
            print(board + str(score))
        else:
            print(board + '+' + str(score))
        time.sleep(0.03)
    print(counter)

tugOfWar()
