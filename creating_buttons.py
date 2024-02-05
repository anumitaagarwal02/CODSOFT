from tkinter import *

root = Tk()
mybutton=Button(root, text="click here")
mybutton.pack()
#disable button
mybutton2=Button(root, text="click here", state=DISABLED)
mybutton2.pack()
#exanding button
mybutton3=Button(root, text="click here", padx=50)
mybutton3.pack()
#defining a buton
def myclick():
    mylabel1=Label(root,text="look i clicked a button!")
    mylabel1.pack()
mybutton4=Button(root, text="click here1", command=myclick)
mybutton4.pack()
#changing the font and bg color
mybutton5=Button(root, text="click here", fg="blue",bg="yellow")
mybutton5.pack()
root.mainloop()
