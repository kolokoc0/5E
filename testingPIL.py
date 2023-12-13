from PIL import Image
queen_img = Image.open("D:\SKola\queen.png")
queen_img = queen_img.resize((125,125))

queen_img.show()


def prepare_board():
    img = Image.new("RGBA",(1000,1000),"white")
    pixels = img.load()
    temp = True
    for y in range(0,1000):
        for x in range(0,1000):
            if (y//125)%2==0:
                if (x//125)%2==0:
                    pixels[x,y] = (255,255,255)
                else:
                    pixels[x,y] = (20,100,0)
            elif (y//125)%2==1:
                if (x//125)%2 == 0:
                    pixels[x,y] = (20,100,0)
                else:
                    pixels[x,y] = (255,255,255)
    return img
img = prepare_board()

placement = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0]]

def place_queens(placement):
    for row in placement:
        for num in row:
            if num==1:
                y = ((placement.index(row))*125)
                x = ((row.index(num))*125)
                img.paste(queen_img,(y,x),queen_img) 
    return img

img = place_queens(placement)
img.show()
