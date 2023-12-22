import tkinter as tk
from tkinter import *

def plus():

    num1 = userInput.get()
    num2 = userInput1.get()

    num_p = int(num1) + int(num2)
    output.config(text=num_p)
    
def minus():
    num1 = userInput.get()
    num2 = userInput1.get()

    num_p = int(num1) - int(num2)
    output.config(text=num_p)

def mul():

    num1 = userInput.get()
    num2 = userInput1.get()

    num_p = int(num1) * int(num2)
    output.config(text=num_p)
    
def div():
    num1 = userInput.get()
    num2 = userInput1.get()

    if num2 == "0":
       output.config(text="Divide by zero error")
    else:
        num_p = int(num1) / int(num2)
        output.config(text=num_p)

root  = tk.Tk()

root.geometry("300x300")

# Set the window background color
root.configure(bg="purple")


message = tk.Label(root, text = "Enter Numbers")
message.pack()

output = tk.Label(root, text="")
output.pack()



userInput = tk.Entry(root)
userInput1 = tk.Entry(root)
if userInput1==0:
    msg = tk.Label(root, text = "It is not divisible")
    msg.pack()
userInput.pack()
userInput1.pack()

btn = tk.Button(root, text="+", command=plus)
btn.pack()

btn = tk.Button(root, text="-", command=minus)
btn.pack()

btn = tk.Button(root, text="*", command=mul)
btn.pack()

btn = tk.Button(root, text="/", command=div)
btn.pack()







root.mainloop()
