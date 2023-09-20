subor = open("sudoku.txt","r", encoding="utf-8")
sudoku = []

# for i in subor:
#     print(i, end="")

def inputParser(subor,sudoku):
    for row in subor:
        temp=[ ]
        for cc in row.strip():
            temp.append(int(cc))
        sudoku.append(temp)
    return sudoku

sudoku = inputParser(subor,sudoku)

def check(x:int,y:int,n:int) -> bool:
    for j in range(9):
        if sudoku[j][x]==n or sudoku[y][j] == n:
            return False
    for j in range(3):
        for i in range(3):
            zac_x = (x//3)*3
            zac_y = (x//3)*3
            if sudoku[zac_y+j][zac_x+i] == n:
                return False
    return True


def solver_of_life():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] ==0:
                for n in range(1,10):
                    if check(x,y,n):
                        sudoku[y][x] = n
                        solver_of_life()
                        sudoku[y][x] = 0
                pass
    print(sudoku)

print(solver_of_life())

