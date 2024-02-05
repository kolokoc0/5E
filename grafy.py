import time
import tkinter as tk

with open("vrcholy.txt","r",encoding="UTF-8") as file1:
    file1 = file1.readlines()
with open("hrany.txt","r",encoding="UTF-8") as file2:
    file2= file2.readlines()

file1 = [line.strip().split(';') for line in file1]

file2 = [line.strip().split(';') for line in file2]

mesta={}
visited = []
mesta_nazvy = {}
neighbouring = {}

win=tk.Tk()
canvas=tk.Canvas(width=1000,height=600,bg="white")
canvas.pack()

def kresli_mesta(mesta):
    for i in file1:
        parts=i
        x=int(parts[1])
        y=int(parts[2])
        mesta_nazvy[parts[0]] = canvas.create_oval(x-5,y-5,x+5,y+5,fill="red",tag=parts[0])

        canvas.create_text(x,y+10,text=parts[0],fill='red')
        mesta[parts[0]]=[x,y]

    kresli_hrany(neighbouring)

def kresli_hrany(neighbouring):
    keys = []
    for i in file2:
        parts=i
        canvas.create_line(mesta[parts[0]][0], mesta[parts[0]][1], mesta[parts[1]][0], mesta[parts[1]][1], fill="black")
        if parts[0] in keys:
            neighbouring[parts[0]][parts[1]] = 0
        else:
            neighbouring[parts[0]] = {parts[1]:0}
            keys.append(parts[0])
        
        if parts[1] in keys:
            neighbouring[parts[1]][parts[0]] = 0
        else:
            neighbouring[parts[1]] = {parts[0]:0}
            keys.append(parts[1])
        
kresli_mesta(mesta)

def depth_search(city):
    visited.append(city)
    canvas.itemconfig(mesta_nazvy[city],fill='lime')
    canvas.update()
    time.sleep(0.2)
    for neighbour in neighbouring[city]:
        if neighbour not in visited:
            depth_search(neighbour)

visited_overall = []
predecesors = {}


def width_search(city):
    visited.append(city)
    canvas.itemconfig(mesta_nazvy[city],fill='lime')
    visited_overall.append(city)
    temp = city
    while len(visited)>0:
        for i in neighbouring[visited[0]]:
            if i not in visited_overall:
                predecesors[i] = temp
                canvas.update()
                time.sleep(0.00001)
                canvas.itemconfig(mesta_nazvy[i],fill='lime')
                visited.append(i)
                visited_overall.append(i)
        visited.pop(0)
        if len(visited)>0:
            temp = visited[0]
    print(predecesors)

def back_track(start,end):
    temp = end
    path = [end]
    while temp!=start:
        path.append(predecesors[temp])
        temp = predecesors[temp]
    print(path[::-1])



start = ''
end = ''
#depth_search('Bratislava')
width_search(start)
back_track(start,end)

win.mainloop()