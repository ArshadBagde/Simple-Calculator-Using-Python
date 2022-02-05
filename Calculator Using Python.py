#https://www.youtube.com/watch?v=fbxsYcSccJE&ab_channel=CodeWithHarry

from tkinter import *
root = Tk()
root.geometry("800 * 500")
root.tilte("Calculator By CodeWithArshad")
root.wm_iconbitmap("1.icon")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="gray")
b = Button(f,text="9", font="lucida 35 bold")
b.pack()
f.pack()

root.mainloop()