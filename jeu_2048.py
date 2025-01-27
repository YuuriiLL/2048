from tkinter import *

root = Tk()
root.title("2048")
root.geometry("600x600")

puissances = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

"""
puissances = [
    [0,2,0,0],
    [0,0,0,0],
    [0,2,0,0],
]
"""

cases = [
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None],
]

colors = {
    1 : '#FFCCFF',
    2 : '#FF99FF',
    3 : '#FF66FF',
    4 : '#FF33FF',
    5 : '#FF00FF',
    6 : '#CC00CC',
    7 : '#990099',
    8 : '#CC99FF',
    9 : '#9933FF',
    10 :'#7F00FF',
    11 :'#6600CC',
    12 :'#000000',
}

# frames
frame_container = Frame(root)
frame_container.pack(fill=BOTH, expand=True)

frame_tableau = LabelFrame(root, width=100, height=50, relief="solid", borderwidth=1)
frame_tableau.pack(expand=True, padx=20, pady=20)

frame_top = Frame(frame_container)
frame_top.pack(fill=X)

frame_top_score = Frame(frame_top)
frame_top_score.pack(side=RIGHT, padx=50)

frame_score = Frame(frame_top_score, pady=10, padx=20)
frame_score.pack(side=LEFT, padx=10)

frame_top_record = Frame(frame_top_score, pady=10, padx=25)
frame_top_record.pack()

frame_button = Frame(frame_container)
frame_button.pack(fill=X)

frame_texte = Frame(frame_button)
frame_texte.pack(side=LEFT, padx=30, pady=5)

# labels
lbl_logo = Label(frame_top, text="2048", font=("Arial", 50), fg="Red")
lbl_logo.pack(side=LEFT, padx=30, pady=10)

lbl_score = Label(frame_score, text="SCORE", font=("Arial", 8))
lbl_score.pack(side=LEFT)

lbl_top = Label(frame_top_record, text="TOP", font=("Arial", 8))
lbl_top.pack()

lbl_texte = Label(frame_texte, text="Glissez les chiffres et obtenez la tuile 2048", font=("Arial", 10))
lbl_texte.pack()

# BUTTONS
bt_new = Button(frame_button, text="New", width=10)
bt_new.pack(side=RIGHT, padx=35)

# Placer les cases dans la frame_tableau
for line in range(len(puissances)):
    for col in range(len(puissances[line])):
        cases[line][col] = Label(frame_tableau, text=2**puissances[line][col], bg=colors[puissances[line][col]], width=8, height=4, relief="solid", font=("Arial", 15), fg="White")
        cases[line][col].grid(row=line, column=col, padx=10, pady=10)

def display_game():
    for line in range(len(puissances)):
        for col in range(len(puissances[line])):
            cases[line][col].config(frame_tableau, text=puissances[line][col],bg=colors[puissances[line][col]])
    return



root.mainloop()
