from tkinter import *

root = Tk()
rootTitle = "Body Mass Index"
root.resizable(False, False) #To make it non resizable
root.configure(background='black')

def cal(): #function calcalate BMI
    height = float(inputH.get())
    weight = float(inputW.get())
    bmi = weight / ((height / 100) ** 2)
    outResult["text"] = "%.3f" % bmi
    if bmi > 18.5:
        if bmi > 24.9:
            if bmi > 25:
                if bmi > 30:
                    outCate["text"] = "Obese"
            else:
                outCate["text"] = "Overweight"
        else:
            outCate["text"] = "Normal"
    else:
        outCate["text"] = "Underweight"
#Header
head = Label(root, text="Body Mass Index", font=("Verdana", 25, "bold"), fg="yellow", bg="black")
head.grid(row=0, columnspan=2, ipady=15)
#Input height and weight
inputH = Label(root, text="Height: (Cm.)", font=("Verdana", 20), fg="yellow", bg="black")
inputH.grid(row=1)
inputW = Label(root, text="Weight: (Kg.)", font=("Verdana", 20), fg="yellow", bg="black")
inputW.grid(row=2, ipady=10)

inputH = Entry(root, font=("Verdana", 20))
inputH.grid(row=1, column=1)
inputW = Entry(root, font=("Verdana", 20))
inputW.grid(row=2, column=1)
#Button for calculate
calca = Button(root, text="Calculate", command=cal, font=("Verdana", 20), bg="orange")
calca.grid(row=3, columnspan=2)
#BMI and catagory result
result = Label(root, text="BMI:", font=("Verdana", 20), fg="yellow", bg="black")
result.grid(row=4, ipady=10)
cate = Label(root, text="Category:", font=("Verdana", 20), fg="yellow", bg="black")
cate.grid(row=5)

outResult = Label(root, bg="#fff", anchor="w", relief="groove", font=("Verdana", 20))
outResult.grid(row=4, column=1)
outCate = Label(root, bg="#fff", anchor="w", relief="groove", font=("Verdana", 20))
outCate.grid(row=5, column=1)

root.mainloop()