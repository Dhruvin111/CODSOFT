import tkinter as tk
import math

calc = " "

def addcalc(symbol):
    global calc
    calc += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0,calc)

def evalcalc():  
    global calc
    print(calc)
    try:
        calc = str(eval(calc))
        result.delete(1.0, "end")
        result.insert(1.0,calc)
    except:
        clearcalc()
        result.insert(1.0,"ERROR")

def clearcalc():
    global calc
    calc = ""
    result.delete(1.0,"end")
    
def clear_single_number():
    global calc
    calc= calc[:-1]
    result.delete(1.0, "end")
    result.insert(1.0,calc)

def calc_sqrt():
    global calc
    try:
        calc=str(math.sqrt(float(calc)))
        result.delete(1.0, "end")
        result.insert(1.0,calc)
    except ValueError:
        clearcalc()
        result.insert(1.0, "ERROR")

def fact():
    global calc
    try:
        num= int(calc)
        if num<0:
            raise ValueError
        fact=1
        for i in range(1, num+1):
            fact*=i
        calc=str(fact)
        result.delete(1.0, "end")
        result.insert(1.0,calc)
    except ValueError:
        clearcalc()
        result.insert(1.0,"ERROR")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x360")

result = tk.Text(root, height=2, width=20, font=("Times", 28))
result.grid(columnspan=5)

button_1= tk.Button(root, text="C", command=clearcalc, width=5, font=("Times", 16))
button_1.grid(row=2, column=1, padx=5, pady=5)
button_2= tk.Button(root, text="√", command=calc_sqrt, width=5, font=("Times", 16))
button_2.grid(row=2, column=2, padx=5, pady=5)
button_3= tk.Button(root, text="/", command=lambda: addcalc("/"), width=5, font=("Times", 16))
button_3.grid(row=2, column=3, padx=5, pady=5)
button_4= tk.Button(root, text="<-", command=clear_single_number, width=5, font=("Times", 16))
button_4.grid(row=2, column=4, padx=5, pady=5)
button_5= tk.Button(root, text="7", command=lambda: addcalc(7), width=5, font=("Times", 16))
button_5.grid(row=3, column=1, padx=5, pady=5)
button_6= tk.Button(root, text="8", command=lambda: addcalc(8), width=5, font=("Times", 16))
button_6.grid(row=3, column=2, padx=5, pady=5)
button_7= tk.Button(root, text="9", command=lambda: addcalc(9), width=5, font=("Times", 16))
button_7.grid(row=3, column=3, padx=5, pady=5)
button_8= tk.Button(root, text="*", command=lambda: addcalc("*"), width=5, font=("Times", 16))
button_8.grid(row=3, column=4, padx=5, pady=5)
button_9= tk.Button(root, text="4", command=lambda: addcalc(4), width=5, font=("Times", 16))
button_9.grid(row=4, column=1, padx=5, pady=5)
button_10= tk.Button(root, text="5", command=lambda: addcalc(5), width=5, font=("Times", 16))
button_10.grid(row=4, column=2, padx=5, pady=5)
button_11= tk.Button(root, text="6", command=lambda: addcalc(6), width=5, font=("Times", 16))
button_11.grid(row=4, column=3, padx=5, pady=5)
button_12= tk.Button(root, text="-", command=lambda: addcalc("-"), width=5, font=("Times", 16))
button_12.grid(row=4, column=4, padx=5, pady=5)
button_13= tk.Button(root, text="1", command=lambda: addcalc(1), width=5, font=("Times", 16))
button_13.grid(row=5, column=1, padx=5, pady=5)
button_14= tk.Button(root, text="2", command=lambda: addcalc(2), width=5, font=("Times", 16))
button_14.grid(row=5, column=2, padx=5, pady=5)
button_15= tk.Button(root, text="3", command=lambda: addcalc(3), width=5, font=("Times", 16))
button_15.grid(row=5, column=3, padx=5, pady=5)
button_16= tk.Button(root, text="+", command=lambda: addcalc("+"), width=5, font=("Times", 16))
button_16.grid(row=5, column=4, padx=5, pady=5)
button_17= tk.Button(root, text="!", command=fact, width=5, font=("Times", 16))
button_17.grid(row=6, column=1, padx=5, pady=5)
button_18= tk.Button(root, text="0", command=lambda: addcalc(0), width=5, font=("Times", 16))
button_18.grid(row=6, column=2, padx=5, pady=5)
button_19= tk.Button(root, text=".", command=lambda: addcalc("."), width=5, font=("Times", 16))
button_19.grid(row=6, column=3, padx=5, pady=5)
button_20= tk.Button(root, text="=", command=evalcalc, width=5, font=("Times", 16))
button_20.grid(row=6, column=4, padx=5, pady=5)


root.mainloop()