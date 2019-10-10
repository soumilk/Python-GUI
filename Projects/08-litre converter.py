from tkinter import *

root = Tk()
root.resizable(0, 0)
root.configure(background='light green')
#function calculate
def calCubicMetre():
    litre = float(inputLitre.get())
    conToCubicMetre = litre * 0.001
    result["text"] = "%.3f" % conToCubicMetre

def calCubicCentimetre():
    litre = float(inputLitre.get())
    conToCubicCentimetre = litre * 1000
    result["text"] = "%.3f" % conToCubicCentimetre

def calCubicFoot():
    litre = float(inputLitre.get())
    conToCubicFoot = litre * 0.03531467
    result["text"] = "%.3f" % conToCubicFoot

def calCubicInch():
    litre = float(inputLitre.get())
    conToCubicInch = litre * 1.0936133
    result["text"] = "%.3f" % conToCubicInch
#Header
head = Label(root, text="Convert Litre to another unit", font=("Verdana", 25, "bold"), fg="black", bg="light green")
head.grid(row=0, columnspan=5, pady=15, padx=15)
#Input litre
inputLitre = Label(root, text="Litre:", font=("Calisto MT", 23), fg="red", bg="light green")
inputLitre.grid(row=1, columnspan=5)

inputLitre = Entry(root, font=("Verdana", 20), fg="yellow", bg="green", justify='center')
inputLitre.grid(row=2, columnspan=5, pady=10)

#Button to calculate to unit that you press
MetreButton = Button(root, text="CubicMetre", command=calCubicMetre, font=("Verdana", 20), fg="white", bg="purple")
MetreButton.grid(row=5, column=2, pady=10)

CentimetreButton = Button(root, text="CubicCentimetre", command=calCubicCentimetre, font=("Verdana", 20), fg="white", bg="purple")
CentimetreButton.grid(row=4, column=2)

FootButton = Button(root, text="CubicFoot", command=calCubicFoot, font=("Verdana", 20), fg="white", bg="purple")
FootButton.grid(row=4, column=3)

InchButton = Button(root, text="CubicInch", command=calCubicInch, font=("Verdana", 20), fg="white", bg="purple")
InchButton.grid(row=5, column=3)
#Calculate result
cal = Label(root, text="Result:", font=("Verdana", 20), fg="purple", bg="light green")
cal.grid(row=7, columnspan=5)

result = Label(root, bg="blue", anchor="w", relief="groove", font=("Verdana", 20), fg="yellow")
result.grid(row=8, columnspan=5, pady=10)

root.mainloop()
