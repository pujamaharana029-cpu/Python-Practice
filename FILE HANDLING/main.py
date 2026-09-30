from pathlib import Path #library through which path is readed
import os

def readfileandfolder():
    path=Path('FILE HANDLING')
    items=list(path.rglob('*')) #rglob means recursive glob
    for i,items in enumerate(items): #i- index ,items-values
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder()
        name=input("tell the file name:-")
        p=Path("FILE HANDLING")/name
        if not p.exists():
            with open(p,"w")as fs:
                data=input("what you want to write in this file:- ")
                fs.write(data)
            print("file created successfully")
        else:
            print("This file already exist")
    except Exception as err:
        print(f"An error occured as{err}")


def readfile():
    readfileandfolder()
    name=input("which file you want to read:- ")
    p=Path("FILE HANDLING")/name
    try:
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            print("Read successfully")
        else:
            print("the file doesn't exists")
    except Exception as err:
        print(f"An error occured as{err}")


def updatefile():
    try:
        readfileandfolder()
        name=input("which file you want to update:- ")
        p=Path("FILE HANDLING")/name
        if p.exists() and p.is_file():
            print("press 1 for changing the name of the file:- ")
            print("Press 2 for overwriting the data of your file:- ")
            print("press 3 for appending some content in your file:- ")

            res=int(input("tell your response:- "))

            if res==1:
                name2=input("tell your new file name:- ")
                p2=Path("FILE HANDLING")/name2
                p.rename(p2)
            if res==2:
                with open(p,'w')as fs:
                    data=input("what you want to write  this will overwrite the data:- ")
                    fs.write(data)
            if res==3:
                with open(p,'a')as fs:
                    data=input("what you want to append:- ")
                    fs.write(" " +data)
    except Exception as err:
        print(f"An error occured as{err}")

def deletefile():
    try:
        readfileandfolder()
        name=input("which file you want to delete:- ")
        p=Path("FILE HANDLING")/name
        if p.exists() and p.is_file():
            os.remove(p)
            print("file removed successfully")
        else:
            print("no such file exists")
    except exception as err:
            print(f"An errornoccured as {err}")




print("press 1 for creatiing a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check=int(input("tell me your response:-"))
if check==1:
    createfile()
if check==2:
    readfile()
if check==3:
    updatefile()
if check==4:
    deletefile()