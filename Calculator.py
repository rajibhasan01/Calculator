import tkinter
from tkinter import *


def click(event):
    global data
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if data.get().isdigit():
            value = int(data.get())
        else:
            try:

                value = eval(lbl.get())

            except Exception as e:

                value = "Error"
                print(e)
        data.set(value)
        lbl.update()

    elif text == "C":
        data.set("")
        lbl.update()
    else:
        data.set(data.get() + text)
        lbl.update()



root = Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")
root.iconbitmap(r'calculator.ico')

data = StringVar()
data.set("")

lbl = Entry(
    root,

    font = ("Verdana",20),
    textvar = data,
    bg = "#ffffff",
    fg = "#000000"

)
lbl.pack(expand = True, fill = BOTH)

btnrow1 = Frame(
    root,
    bg = "#000000"
    )
btnrow1.pack(expand = True, fill = "both")


btnrow2 = Frame(
    root,
    bg = "#ffffff",
)
btnrow2.pack(expand = True, fill = BOTH)

btnrow3 = Frame(
    root,
    bg = "#ffffff",
)
btnrow3.pack(expand = True, fill = BOTH)

btnrow4 = Frame(
    root,
    bg = "#ffffff",
)
btnrow4.pack(expand = True, fill = BOTH)

btn7 = Button(
    btnrow1,
    text = "7",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btn7.pack(side = LEFT, expand = True, fill = BOTH)
btn7.bind("<Button-1>", click)


btn8 = Button(
    btnrow1,
    text = "8",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0


)
btn8.pack(side = LEFT, expand = True, fill = BOTH)
btn8.bind("<Button-1>", click)

btn9 = Button(
    btnrow1,
    text = "9",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btn9.pack(side = LEFT, expand = True, fill = BOTH)
btn9.bind("<Button-1>", click)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btnplus.pack(side = LEFT, expand = True, fill = BOTH)
btnplus.bind("<Button-1>", click)


btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btn4.pack(side = LEFT, expand = True, fill = BOTH)
btn4.bind("<Button-1>", click)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btn5.pack(side = LEFT, expand = True, fill = BOTH)
btn5.bind("<Button-1>", click)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btn6.pack(side = LEFT, expand = True, fill = BOTH)
btn6.bind("<Button-1>", click)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btnminus.pack(side = LEFT, expand = True, fill = BOTH)
btnminus.bind("<Button-1>", click)


btn1 = Button(
    btnrow3,
    text = "1",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0,

)
btn1.pack(side = LEFT, expand = True, fill = BOTH)
btn1.bind("<Button-1>", click)

btn2 = Button(
    btnrow3,
    text = "2",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0,

)
btn2.pack(side = LEFT, expand = True, fill = BOTH)
btn2.bind("<Button-1>", click)

btn3 = Button(
    btnrow3,
    text = "3",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btn3.pack(side = LEFT, expand = True, fill = BOTH)
btn3.bind("<Button-1>", click)

btnmultiply = Button(
    btnrow3,
    text = "*",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btnmultiply.pack(side = LEFT, expand = True, fill = BOTH)
btnmultiply.bind("<Button-1>", click)


btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btnc.pack(side = LEFT, expand = True, fill = BOTH)
btnc.bind("<Button-1>", click)


btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btn0.pack(side = LEFT, expand = True, fill = BOTH)
btn0.bind("<Button-1>", click)


btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btnequal.pack(side = LEFT, expand = True, fill = BOTH)
btnequal.bind("<Button-1>", click)


btndivided = Button(
    btnrow4,
    text = "/",
    font = ("Verdana",22),
    relief = GROOVE,
    border = 0

)
btndivided.pack(side = LEFT, expand = True, fill = BOTH)
btndivided.bind("<Button-1>", click)


#----------------Hover Function---------------
def entered1(event):
    btn1.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left1(event):
    btn1.config(
        fg="#000000",
        bg="gray93"
    )

def entered2(event):
    btn2.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left2(event):
    btn2.config(
        fg="#000000",
        bg="gray93"
    )

def entered3(event):
    btn3.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left3(event):
    btn3.config(
        fg="#000000",
        bg="gray93"
    )

def entered4(event):
    btn4.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left4(event):
    btn4.config(
        fg="#000000",
        bg="gray93"
    )


def entered5(event):
    btn5.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left5(event):
    btn5.config(
        fg="#000000",
        bg="gray93"
    )

def entered6(event):
    btn6.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left6(event):
    btn6.config(
        fg="#000000",
        bg="gray93"
    )

def entered7(event):
    btn7.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left7(event):
    btn7.config(
        fg="#000000",
        bg="gray93"
    )

def entered8(event):
    btn8.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left8(event):
    btn8.config(
        fg="#000000",
        bg="gray93"
    )

def entered9(event):
    btn9.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left9(event):
    btn9.config(
        fg="#000000",
        bg="gray93"
    )

def enteredplus(event):
    btnplus.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def leftplus(event):
    btnplus.config(
        fg="#000000",
        bg="gray93"
    )

def enteredminus(event):
    btnminus.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def leftminus(event):
    btnminus.config(
        fg="#000000",
        bg="gray93"
    )

def enteredmultiply(event):
    btnmultiply.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def leftmultiply(event):
    btnmultiply.config(
        fg="#000000",
        bg="gray93"
    )

def enteredc(event):
    btnc.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def leftc(event):
    btnc.config(
        fg="#000000",
        bg="gray93"
    )

def entered0(event):
    btn0.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def left0(event):
    btn0.config(
        fg="#000000",
        bg="gray93"
    )

def entereddivided(event):
    btndivided.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def leftdivided(event):
    btndivided.config(
        fg="#000000",
        bg="gray93"
    )

def enteredequal(event):
    btnequal.config(
        bg = "#343434",
        fg = "#ffffff"
    )

def leftequal(event):
    btnequal.config(
        fg="#000000",
        bg="gray93"
    )

#--------------------Blind-----------------
btn0.bind("<Enter>", entered0)
btn0.bind("<Leave>", left0)

btn1.bind("<Enter>", entered1)
btn1.bind("<Leave>", left1)

btn2.bind("<Enter>", entered2)
btn2.bind("<Leave>", left2)

btn3.bind("<Enter>", entered3)
btn3.bind("<Leave>", left3)

btn4.bind("<Enter>", entered4)
btn4.bind("<Leave>", left4)

btn5.bind("<Enter>", entered5)
btn5.bind("<Leave>", left5)

btn6.bind("<Enter>", entered6)
btn6.bind("<Leave>", left6)

btn7.bind("<Enter>", entered7)
btn7.bind("<Leave>", left7)

btn8.bind("<Enter>", entered8)
btn8.bind("<Leave>", left8)

btn9.bind("<Enter>", entered9)
btn9.bind("<Leave>", left9)

btnc.bind("<Enter>", enteredc)
btnc.bind("<Leave>", leftc)

btnplus.bind("<Enter>", enteredplus)
btnplus.bind("<Leave>", leftplus)

btnminus.bind("<Enter>", enteredminus)
btnminus.bind("<Leave>", leftminus)

btnequal.bind("<Enter>", enteredequal)
btnequal.bind("<Leave>", leftequal)

btnmultiply.bind("<Enter>", enteredmultiply)
btnmultiply.bind("<Leave>", leftmultiply)

btndivided.bind("<Enter>", entereddivided)
btndivided.bind("<Leave>", leftdivided)


root.mainloop()
