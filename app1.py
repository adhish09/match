from tkinter import *
import hashlib
from difflib import SequenceMatcher

def hash_file(fileName1, fileName2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(fileName1, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    with open(fileName2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

    return h1.hexdigest(),h2.hexdigest()


root=Tk()
root.title('Calculator')
root.geometry('750x500')
bg=PhotoImage(file='C:\\Users\\adhis\\Downloads\\bg.png')
label1=Label(root,image=bg)
label1.place(x=0,y=0)
e1=Entry(root,width=100,borderwidth=5,)
e1.grid(row=0,column=0)
e1.place(x=75,y=110)
l1=Label(root,text='Enter the path of the first file',borderwidth=5,width=50,height=1)
l1.grid(row=1,column=0)
l1.place(x=200,y=150)
e2=Entry(root,width=100,borderwidth=5)
e2.grid(row=2,column=0)
e2.place(x=75,y=200)
l2=Label(root,text='Enter the path of the first file',borderwidth=5,width=50,height=1)
l2.grid(row=3,column=0)
l2.place(x=200,y=250)
def compare(file1,file2):
    msg1,msg2 = hash_file(file1,file2)
    print(msg1+"\t"+msg2)
    print((SequenceMatcher(None,msg1,msg2).ratio())*100)
    Label(root,text=str((SequenceMatcher(None,msg1,msg2).ratio())*100)).grid(row=6,column=0)
button1=Button(root,bg='yellow',text='Compare',width=20,height=3,borderwidth=5,command=lambda: compare(e1.get(),e2.get()))
button1.grid(row=4,column=0)
button1.place(x=300,y=300)
root.mainloop()
