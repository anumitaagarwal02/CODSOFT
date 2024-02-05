from tkinter import *

root = Tk()
#creating  a label widged
mylabel1= Label(root,text="hello world!")
mylabel2= Label(root,text="my name is anumita")
#shoving it into screen
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=2,column=0)

root.mainloop()
