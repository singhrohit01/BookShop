from tkinter import *
from backend import Database1


database=Database1()

def get_selected_row(event):
    try:
        global selected_tuple
        
        index=list1.curselection()[0]

        selected_tuple=list1.get(index)


        Entry1.delete(0,END)
        Entry1.insert(END,selected_tuple[1])

        Entry2.delete(0,END)
        Entry2.insert(END,selected_tuple[2])

        Entry3.delete(0,END)
        Entry3.insert(END,selected_tuple[3])

        Entry4.delete(0,END)
        Entry4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()))


def delete_command():
    database.delete(selected_tuple[0])


def update_command():
    database.update(selected_tuple[0],Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())

window=Tk()

window.wm_title("BookStore")

#This is the code for labels for title, author ,year and isbn

l1=Label(window,text="Title")
l1.grid(row=0,column=0)


l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

#These entry code shows all the entries where the book will be entered 

Title_text=StringVar()
Entry1=Entry(window,textvariable=Title_text)
Entry1.grid(row=0,column=1)


Author_text=StringVar()
Entry2=Entry(window,textvariable=Author_text)
Entry2.grid(row=0,column=3)

Year_text=StringVar()
Entry3=Entry(window,textvariable=Year_text)
Entry3.grid(row=1,column=1)


ISBN_text=StringVar()
Entry4=Entry(window,textvariable=ISBN_text)
Entry4.grid(row=1,column=3)

#Here is the code for listbox, which will show all the entries list in our database app

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

#This is the code for ScrollBar

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

#Here we will configure the buttons

Button1=Button(window,text="View All",width=12,command=view_command)
Button1.grid(row=2,column=3)


Button2=Button(window,text="Search Entry",width=12,command=search_command)
Button2.grid(row=3,column=3)


Button3=Button(window,text="Add Entry",width=12,command=add_command)
Button3.grid(row=4,column=3)


Button4=Button(window,text="Update Selected",width=12,command=update_command)
Button4.grid(row=5,column=3)


Button5=Button(window,text="Delete Selected",width=12,command=delete_command)
Button5.grid(row=6,column=3)


Button6=Button(window,text="Close",width=12,command=window.destroy)
Button6.grid(row=7,column=3)


window.mainloop()