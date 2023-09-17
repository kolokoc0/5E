import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=900,height=900)
canvas.pack()

def sierpinsky(x,y,d,hlbka=9):
    if hlbka>0:
        hlbka -=1
        canvas.create_rectangle(x,y,x+d,y+d)
    
        sierpinsky(x,y,d//3,hlbka)
        sierpinsky(x,y+d//3,d//3,hlbka)
        sierpinsky(x,y+2*(d//3),d//3,hlbka)
        sierpinsky(x+d//3,y,d//3,hlbka)
        sierpinsky(x+2*(d//3),y,d//3,hlbka)
        sierpinsky(x+2*(d//3),y+d//3,d//3,hlbka)
        sierpinsky(x+d//3,y+2*(d//3),d//3,hlbka)
        sierpinsky(x+2*(d//3),y+2*(d//3),d//3,hlbka)



sierpinsky(100,100,700)
window.mainloop()