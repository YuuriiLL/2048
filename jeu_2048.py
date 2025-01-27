from tkinter import *

root = Tk()
root.title("2048")
root.geometry("800x600")

puissances = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

cases = [
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None],
]
frame_container = LabelFrame(root)
frame_container.pack(fill=BOTH)

for line in range(len(puissances)):
    for col in range(len(puissances[line])):
        cases[line][col] = Label(root, text=2**puissances[line][col], width=15,height=3,relief="solid",font=("Arial",15))
        cases[line][col].place(x=15 + 200 * col, y=150   + 90 * line)

root.mainloop()