from tkinter import *


def calculate_km():
    miles_ = int(miles.get())
    new_km = round(miles_ * 1.609)
    ans_label.config(text=new_km)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# user's input
miles = Entry(width=10)
miles.insert(END, string='0')
miles.grid(column=1, row=0)

# miles label
miles_label = Label(text="Miles", font=("Calibri", 12, "bold"))
miles_label.grid(column=2, row=0)

# is equal label
is_equal_label = Label(text="is equal to", font=("Calibri", 12, "bold"))
is_equal_label.grid(column=0, row=1)

# answer label
ans_label = Label(text="0", font=("Calibri", 12, "bold"))
ans_label.grid(column=1, row=1)

# km label
km_label = Label(text="Km", font=("Calibri", 12, "bold"))
km_label.grid(column=2, row=1)

# calculate button
calculate = Button(text="Calculate", command=calculate_km)
calculate.grid(column=1, row=3)


window.mainloop()
