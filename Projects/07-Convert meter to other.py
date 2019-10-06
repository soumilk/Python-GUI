from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.head = Label(self, text="Convert meter to other.")
        self.head.grid(row=0, columnspan=5)

        self.inputMeter = Label(self, text="Meter:")
        self.inputMeter.grid(row=1, columnspan=5)

        self.inputMeter = Entry(self)
        self.inputMeter.grid(row=2, columnspan=5)

        self.convert = Label(self, text="Convert to:")
        self.convert.grid(row=4, column=0)

        self.feetButton = Button(self, text="Feet", command=self.calFeet)
        self.feetButton.grid(row=4, column=1)

        self.inchButton = Button(self, text="Inch", command=self.calInch)
        self.inchButton.grid(row=4, column=2)

        self.mileButton = Button(self, text="Mile", command=self.calMile)
        self.mileButton.grid(row=4, column=3)

        self.mileButton = Button(self, text="Yard", command=self.calYard)
        self.mileButton.grid(row=4, column=4)

        self.cal = Label(self, text="Result:")
        self.cal.grid(row=5, columnspan=5)

        self.result = Label(self, bg="#fff", anchor="w", relief="groove")
        self.result.grid(row=6, columnspan=5)

    def calFeet(self):
        self.meter = float(self.inputMeter.get())
        self.conToFeet = self.meter * 3.2808399
        self.result["text"] = self.conToFeet

    def calInch(self):
        self.meter = float(self.inputMeter.get())
        self.conToInch = self.meter * 39.3700787
        self.result["text"] = self.conToInch

    def calMile(self):
        self.meter = float(self.inputMeter.get())
        self.conToMile = self.meter * 0.000621371192
        self.result["text"] = self.conToMile

    def calYard(self):
        self.meter = float(self.inputMeter.get())
        self.conToYard = self.meter * 1.0936133
        self.result["text"] = self.conToYard

def main():
        a = App()
        a.mainloop()

if __name__ == "__main__":
        main()