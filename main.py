from tkinter import *

FONT = ("Helvetica", 15, "normal")

# def button_clicked():
#     # print("I got clicked")
#     new_text = my_entry.get()
#     my_label.config(text=new_text)


# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)

# my_label = Label(text="I am a Label.", font=("Arial", 24, "bold"))  # Label
# my_label.config(text="New Text")
# # my_label["text"] = "New Text"
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# my_button = Button(text="Click Me", command=button_clicked)  # Button
# my_button.grid(column=1, row=1)

# my_button_2 = Button(text="Click Me 2", command=button_clicked)
# my_button_2.grid(column=2, row=0)

# my_entry = Entry(width=10)  # Entry
# my_entry.grid(column=3, row=2)

# window.mainloop()


def miles_to_km():
    miles = float(miles_entry.get())
    km = "{:.3f}".format(miles * 1.609)
    result_label.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=30)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)

miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
