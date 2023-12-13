import tkinter as tk

win = tk.Tk()

canvas = tk.Canvas(win, width = 450, height = 450, bg = "white")
canvas.pack()


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
            zac_y = (y//3)*3
            if sudoku[zac_y+j][zac_x+i] == n:
                return False
    return True

def create_grid():
    for x in range(9):
        if (x*50)%3==0:
            widt = 5
        else:
            widt = 2
        canvas.create_line(x*50,0,x*50,450,width=widt)
        canvas.create_line(0,x*50,450,x*50,width=widt)
    for y in range(9):
        for x in range(9):
            canvas.create_text(x*50+10,y*50,text = str(sudoku[y][x]),anchor = "nw",font = ("Arial",35))


ran = 0
temp = False
def solver_of_life():
    global sudoku,temp,ran
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] ==0:
                for n in range(1,10):
                    if check(x,y,n):
                        sudoku[y][x] = n
                        solver_of_life()
                while ran!=9:
                    if sudoku[ran].count(0)!=0:
                        sudoku[y][x]=0
                        ran = 0
                        return
                    else:
                        ran+=1
                return

    create_grid()
solver_of_life()

def create_grid():
    for x in range(9):
        if (x*50)%3==0:
            widt = 5
        else:
            widt = 2
        canvas.create_line(x*50,0,x*50,450,width=widt)
        canvas.create_line(0,x*50,450,x*50,width=widt)
    for y in range(9):
        for x in range(9):
            canvas.create_text(x*50+10,y*50,text = str(sudoku[y][x]),anchor = "nw",font = ("Arial",35))


win.mainloop()

