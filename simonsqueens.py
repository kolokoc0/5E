from PIL import Image
image=Image.open("Queen logo.jpg").convert("RGBA")
image = image.resize((100,100))
s=0
number=1

def set():
    lst=[]
    temp=[]
    for y in range(8):
        for x in range(8):
            temp.append(0)
        lst.append(temp)
        temp=[ ]
    return lst
lst=set()

def pieces(position):
    for row in position:
        for num in row:
            if num==1:
                y=((position.index(row))*100)
                x=((row.index(num))*100)
                picture.paste(image,(y,x),image)
    return picture

def grinder(onequeen):
    global lst,s,number,picture
    if onequeen==8:
        print(lst)
        s+=1

        photo=Image.new("RGB",(800, 800),"white",)
        pixels=photo.load()
        t=True
        for a in range(0,800):
            for b in range(0,800):
                if (a//100)%2==0:
                    if (b//100)%2==0: pixels[b,a]=(255,255,255)
                    else: pixels[b,a]=(0,0,0)
                elif (a//100)%2==1:
                    if (b//100)%2==0: pixels[b,a]=(0,0,0)
                    else: pixels[b,a]=(255,255,255)
        picture=photo

        picture=pieces(lst)
        picture.save(f"possibility{number}.jpeg",)
        number+=1
    else:
        for z in range(8):
            for x in range(8):
                for y in range(8):
                    if x==onequeen:
                        if lst[onequeen][y]==1: 
                            check = False
                            break
                    elif y==z:
                        if lst[x][z]==1:
                            check = False
                            break
                    elif y+x==z+onequeen:
                        if lst[x][y]==1:
                            check = False
                            break
                    elif y-x==z-onequeen:
                        if lst[x][y]==1: 
                            check = False
                            break
            check = True

            if check==True:
                lst[onequeen][z]=1
                grinder(onequeen+1)
                lst[onequeen][z]=0

grinder(0)