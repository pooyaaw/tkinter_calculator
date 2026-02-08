from tkinter import *

root = Tk()
# changes then name of the program that is written on top of the window
root.title("Pouyas Rechner")

e = Entry(root, width=35, borderwidth=5) 
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
# columnspan 3 because underneath the Entry is going to be three columns and the entry should span over all of them

current = " "


def button_click(x):

    global current
    e.insert(END, x)
    current = str(e.get())  
    # print(f"{e.get()}current = {current}")
    
    
def button_clear_func():
    global fnum 
    fnum = 0
    e.delete(0,END)


fnum = 0

def button_plus_func():
    # so this needs to remember (state) not do the whole equal thing. when you press it it stores the first number and e.delete s
    first_number = e.get()
    global fnum 
    if first_number == "":
        pass
    else: 
        fnum += int(first_number)
    print(f"fnum= {fnum}") #log , delete later
    e.delete(0, END)

def button_equal_func():
    second_number = e.get()
    global fnum 
    fnum += int(second_number)
    second_number = ""
    e.delete(0,END)
    e.insert(0, str(fnum))   # insert result as string
    fnum = 0
    print(f"fnum= {fnum}") #log , delete later


# defining buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)) 
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_clear = Button(root, text="C", padx=40, pady=20, command= button_clear_func) # here I can omit lambda because I don't need to pass anything. 
button_plus = Button(root, text="+", padx=40, pady=20, command= button_plus_func)
button_equal = Button(root, text="=", padx=40, pady=20, command= button_equal_func)
# when we pass stuff into these buttons it has to be through a lambda function

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
