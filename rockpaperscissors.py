#  rock paper scissors first try
import random
import math

def play():
    user = input("Whats your choice? 'r' for rock 'p' for paper 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return 0, user, computer

    # r > s, s > p, p > r
    if is_win(user,computer):
        return 1, user, computer
    return -1, user, computer


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_needed = math.ceil(n/2)
    while player_wins < wins_needed and computer_wins < wins_needed:
        result, user, computer = play()
        # tie
        if result == 0:
            print("its a tie. you and the computer have both chosen {}. \n".format(user))
        # you win
        elif result == 1:
            player_wins += 1
            print("you win! you have chosen {}. whilst the computer has chosen {}. \n".format(user,computer))
        # you lose
        else:
            computer_wins += 1
            print("you lose. you chose {}. the computer has chosen {}. \n".format(user,computer))
        print('\n')

    if player_wins > computer_wins:
        print("you win best out of {} games!!".format(n))
    else:
        print("you suck!!!!! the computer has won best out of {}.".format(n))


if __name__ == '__main__':
    play_best_of(3) # 2s



