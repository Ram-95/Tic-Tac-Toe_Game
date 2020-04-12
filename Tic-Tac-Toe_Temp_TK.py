from tkinter import *
import random
from tkinter import messagebox
from tkinter import ttk

'''---------------------------------------------------Functions ------------------------------------------------------'''
#Sets the name of the Game Mode as Heading on Top of the Board
def player_vs_player():
    pass


def computer_vs_player():
    pass


def set_mode(btn):
    label5.config(text=btn["text"], fg="indianred")
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    
def button(frame):          
    b=Button(frame,padx=1,bg="white",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b

#Resets everything after every game
def reset():
    #Resetting the Buttons
    button1.config(text="", state=NORMAL)
    button2.config(text="", state=NORMAL)
    button3.config(text="", state=NORMAL)
    button4.config(text="", state=NORMAL)
    button5.config(text="", state=NORMAL)
    button6.config(text="", state=NORMAL)
    button7.config(text="", state=NORMAL)
    button8.config(text="", state=NORMAL)
    button9.config(text="", state=NORMAL)

    #Setting the Mode of playing buttons
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    

#Getting the Players name
def submit():
    global details_1
    global details_2
    details_1 = "Player1" if p1.get() == "" else p1.get()
    details_2 = "Player2" if p2.get() == "" else p2.get()
    info = '\nPlayer-1 Name: ' + details_1[:10].title() + ' (O)\n\nPlayer-2 Name: ' + details_2[:10].title() + ' (X)'
    label8.config(text=info, font="Times 16 bold", fg="blue")
      
#Horizontal Check
def horizontal():
    if((button1["text"] == button2["text"] == button3["text"] and button1["text"] != "") or
       (button4["text"] == button5["text"] == button6["text"] and button4["text"] != "") or
       (button7["text"] == button8["text"] == button9["text"] and button7["text"] != "")):
        return True
    else:
        return False

#Vertical Check
def vertical():
    if((button1["text"] == button4["text"] == button7["text"] and button1["text"] != "") or
       (button2["text"] == button5["text"] == button8["text"] and button2["text"] != "") or
       (button3["text"] == button6["text"] == button9["text"] and button3["text"] != "")):
        return True
    else:
        return False

#Diagonal Check
def diagonal():
    if((button1["text"] == button5["text"] == button9["text"] and button1["text"] != "") or
       (button7["text"] == button5["text"] == button3["text"] and button7["text"] != "")):
        return True
    else:
        return False

#Code for checking if match is tied
def draw():
    if(button1["state"] == button2["state"] == button3["state"] == button4["state"] ==
       button5["state"] == button6["state"] == button7["state"] == button8["state"] ==
       button9["state"]):
        return True
    return False

#Checks if the winning conditions are met
def check():
    if horizontal() or vertical() or diagonal():
        messagebox.showinfo("GAME OVER","Somebody Won the Match")
        reset()
    elif draw():
        messagebox.showinfo("GAME DRAW","Match is Tied")
        reset()
        

#Function to execute when button is clicked
def click(row,col,button):
    global flag
    button.config(text=a[flag],state=DISABLED,disabledforeground=colour[a[flag]])
    chance = details_1[:10].title() + "(O)'s Chance" if flag == 1 else details_2[:10].title() + "(X)'s Chance"
    end_label.config(text=chance)
    flag = 0 if flag == 1 else 1
    check()

'''------------------------------------------------ Tkinter User Interface ------------------------------------------'''
root = Tk()
root.title('Tic-Tac-Toe Game')
root.geometry('850x700')

#Dividing the Screen into 2 parts
top = Frame(root, borderwidth=1, relief="sunken")
bottom = Frame(root, borderwidth=0, relief="sunken")
left = Frame(bottom, borderwidth=0, relief="sunken")
right = Frame(bottom, borderwidth=0, relief="sunken")
container = Frame(left, borderwidth=0, relief="sunken")
container2 = Frame(left, borderwidth=0, relief="sunken")
container3 = Frame(right, borderwidth=0, relief="sunken")
container4 = Frame(right, borderwidth=0, relief="sunken")
container5 = Frame(left, borderwidth=0, relief="sunken")
container7 = Frame(left, borderwidth=0, relief="sunken")
container6 = Frame(left, borderwidth=0, relief="sunken")


#Creating Labels and setting the properties
label = Label(top, fg="dark blue", text="TIC-TAC-TOE (X's and O's)", font='Calibri 28 bold')
label1 = Label(container, text="Mode of Playing\n", font="Times 16 underline")
label2 = Label(left)
label3 = Label(right)
label4 = Label(container2, text="Player Names", font="Times 16 underline")
label5 = Label(container3, text="Please Select Playing Mode", font='Calibri 20 bold underline')
label6 = Label(container4, height="800", width="800")
label7 = Label(container5, text="Player Details", font="Times 16 underline")
label8 = Label(container5, font="Times 16 bold", fg="blue")
label8.config(text="\nPlayer-1 (X) \n\nPlayer-2 (O)")

#Displays the borders along with text
top.pack(side="top", expand=False, fill="both")
bottom.pack(side="bottom", expand=True, fill="both")
left.pack(side="left", expand=True, fill="both", padx= 5, pady=5)
right.pack(side="right", expand=True, fill="both", padx= 5, pady=5)
container.pack(expand=False, fill="both", padx=5, pady=5)
container2.pack(expand=True, fill="both", padx=5, pady=5)
container3.pack(expand=False, fill="both", padx=5, pady=5)
container4.pack(expand=True, fill="both", padx=5, pady=5)
container5.pack(expand=False, fill="both", padx=5, pady=5)
container6.pack(expand=False, fill="both", padx=5, pady=5)
container7.pack(expand=False, fill="both", padx=5, pady=5)


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

e1 = Entry(container2, textvariable=p1, width = 50, relief="groove", font="Times 12").place(x = 120, y = 55)  
e2 = Entry(container2, textvariable=p2, width = 50, relief="groove", font="Times 12").place(x = 120, y = 95)

#Button for Submit
b3 = Button(container2, text = "Submit", font="Consolas 12 bold", fg="white", bg="indigo", activebackground="coral", relief="groove",
            padx=5, pady=5, command=submit)
 

#Button for Reset
b4 = Button(container6, text = "Reset Everything", font="Consolas 15 bold", fg="white", bg="red", activebackground="yellow", relief="groove",
            padx=5, pady=5, command=reset)


'''------------------------------------------------- TIC-TAC-TOE Board ------------------------------------------------ '''

button1=Button(container4, bg="white",width=3,font=('arial',60,'bold'),relief="sunken",bd=10, command=lambda row=1,col=1:click(row,col,button1))
button1.grid(row=1,column=1)

button2=Button(container4,bg="white",width=3,font=('arial',60,'bold'),relief="sunken",bd=10, command=lambda row=1,col=2:click(row,col,button2))
button2.grid(row=1,column=2)

button3=Button(container4, bg="white",width=3,font=('arial',60,'bold'),relief="sunken",bd=10, command=lambda row=1,col=3:click(row,col,button3))
button3.grid(row=1,column=3)

button4=Button(container4,  bg="white",width=3,font=('arial',60,'bold'),relief="sunken",bd=10, command=lambda row=2,col=1:click(row,col,button4))
button4.grid(row=2,column=1)

button5=Button(container4, bg="white",width=3,font=('arial',60,'bold'),relief="sunken",bd=10, command=lambda row=2,col=2:click(row,col,button5))
button5.grid(row=2,column=2)

button6=Button(container4, bg="white",width=3,font=('arial',60,'bold'),relief="sunken",bd=10, command=lambda row=2,col=3:click(row,col,button6))
button6.grid(row=2,column=3)

button7=Button(container4, bg="white",width=3,font=('arial',60,'bold'),relief="sunken",bd=10,
               command=lambda row=3,col=1:click(row,col,button7))
button7.grid(row=3,column=1)

button8=Button(container4, bg="white",width=3,font=('arial',60,'bold'),relief="sunken",bd=10,
               command=lambda row=3,col=2:click(row,col,button8))
button8.grid(row=3,column=2)

button9=Button(container4, bg="white",width=3,font=('arial',60,'bold'),relief="sunken",bd=10,
               command=lambda row=3,col=3:click(row,col,button9))
button9.grid(row=3,column=3)

#Below board that shows the players' turns
end_label=Label(container4, text="(O)'s Chance",font=('arial',20,'bold'))
end_label.grid(row=4,column=0,columnspan=5)

'''-------------------------------------------------------- END of TIC TAC TOE Board --------------------------------------------------- '''

#Packing Labels
label.pack()
label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
#label6.pack()
label7.pack()
label8.pack()
b1.pack(side="top")
b2.pack(side="bottom")
b3.pack(side="bottom")
b4.pack(side="top")
sep.pack(side="left", fill="y", padx=4, pady=4)

#Flag to change between the players - 0 -> 1st Player 1-> 2nd Player
global flag
flag = 0
details_1 = ''
details_2 = ''

a = ['O','X']
colour={'O':"red",'X':"lawn green"}


#Disables resizing the window
root.resizable(False, False)
root.mainloop()
