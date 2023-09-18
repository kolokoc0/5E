
def prepare_matrix():
    matrix = []
    sub_matrix = []
    for y in range(8):
        for x in range(8):
            sub_matrix.append(0)
        matrix.append(sub_matrix)
        sub_matrix = [ ]
    return matrix

matrix = prepare_matrix()



def check(x:int,y:int) -> bool:
    for j in range(8):
        for i in range(8):
            if j==y:
                if matrix[y][i]==1:
                    return False
            elif i==x:
                if matrix[j][x]==1:
                    return False
            elif i+j==x+y:
                if matrix[j][i]==1:
                    return False
            elif i-j==x-y:
                if matrix[j][i]==1:
                    return False
    return True

count = 0
def drticka(dama:int):
    global matrix,count
    if dama==8:
        print(matrix)
        print("-"*210)
        count +=1
    else:
        for i in range(8):
            if check(i,dama):
                matrix[dama][i] = 1
                drticka(dama+1)
                matrix[dama][i] = 0

drticka(0)
print(count)

