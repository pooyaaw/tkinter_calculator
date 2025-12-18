from tkinter import *

root = Tk()
# changes then name of the program that is written on top of the window
root.title("basic calculator")

e = Entry(root, width=35, borderwidth=5)

e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
# columnspan 3 because underneath the Entry is going to be three columns and the entry should span over all of them


def button_click():
    return

# defining buttons


button_1 = Button(root, text="1", padx=40, pady=20, command=button_click)
button_2 = Button(root, text="2", padx=40, pady=20, command=button_click)
button_3 = Button(root, text="3", padx=40, pady=20, command=button_click)
button_4 = Button(root, text="4", padx=40, pady=20, command=button_click)
button_5 = Button(root, text="5", padx=40, pady=20, command=button_click)
button_6 = Button(root, text="6", padx=40, pady=20, command=button_click)
button_7 = Button(root, text="7", padx=40, pady=20, command=button_click)
button_8 = Button(root, text="8", padx=40, pady=20, command=button_click)
button_9 = Button(root, text="9", padx=40, pady=20, command=button_click)
button_0 = Button(root, text="0", padx=40, pady=20, command=button_click)
button_clear = Button(root, text="C", padx=40, pady=20, command=button_click)
button_plus = Button(root, text="+", padx=40, pady=20, command=button_click)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_click)

# putting buttons on the screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)
button_clear.grid(row=1, column=2)
button_equal.grid(row=5, column=2)
button_plus.grid(row=5, column=0)

root.mainloop()
