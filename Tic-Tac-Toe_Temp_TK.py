from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Tic-Tac-Toe')
root.geometry('1280x800')

#Dividing the Screen into 2 parts
top = Frame(root, borderwidth=1, relief="solid")
bottom = Frame(root, borderwidth=2, relief="solid")
left = Frame(bottom, borderwidth=2, relief="solid")
right = Frame(bottom, borderwidth=2, relief="solid")
container = Frame(left, borderwidth=1, relief="solid")
container2 = Frame(left, borderwidth=2, relief="solid")
container3 = Frame(right, borderwidth=2, relief="solid")
container4 = Frame(right, borderwidth=2, relief="solid")
container5 = Frame(left, borderwidth=2, relief="solid")

#Separator - To separate the Buttons
sep = ttk.Separator(container)

#Modes of Playing two Buttons
b1 = Button(container, text = "Player vs Player", font="Consolas 16 bold", fg="white", bg="green", activebackground="gray", width="20", relief="groove",
            padx=10, pady=10)
b2 = Button(container, text="Player vs Computer", font="Consolas 16 bold", fg="white", bg="green", activebackground="gray", width="20", relief="groove",
            padx=10, pady=10)


#Player Names - User Input Textfields
player1 = Label(container2, text = "Player 1: ", font="Times 18").place(x = 30,y = 50)
player2 = Label(container2, text = "Player 2: ", font="Times 18").place(x = 30,y = 90)

e1 = Entry(container2, width = 50, relief="groove", font="Times 14").place(x = 120, y = 55)  
e2 = Entry(container2, width = 50, relief="groove", font="Times 14").place(x = 120, y = 95)
 

#Creating Labels and setting the properties
label = Label(top, fg="dark blue", text="TIC-TAC-TOE (X's and O's)", font='Calibri 28 bold')
label1 = Label(container, text="Mode of Playing\n", font="Times 16 underline")
label2 = Label(left, text="Left Part")
label3 = Label(right, text="Right Part")
label4 = Label(container2, text="Player Names", font="Times 16 underline")
label5 = Label(container3, text="Which mode of playing?", font='Times 20 bold underline')
label6 = Label(container4, text="Board goes here..")
label7 = Label(container5, text="Player Details..", font="Times 16 underline")

#Displays the borders along with text
top.pack(side="top", expand=False, fill="both")
bottom.pack(side="bottom", expand=True, fill="both")
left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")
container.pack(expand=False, fill="both", padx=5, pady=5)
container2.pack(expand=True, fill="both", padx=5, pady=5)
container3.pack(expand=False, fill="both", padx=5, pady=5)
container4.pack(expand=True, fill="both", padx=5, pady=5)
container5.pack(expand=True, fill="both", padx=5, pady=5)


#Packing Labels
label.pack()
label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()
b1.pack(side="top")
b2.pack(side="bottom")
sep.pack(side="left", fill="y", padx=4, pady=4)

root.mainloop()
