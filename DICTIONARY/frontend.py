from tkinter import *
import backend


def get_word_list():
    list1.delete(0, END)
    for row in backend.word_list(e1_value.get()):
        if row != "":
            list1.insert(END, row.capitalize())


def get_selected_row(event):
    global selected_item
    try:
        index = list1.curselection()[0]
        selected_item = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_item)
        get_meaning()
    except:
        get_meaning()


def get_meaning():
    meaning_str = e1_value.get().capitalize() + "\n"
    i = 1
    meaning = backend.meaning(e1_value.get().lower())
    for sentence in meaning:
        meaning_str = meaning_str + str(i) + ". " + sentence + "\n"
        i = i + 1
    var3.set(meaning_str)


window = Tk()

window.wm_title("Dictionary")

var1 = StringVar()
l1 = Label(window, textvariable=var1, width=30, font='Helvetica 10 bold')
l1.grid(row=0, column=0, columnspan=2)
var1.set("ENTER A WORD ")

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=30)
e1.grid(row=0, column=2, columnspan=2)

b1 = Button(window, text="Search", width=30, command=get_word_list)
b1.grid(row=0, column=4, columnspan=2)

list1 = Listbox(window, height=10, width=50, font='Helvetica 10 bold')
list1.grid(row=1, column=0, rowspan=2, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=1, column=2, rowspan=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

var2 = StringVar()
l2 = Label(window, textvariable=var2, height=2, width=100, font='Helvetica 10 bold')
l2.grid(row=1, column=3, columnspan=3)
var2.set("RESULT")

var3 = StringVar()
l3 = Label(window, textvariable=var3, height=6, width=100, wraplength=500, anchor='nw', justify=LEFT, borderwidth=3,
           relief="groove")
l3.grid(row=2, column=3, columnspan=3)
var3.set("")

get_word_list()
window.mainloop()
