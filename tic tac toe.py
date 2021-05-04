def win_check(x_cells, o_cells, the_round):
    win_sets=[{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{7,5,3},{1,5,9}]
    for win_set in win_sets:
        if win_set.issubset(o_cells):
            print("\nO player wins!")
            return True
        if win_set.issubset(x_cells):
            print("\nX player wins!")
            return True
    else:
        return False

def show(x_cells, o_cells):
    grid =   ' 7 | 8 | 9 \n ----------- \n 4 | 5 | 6 \n ----------- \n 1 | 2 | 3'
    for i in range(1,10):
        if i in x_cells:
            grid=grid.replace(str(i), 'x')
        if i in o_cells:
            grid=grid.replace(str(i), 'o')
        else:
            grid=grid.replace(str(i), ' ')
    print(grid)


def valid_cell(x_cells, o_cells):
    cell = int(input("Please enter a cell: "))
    while cell<1 or cell>9 or cell in x_cells or cell in o_cells:
        cell = int(input("Please enter a valid cell: "))
    return cell

def tic_tac_toe():
    x_cells = set()
    o_cells = set()
    
    the_round = 1

    while the_round < 10:
        player = 'x' if the_round%2 == 1 else 'o'
        print(f'\nRound {the_round} it is {player} s turn to play \n')

        cell = valid_cell(x_cells, o_cells)
        if the_round % 2 == 1:
            x_cells.add(cell)
        else:
            o_cells.add(cell)
            
        if win_check(x_cells, o_cells, the_round):
            show(x_cells, o_cells)
            return

        show(x_cells, o_cells)        
        the_round += 1
    print('\ndraw')

if __name__ == '__main__':
    print(' 7 | 8 | 9 \n ----------- \n 4 | 5 | 6 \n ----------- \n 1 | 2 | 3')
    tic_tac_toe()
    
