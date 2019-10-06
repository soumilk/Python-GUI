from tkinter import *

root = Tk()
root.resizable(0, 0)
root.configure(background='blue')
#function calculate
def calFeet():
    meter = float(inputMeter.get())
    conToFeet = meter * 3.2808399
    result["text"] = "%.3f" % conToFeet

def calInch():
    meter = float(inputMeter.get())
    conToInch = meter * 39.3700787
    result["text"] = "%.3f" % conToInch

def calMile():
    meter = float(inputMeter.get())
    conToMile = meter * 0.000621371192
    result["text"] = "%.3f" % conToMile

def calYard():
    meter = float(inputMeter.get())
    conToYard = meter * 1.0936133
    result["text"] = "%.3f" % conToYard
#Header
head = Label(root, text="Convert meter to another unit", font=("Verdana", 25, "bold"), fg="yellow", bg="blue")
head.grid(row=0, columnspan=5, pady=15, padx=15)
#Input meter
inputMeter = Label(root, text="Meter:", font=("Verdana", 20), fg="yellow", bg="blue")
inputMeter.grid(row=1, columnspan=5)

inputMeter = Entry(root, font=("Verdana", 20), fg="yellow", bg="blue", justify='center')
inputMeter.grid(row=2, columnspan=5, pady=10)

convert = Label(root, text="Convert to:", font=("Verdana", 20), fg="yellow", bg="blue")
convert.grid(row=4, column=0)
#Button to calculate to unit that you press
feetButton = Button(root, text="Feet", command=calFeet, font=("Verdana", 20), fg="white", bg="purple")
feetButton.grid(row=4, column=1, pady=10)

inchButton = Button(root, text="Inch", command=calInch, font=("Verdana", 20), fg="white", bg="purple")
inchButton.grid(row=4, column=2)

mileButton = Button(root, text="Mile", command=calMile, font=("Verdana", 20), fg="white", bg="purple")
mileButton.grid(row=4, column=3)

mileButton = Button(root, text="Yard", command=calYard, font=("Verdana", 20), fg="white", bg="purple")
mileButton.grid(row=4, column=4)
#Calculate result
cal = Label(root, text="Result:", font=("Verdana", 20), fg="yellow", bg="blue")
cal.grid(row=5, columnspan=5)

result = Label(root, bg="blue", anchor="w", relief="groove", font=("Verdana", 20), fg="yellow")
result.grid(row=6, columnspan=5, pady=10)

root.mainloop()