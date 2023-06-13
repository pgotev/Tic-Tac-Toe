from math import ceil


def print_field():
    for row in field:
        print("|", end="")
        print("|".join(str(x) for x in row), end="")
        print("|")



def check_win_condition(r, c):
    player = field[r][c]

    def check_horizontal():
        sequence_counter = 1
        for i in range(1, win_condition):
            if 0 <= c + i < cols:
                if field[r][c + i] == player:
                    sequence_counter += 1
                else:
                    break
        for i in range(1, win_condition):
            if 0 <= c - i < cols:
                if field[r][c - i] == player:
                    sequence_counter += 1
                else:
                    break
        return sequence_counter >= win_condition

    def check_vertical():
        sequence_counter = 1
        for i in range(1, win_condition):
            if 0 <= r + i < rows:
                if field[r + i][c] == player:
                    sequence_counter += 1
                else:
                    break
        for i in range(1, win_condition):
            if 0 <= r - i < rows:
                if field[r - i][c] == player:
                    sequence_counter += 1
                else:
                    break
        return sequence_counter >= win_condition

    def check_diagonal():
        sequence_counter = 1
        for i in range(1, win_condition):
            if 0 <= r + i < rows and 0 <= c + i < cols:
                if field[r + i][c + i] == player:
                    sequence_counter += 1
                else:
                    break
        for i in range(1, win_condition):
            if 0 <= r - i < rows and 0 <= c - i < cols:
                if field[r - i][c - i] == player:
                    sequence_counter += 1
                else:
                    break
        return sequence_counter >= win_condition

    def check_reverse_diagonal():
        sequence_counter = 1
        for i in range(1, win_condition):
            if 0 <= r + i < rows and 0 <= c - i < cols:
                if field[r + i][c - i] == player:
                    sequence_counter += 1
                else:
                    break
        for i in range(1, win_condition):
            if 0 <= r - i < rows and 0 <= c + i < cols:
                if field[r - i][c + i] == player:
                    sequence_counter += 1
                else:
                    break
        return sequence_counter >= win_condition

    return check_horizontal() or check_vertical() or check_diagonal() or check_reverse_diagonal()


def apply_player_move(player):
    while True:
        row, column = player_makes_move(player)
        if field[row][column] == "X" or field[row][column] == "O":
            print("This space is taken. Pick a free space.")
        else:
            break

    field[row][column] = player
    return row, column


def player_makes_move(player):
    while True:
        try:
            chosen_number = int(input(f"{players[player]}({player}), please pick a number in the field: "))
        except ValueError:
            print("Value is invalid. Try again.")
            continue

        if not (0 <= chosen_number <= rows * cols):
            print("Number is outside the field. Try again.")
            continue
        else:
            break

    chosen_row = ceil(chosen_number / cols) - 1
    chosen_col = chosen_number % cols - 1

    return chosen_row, chosen_col


print("WELCOME\nThis is Tic-Tac-Toe.")

while True:
    rows = int(input("Enter the numbers of rows in the playing field: "))
    cols = int(input("Enter the numbers of columns in the playing field: "))
    if rows <= 0 or cols <=0:
        print("Number of rows and columns cannot be a less than 1. Please enter valid values.")
    else:
        break

while True:
    win_condition = int(input("Pick the win condition for the current game: "))
    if win_condition > rows and win_condition > cols:
        print(f"The win condition is too big for the field. Please pick a number that fits in the field({rows}x{cols})")
    else:
        break


player_1 = input("Pick a name for the player № 1: ")
player_2 = input("Pick a name for the player № 2: ")

while True:
    player_1_sign = input(f"{player_1} whould you like to play with 'X' or 'O'?")
    if player_1_sign.lower() != 'x' and player_1_sign.lower() != 'o':
        print("Incorrect sign. Try again.")
    else:
        break
player_2_sign = 'O' if player_1_sign == 'X' else 'X'

players = {player_1_sign: player_1, player_2_sign: player_2}
field = [[] for _ in range(rows)]
counter = 1
for i in range(rows):
    for j in range(cols):
        field[i].append(counter)
        counter += 1

print("Game starting now!")
print_field()
field = [[" "] * cols for _ in range(rows)]

current_player, next_player = player_1_sign, player_2_sign

while True:
    move_coordinates = apply_player_move(current_player)
    print_field()

    if check_win_condition(*move_coordinates):
        print(f"{players[current_player]} won the game!")
        exit()
    for row in field:
        if " " in row:
            break
    else:
        print("No more free spaces. Draw.")
        exit()

    current_player, next_player = next_player, current_player
