from tkinter import *

root = Tk()
e=Entry(root,width=50,bg="blue",fg="white",borderwidth=5)
e.pack()
def myclick():
    hello= "Hello" + e.get()
    mylabel1=Label(root,text=hello)
    mylabel1.pack()
mybutton4=Button(root, text="enter your name", command=myclick)
mybutton4.pack()

root.mainloop()
