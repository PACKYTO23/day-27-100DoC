import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label.", font=("Arial", 24, "bold"))  # Label
my_label.pack(side="right")

window.mainloop()
