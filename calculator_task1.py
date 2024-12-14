import tkinter as tk
from tkinter import messagebox

def calculator():
    def del_entry():
        ent.delete(0, 'end')

    def dsp(x):
        data = ent.get()
        nd = data + str(x)
        exp.set(nd)

    def cal():
        try:
            result = eval(ent.get())
            exp.set(result)
        except:
            exp.set("Error")
            messagebox.showerror("Error", "Invalid Input")

    t = tk.Tk()
    t.title("Calculator")
    t.geometry("400x600")
    t.configure(bg="#f5f5f5")

    exp = tk.StringVar()
    exp.set('')

    ent = tk.Entry(t, textvariable=exp, font=("Arial", 24, "bold"), bd=10, insertwidth=4, width=14, borderwidth=4, justify="right")
    ent.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

    button_frame = tk.Frame(t)
    button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '+']
    ]

    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            button_text = buttons[i][j]
            if button_text == '=':
                btn = tk.Button(button_frame, text=button_text, padx=20, pady=20, font=("Arial", 18),
                                bg="#4CAF50", fg="white", command=cal)
            else:
                btn = tk.Button(button_frame, text=button_text, padx=20, pady=20, font=("Arial", 18),
                                bg="#8D8D8D", fg="white", command=lambda x=button_text: dsp(x))
            btn.grid(row=i, column=j, padx=5, pady=5)

    clear_button = tk.Button(t, text="C", padx=20, pady=20, font=("Arial", 18, "bold"), bg="#f44336", fg="white", width=14, command=del_entry)
    clear_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    t.mainloop()

# Run the calculator function
if__name__=="__main__":
    calculator()
