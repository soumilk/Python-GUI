from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.head = Label(self, text="Body Mass Index (BMI)")
        self.head.grid(row=0, columnspan=2)

        self.inputH = Label(self, text="Height: (Centimeter)")
        self.inputH.grid(row=1, column=0)

        self.inputW = Label(self, text="Weight: (Kilogram)")
        self.inputW.grid(row=2, column=0)

        self.inputW = Entry(self)
        self.inputW.grid(row=2, column=1)

        self.inputH = Entry(self)
        self.inputH.grid(row=1, column=1)

        self.button = Button(self, text="Calculate", command=self.calc)
        self.button.grid(row=4, columnspan=2)

        self.bmiCal = Label(self, text="BMI:")
        self.bmiCal.grid(row=5, column=0)

        self.cate = Label(self, text="Catagory:")
        self.cate.grid(row=6, column=0)

        self.result = Label(self, bg="#fff", anchor="w", relief="groove")
        self.result.grid(row=5, column=1)

        self.cateName = Label(self, bg="#fff", anchor="w", relief="groove")
        self.cateName.grid(row=6, column=1)

    def calc(self):
        self.height = float(self.inputH.get())
        self.weight = float(self.inputW.get())
        self.bmi = (self.weight / (self.height ** 2)) * 703
        self.bmi = round(self.bmi, 2)
        self.result["text"] = self.bmi
        if self.bmi > 18.5:
            if self.bmi > 24.9:
                if self.bmi > 25:
                    if self.bmi > 30:
                        self.cateName["text"] = "Obese"
                else:
                    self.cateName["text"] = "Overweight"
            else:
                self.cateName["text"] = "Normal"
        else:
            self.cateName["text"] = "Underweight"

def main():
    a = App()
    a.mainloop()

if __name__ == "__main__":
    main()