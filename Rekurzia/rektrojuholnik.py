import tkinter as tk
import math
window = tk.Tk()

canvas= tk.Canvas(window,width = 1000,height = 1000)
canvas.pack()

def sierp(x,y,d,hlbka=9):
    if hlbka>0:
        hlbka -= 1
        v = ((-1)*d*math.sin(math.radians(60)))
        canvas.create_line(x,y,x+d,y)
        canvas.create_line(x+d,y,x+d//2,y+v)
        canvas.create_line(x,y,x+d//2,y+v)
        sierp(x,y,d//2,hlbka)
        sierp(x+d//2,y,d//2,hlbka)
        sierp(x+d//4,y+v//2,d//2,hlbka)



sierp(200,800,600)

window.mainloop()
