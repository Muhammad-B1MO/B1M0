from tkinter import*

root = Tk()
root.title("welcome")
root.geometry('200x150')
root.resizable(False, False)

def user():
    user=ent.get()
    print(user)

ent = Entry(root, width=20)
ent.place(x=20, y =20)

but=Button(root, text="hello",width=20,command=user)
but.place(x=20,y=100)

root.mainloop()
