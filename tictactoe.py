def create_grid():
    return list('.........')

def dump_grid(grid):
    for y in range(3):
        for x in range(3):
            print(grid[x + (3 * y)], end='')
        print('')

def play(playerChar, position, grid):
    if position >= 9:
        return False
    if grid[position] == '.':
        grid[position] = playerChar
        return True
    return False

def vertical_win(grid):
    for i in range(3):
        pos = i
        #if current == next
        if grid[pos] == grid[pos + 3] and grid[pos + 3] == grid[pos + 6] and grid[pos] != '.':
            return True
    return False

def horizontal_win(grid):
    for i in range(3):
        pos = 3 * i
        #if current == next
        if grid[pos] == grid[pos + 1] and grid[pos + 1] == grid[pos + 2] and grid[pos] != '.':
            return True
    return False

def diagonal_win(grid):
    diag1 = grid[0] == grid[4] and grid[4] == grid[8] and grid[0] != '.'
    diag2 = grid[2] == grid[4] and grid[4] == grid[6] and grid[2] != '.'
    if diag1 or diag2:
        return True
    return False

def is_win(grid):
    win = False
    if vertical_win(grid) == True:
        print("vertical_win")
        win = True
    if horizontal_win(grid) == True:
        print("horizontal_win")
        win = True
    if diagonal_win(grid) == True:
        print("diagonal_win")
        win = True
    return win

def take_input():
    pos = input("Where do you want to play ? (type 'exit' to stop game) ")
    if pos == "exit":
        exit("Game Over.")
    return int(pos)

def main():
    playerA = 'x'
    playerB = 'o'
    player = playerA
    grid = create_grid()

    while 1:
        # print grid and take player input
        dump_grid(grid)
        position = take_input()

        # play while invalid input
        nextPlayer = play(player, position, grid)
        while nextPlayer == False:
            print("invalid position")
            pos = take_input()
            nextPlayer = play(player, position, grid)
        if is_win(grid):
            dump_grid(grid)
            exit()

        # change player if the move is valid
        if player == playerB and nextPlayer:
            player = playerA
        elif nextPlayer:
            player = playerB

main()
