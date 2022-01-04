from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=30)


# Calculation
def calculate():
    miles = float(inp.get())
    km = 1.60934 * miles
    km_result_label.config(text=km)
    return


# Label 1
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=2)

# Label 2
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)
miles_label.config(padx=15)

# Label 3
km_label = Label(text="Km")
km_label.grid(column=3, row=2)

# Label 4
km_result_label = Label(text=0)
km_result_label.grid(column=2, row=2)
km_result_label.config(pady=20)

# Button
button = Button(text="calculate", command=calculate)
button.grid(column=2, row=3)

# Entry
inp = Entry()
inp.grid(column=2, row=1)
inp.insert(END, string="0")

window.mainloop()
