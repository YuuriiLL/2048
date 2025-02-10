# Nom du programme : jeu_2048
# Auteur : Yuri Lima.
# Date : 10.02.2025

from tkinter import *
import random

def spawn_tile():
    # Choisir une position vide (0) pour ajouter une nouvelle tuile
    empty_positions = []
    for i in range(4):
        for j in range(4):
            if puissances[i][j] == 0:
                empty_positions.append((i, j))
    if empty_positions:
        i, j = random.choice(empty_positions)
        puissances[i][j] = random.choice([2, 4])

def pack_4(a, b, c, d, reverse=False):
    moves = 0
    if reverse:
        a, b, c, d = d, c, b, a  # Inverser pour gérer droite/bas avec la même logique

    # Déplacement des tuiles vers la gauche (ou vers le haut si colonne)
    if a == 0:
        a, b, c, d = b, c, d, 0
        moves += 1
    if b == 0:
        b, c, d = c, d, 0
        moves += 1
    if c == 0:
        c, d = d, 0
        moves += 1

    # Fusion des tuiles identiques
    if a == b and a != 0:
        a, b, c, d = a * 2, c, d, 0
        moves += 1
    if b == c and b != 0:
        b, c, d = b * 2, d, 0
        moves += 1
    if c == d and c != 0:
        c, d = c * 2, 0
        moves += 1

    # Déplacer à nouveau après la fusion
    if a == 0:
        a, b, c, d = b, c, d, 0
        moves += 1
    if b == 0:
        b, c, d = c, d, 0
        moves += 1
    if c == 0:
        c, d = d, 0
        moves += 1

    if reverse:
        a, b, c, d = d, c, b, a  # Réinverser pour retrouver l'ordre initial

    return a, b, c, d, moves


root = Tk()
root.title("2048")
root.geometry("600x700")

# Initialisation de la grille (une matrice de 4x4 avec des zéros)
puissances = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

cases = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]

colors = {
    0: '#FFFFFF',
    2: '#FFCCFF',
    4: '#FF99FF',
    8: '#FF66FF',
    16: '#FF33FF',
    32: '#FF00FF',
    64: '#CC00CC',
    128: '#990099',
    256: '#CC99FF',
    512: '#9933FF',
    1024: '#7F00FF',
    2048: '#6600CC',
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

lbl_texte = Label(frame_texte, text="Glissez les chiffres et obten"
                                    "ez la tuile 2048", font=("Arial", 10))
lbl_texte.pack()

# BUTTONS
bt_new = Button(frame_button, text="New", width=10, command=lambda: new_game())
bt_new.pack(side=RIGHT, padx=35)

# Placer les cases dans la frame_tableau
def display_game():
    for line in range(len(puissances)):
        for col in range(len(puissances[line])):
            # Si les cases n'ont pas encore été créées, on les crée
            if cases[line][col] is None:
                cases[line][col] = Label(frame_tableau, text=puissances[line][col], bg=colors.get(puissances[line][col], '#FFFFFF'), width=8, height=4, relief="solid", font=("Arial", 15), fg="White")
                cases[line][col].grid(row=line, column=col, padx=10, pady=10)
            else:
                cases[line][col].config(text=puissances[line][col], bg=colors.get(puissances[line][col], '#FFFFFF'))
    return

def new_game():
    global puissances
    puissances = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    spawn_tile()
    spawn_tile()
    display_game()

def move_left(event):
    moved = False
    for row in range(4):
        a, b, c, d, moves = pack_4(*puissances[row], reverse=False)
        if moves > 0:
            moved = True
        puissances[row] = [a, b, c, d]
    if moved:
        spawn_tile()
    display_game()

def move_right(event):
    moved = False
    for row in range(4):
        a, b, c, d, moves = pack_4(*puissances[row], reverse=True)
        if moves > 0:
            moved = True
        puissances[row] = [a, b, c, d]
    if moved:
        spawn_tile()
    display_game()

def move_up(event):
    moved = False
    for col in range(4):
        col_values = [puissances[row][col] for row in range(4)]
        a, b, c, d, moves = pack_4(*col_values, reverse=False)
        if moves > 0:
            moved = True
        for row in range(4):
            puissances[row][col] = [a, b, c, d][row]
    if moved:
        spawn_tile()
    display_game()

def move_down(event):
    moved = False
    for col in range(4):
        col_values = [puissances[row][col] for row in range(4)]
        a, b, c, d, moves = pack_4(*col_values, reverse=True)
        if moves > 0:
            moved = True
        for row in range(4):
            puissances[row][col] = [a, b, c, d][row]
    if moved:
        spawn_tile()
    display_game()


root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Down>", move_down)
root.bind("<Up>", move_up)

# Démarrer un nouveau jeu au lancement de l'application
new_game()

root.mainloop()