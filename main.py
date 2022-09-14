from tkinter import Tk, Button, Grid
import crop

root = Tk()
root.geometry("500x500")

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

button1 = Button(root, text="Crop tudo bicho", command=crop.button_func)
button1.grid(row=0, column=0, sticky="NSEW")

root.mainloop()

