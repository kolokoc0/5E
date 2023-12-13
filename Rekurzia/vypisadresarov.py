import os

def Folders(path,depth=0):
    for item in os.listdir(path):
        if os.path.isdir(path+"\\"+item) and item[0] not in ".$":
            if len(os.listdir(path+"\\"+item))!=0: #vrati aj subory ktore su v danom adresari treba len adresare nie subory
                print('-'*depth,item)
                Folders(path+"\\"+item,depth+1)
            else:
                print("-"*depth,item)
Folders("D:\\Skola")
