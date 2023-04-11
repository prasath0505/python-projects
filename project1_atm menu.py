from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import random
window = Tk()
window.geometry("360x360")
window.title("Banking App")
window.bg=PhotoImage("D:\bank2.png")
pin_label = Label(window, text="Enter PIN:",bg='SlateGray3')
pin_label.pack()
pin_entry = Entry(window, show="*")
pin_entry.pack()

amount_label = Label(window, text="Enter Amount:",bg='SlateGray3')
amount_label.pack()
amount_entry = Entry(window)
amount_entry.pack()

transaction_label = Label(window, text="Select Option:",bg='SlateGray3')
transaction_label.pack()
transaction_var = StringVar()
transaction_option = OptionMenu(window, transaction_var, "Deposit", "Withdraw","Check Balance")
transaction_option.pack()
def deposit():
    pin = pin_entry.get()
    amount = int(amount_entry.get())
    transaction_id = random.randint(10000, 99999)
    balance[pin] += amount
    messagebox.showinfo("Deposit Successful", f"Transaction ID: {transaction_id}\nAmount Deposited: {amount}\nNew Balance: {balance[pin]}\nThanks for banking with us❤")
balance = {"1234": 0, "2001": 0, "2022": 0}  
def withdraw():
    pin = pin_entry.get()
    amount = int(amount_entry.get())
    if amount > balance[pin]:
        messagebox.showerror("Withdraw Error", "Insufficient Balance")
    else:
        transaction_id = random.randint(10000, 99999)
        balance[pin] -= amount
        messagebox.showinfo("Withdraw Successful", f"Transaction ID: {transaction_id}\nAmount Withdrawn: {amount}\nNew Balance: {balance[pin]}")
balance = {"1234": 0, "2001": 0, "2022": 0}
def balance_check():
    pin = pin_entry.get()
    messagebox.showinfo("balance",f"Your balance is: Rs.{balance[pin]}")
balance = {"1234": 0, "2001": 0, "2022": 0}
def check_pin():
    pin = pin_entry.get()
    if pin in balance:
        if transaction_var.get() == "Deposit":
            deposit()
        elif transaction_var.get() == "Withdraw":
            withdraw()
        else:
            balance_check()
    else:
        messagebox.showerror("PIN Error", "Invalid PIN")
button = Button(window, text="OK", command=check_pin,bg='DarkSeaGreen3')
button.pack()
window.mainloop()
