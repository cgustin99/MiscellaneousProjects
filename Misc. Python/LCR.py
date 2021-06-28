import random
import numpy as np
import matplotlib.pyplot as plt

num_of_players = 5
num_of_games = 1000
center_pot = 0

def roll(num_of_dice):
    roll_list = np.array(['L', 'R', 'C', 'd', 'd', 'd'])
    current_rolls = []

    for roll in range(num_of_dice):
        current_rolls.append(random.choice(roll_list))

    return current_rolls

def initialize_players():
    array = np.zeros([num_of_players, 2])

    for i in range(num_of_players):
        array[i] = [i, 3]

    return array

def turn(array, player_number):
    global center_pot

    #Get a roll for player_i depending on their money
    if array[player_number][1] > 3:
        this_roll = roll(3)
    elif array[player_number][1] <= 3:
        this_roll = roll(int(array[player_number][1]))
    #print(this_roll)

    #Change player array based on roll
    for i in range(len(this_roll)):
        if this_roll[i] == 'L':
            array[player_number][1] -= 1
            array[player_number - 1][1] += 1
        elif this_roll[i] == 'R':
            if player_number != num_of_players - 1:
                array[player_number][1] -= 1
                array[player_number + 1][1] += 1
            else:
                array[player_number][1] -= 1
                array[player_number - (num_of_players - 1)][1] += 1
        elif this_roll[i] == 'C':
            array[player_number][1] -= 1
            center_pot += 1
        elif this_roll[i] == 'd':
            pass

    return array

def money_check(array):
    money_bin = 0

    for i in range(num_of_players):
        if array[i][1] == 0:
            money_bin += 1

    #print("Money Bin: ", money_bin)
    if money_bin == num_of_players - 1:
        money_bin = 0
        return 1
    else:
        money_bin = 0
        return 0

def game():
    players = initialize_players()
    switch = 0

    while switch == 0:
        for iter in range(num_of_players):
            if players[iter][1] != 0:
                if money_check(players) == 0:
                    #print("Player:", iter)
                    turn(players, iter)
                else:
                    switch = 1

    winner = 0
    for iter in range(num_of_players):
        if players[iter][1] != 0:
            winner = iter

    return winner

players = np.fromiter((i for i in range(num_of_players)), int)
player_wins = np.zeros(num_of_players)
y_pos = np.arange(len(players))

for i in range(num_of_games):
    player_wins[game()] += 1

plt.bar(y_pos, player_wins)
plt.xticks(y_pos, players)
plt.xlabel("Player #")
plt.ylabel("# of Wins")
plt.title("LCR Wins, N = " + str(num_of_games))
plt.show()
