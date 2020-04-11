from tkinter import *
from tkinter import ttk

'''---------------------------------------------------Functions ------------------------------------------------------'''
#Sets the name of the Game Mode as Heading on Top of the Board
def set_mode(btn):
    label5.config(text=btn["text"], fg="indianred")
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    

#Resets everything after every game
def reset():
    pass

#Getting the Players name
def submit():    
    details_1 = "Player1" if p1.get() == "" else p1.get()
    details_2 = "Player2" if p2.get() == "" else p2.get()
    info = '\nPlayer-1 Name: ' + details_1.title() + ' (X)\n\nPlayer-2 Name: ' + details_2.title() + ' (O)'
    label7.config(text=info, font="Times 20 bold", fg="blue")
      

#Checks if the winning conditions are met
def check():
    pass


'''------------------------------------------------ Tkinter User Interface ------------------------------------------'''
root = Tk()
root.title('Tic-Tac-Toe')
root.geometry('1200x680')

#Dividing the Screen into 2 parts
top = Frame(root, borderwidth=1, relief="solid")
bottom = Frame(root, borderwidth=2, relief="solid")
left = Frame(bottom, borderwidth=0, relief="solid")
right = Frame(bottom, borderwidth=0, relief="solid")
container = Frame(left, borderwidth=1, relief="solid")
container2 = Frame(left, borderwidth=0, relief="solid")
container3 = Frame(right, borderwidth=2, relief="solid")
container4 = Frame(right, borderwidth=2, relief="solid")
container5 = Frame(left, borderwidth=1, relief="solid")
container6 = Frame(left, borderwidth=0, relief="solid")

#Separator - To separate the Buttons
sep = ttk.Separator(container)

'''Modes of Playing two Buttons'''
b1 = Button(container, text = "Player vs Player", font="Consolas 16 bold", fg="white", bg="green", activebackground="coral", width="20", relief="groove",
            padx=10, pady=10)
#Calling the set_mode function
b1.configure( command=lambda btn=b1: set_mode(btn))


b2 = Button(container, text="Player vs Computer", font="Consolas 16 bold", fg="white", bg="green", activebackground="coral", width="20", relief="groove",
            padx=10, pady=10)
#Calling the set_mode function
b2.configure( command=lambda btn=b2: set_mode(btn))


#Player Names - User Input Textfields
p1 = StringVar()
p2 = StringVar()

player1 = Label(container2, text = "Player 1: ", font="Times 18").place(x = 30,y = 50)
player2 = Label(container2, text = "Player 2: ", font="Times 18").place(x = 30,y = 90)

e1 = Entry(container2, textvariable=p1, width = 30, relief="groove", font="Times 12").place(x = 120, y = 55)  
e2 = Entry(container2, textvariable=p2, width = 30, relief="groove", font="Times 12").place(x = 120, y = 95)

#Button for Submit
b3 = Button(container2, text = "Submit", font="Consolas 12 bold", fg="white", bg="indigo", activebackground="coral", relief="groove",
            padx=5, pady=5, command=submit)
 

#Button for Reset
b4 = Button(container6, text = "Reset Everything", font="Consolas 15 bold", fg="white", bg="red", activebackground="yellow", relief="groove",
            padx=5, pady=5, command=reset)


#Creating Labels and setting the properties
label = Label(top, fg="dark blue", text="TIC-TAC-TOE (X's and O's)", font='Calibri 28 bold')
label1 = Label(container, text="Mode of Playing\n", font="Times 16 underline")
label2 = Label(left)
label3 = Label(right)
label4 = Label(container2, text="Player Names", font="Times 16 underline")
label5 = Label(container3, text="Please Select mode of playing..", font='Calibri 20 bold underline')
label6 = Label(container4, text="Board goes here..")
label7 = Label(container5, text="Player Details..", font="Times 16 underline")


#Displays the borders along with text
top.pack(side="top", expand=False, fill="both")
bottom.pack(side="bottom", expand=True, fill="both")
left.pack(side="left", expand=False, fill="both")
right.pack(side="right", expand=True, fill="both")
container.pack(expand=False, fill="both", padx=5, pady=5)
container2.pack(expand=True, fill="both", padx=5, pady=5)
container3.pack(expand=False, fill="both", padx=5, pady=5)
container4.pack(expand=True, fill="both", padx=5, pady=5)
container5.pack(expand=False, fill="both", padx=5, pady=5)
container6.pack(expand=False, fill="both", padx=5, pady=5)



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
b3.pack(side="bottom")
b4.pack()
sep.pack(side="left", fill="y", padx=4, pady=4)

#Disables resizing the window
root.resizable(False, False)
root.mainloop()
