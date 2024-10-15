import tkinter as tk
from tkinter import messagebox

def add_expense():
    expense_name= entry_name.get()
    expense_amount=entry_amount.get()

    if expense_name== "" or expense_amount =="":
        messagebox.showwarning("input error", "please enter both name and amount,")
        return
    
    try:
        amount= float(expense_amount)
        expenses_list.append((expense_name, amount))
        entry_name.delete(0,tk.END)
        entry_name.delete(0,tk.END)
        update_expenses_display()
    except ValueError:
        messagebox.showwarning("input error","please enter a valid amount.")

def update_expenses_display():
    expenses_display.delete(1.0,tk.END)
    total=0
    for name,amount in expenses_list:
        expenses_display.insert(tk.END,f"{name}:${amount:.2f}\n")
        total+=amount
    expenses_display.insert(tk.END,f"\ntotal expenses: ${total:.2f}")

app=tk.Tk()
app.title("expense tracker")
app.geometry("400x400")
app.configure(bg="red")

expenses_list=[]

tk.Label(app,text="expense name:",bg="orange",font=("helvetica",12)).grid(row=0,column=0,padx=10,pady=10)
entry_name=tk.Entry(app,width=25)
entry_name.grid(row=0,column=1,pady=10)

tk.Label(app,text="amount:",bg="orange",font=("helvetica",12)).grid(row=0,column=0,padx=10,pady=10)
entry_amount=tk.Entry(app,width=25)
entry_amount.grid(row=2,column=1,padx=10,pady=10)

add_botton=tk.Button(app,text="add expense",command=add_expense,bg="black",fg="white",font=("Helvetica",12))
add_botton.grid(row=2,columnspan=1,pady=10)

expenses_display=tk.Text(app,width=40,height=10,padx=5,pady=5,bg="gray",font=("helvetica",12))
expenses_display.grid(row=3,columnspan=2,padx=10,pady=10)

app.mainloop()
