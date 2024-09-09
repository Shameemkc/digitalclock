# password generator.

from tkinter import *
import string, random

screen=Tk()
screen.geometry("300x500")

Title=StringVar()
TitleLabel=Label(screen, textvariable=Title).pack()
Title.set("password generator")

def SelectionOptions():
    Choice.get()
 
Choice= IntVar()
Button1 = Radiobutton(screen,text="POOR",variable=Choice,value=1,command=SelectionOptions).pack(anchor=CENTER)
Button2 = Radiobutton(screen,text="AVERAGE",variable=Choice,value=2,command=SelectionOptions).pack(anchor=CENTER)
Button3 = Radiobutton(screen,text="STRONG",variable=Choice,value=3,command=SelectionOptions).pack(anchor=CENTER)
 
LabelChoice = Label(screen)
LabelChoice.pack()
 
LengthLabel = StringVar()
LengthLabel.set("Password Length")
LengthTitle = Label(screen,textvariable=LengthLabel).pack()

Value = IntVar()
SpinLength = Spinbox(screen, from_=8, to_=25, textvariable = Value, width = 14).pack()

Poor = string.ascii_uppercase+string.ascii_lowercase
Average = string.ascii_uppercase+string.ascii_lowercase+string.digits
Symbols="""~`! @#$%^&*()_-+={[}]|;"'<,>.?/ """
Advance= Poor+Average+Symbols
 
def PassGen():
    if Choice.get()==1:
        return "".join(random.sample(Poor,Value.get()))
    if Choice.get()==2:
        return "".join(random.sample(Average,Value.get()))
    if Choice.get()==3:
        return "".join(random.sample(Advance,Value.get()))

Lsum=Label(screen,text="")
Lsum.pack(side=BOTTOM)
def CallBack():
    Lsum.config(text=PassGen())
Password=str(CallBack())
PassGenButton = Button(screen,text="generate Password",bd=5, height=2 ,command=CallBack,pady=3)
PassGenButton.pack()
 
screen.mainloop()