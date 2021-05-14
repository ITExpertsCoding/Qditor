import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

window = Tk()
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

filepath = ""
filepathh = ""

filedir = ""
#
a = 0


def save_file():
    "Save the current file as a new file."
    global filedir
    global filesaved

    filepath = asksaveasfilename(defaultextension="txt",
                                 filetypes=[("All Files", "*.*"), ("Text Files", ".txt"), ('Python Files', '*.py'),
                                            ('HTML Files', '*.html'), ('JSON Files', '*.json')], )

    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, "end-1c")
        output_file.write(text)
        filesaved = True
    window.title(f" Qditor- {filepath}")
    filedir = filepath

def open_file():
    "Open a file for editing."
    global filea
    pop = messagebox.askyesno("Do you want to save?")
    print(pop)
    filepath = askopenfilename(
        filetypes=[("All Files", "*.*"), ("Text Files", ".txt"), ('Python Files', '*.py'), ('HTML Files', '*.html'),('JSON Files', '*.json')])
    if not filepath:
        return

    txt_edit.delete(1.0, END)
    filea = filepath

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert("end-1c", text)
        window.title(f"Qditor- {filepath}")

    savefilee = False
    if pop == True:
        filepath = askopenfilename(
            filetypes=[("All Files", "*.*"), ("Text Files", ".txt"), ('Python Files', '*.py'),
                           ('HTML Files', '*.html'), ('JSON Files', '*.json')])
        save
        if not filepath:
            return
        txt_edit.delete(1.0, END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert("end-1c", text)
        window.title(f"Simple Text Editor - {filepath}")

def save():
    filepathh = filea
    global filesaved
    with open(filepathh, "w") as output_file:
        text = txt_edit.get(1.0, "end-1c")
        output_file.write(text)
        filesaved = True
        print("fwqcs")
    try:
        path = asksaveasfilename(defaultextension="txt",
                                 filetypes=[("All Files", "*.*"), ("Text Files", ".txt"), ('Python Files', '*.py'),
                                            ('HTML Files', '*.html'), ('JSON Files', '*.json')])
        path.close()
    except FileNotFoundError:
        save_file()
        print("fiwrbsnoe fweatn")

    if filepathh == filepathh + {"/"} or filepathh == "":
        save_file()

def dosomething():
    if txt_edit != "":
        pop = messagebox.askyesno("Question Pop Up", "R   U   S U R E ?")

        if pop == True:
            exit()
        if pop == True:
            save

def clear():
    if txt_edit != "":
        pop = messagebox.askyesno("Question Pop Up", "R   U   S U R E ?")

        if pop == True:
            txt_edit.delete(1.0, "end-1c")

def copy():
    global content
    content = txt_edit.selection_get()

def paste():
    txt_edit.insert(INSERT, content)

def cut():
    global content
    content = txt_edit.selection_get()
    txt_edit.delete("sel.first", "sel.last")

def delete():
    txt_edit.delete("sel.first", "sel.last")

def Convert(string):
    li = list(string.split(" "))
    return li

def openhelp():
    messagebox.askokcancel("help", "Why do you even need help on a text editor?.     V0.01")

openstatus = True

menu = Menu(window)

filmenu = Menu(menu, tearoff=0)

filmenu.add_command(label="Open File", command=open_file)
filmenu.add_command(label="Save As", command=save_file)
filmenu.add_command(label="Save", command=save)
filmenu.add_command(label="New", command=clear)
filmenu.add_separator()
filmenu.add_command(label="Exit", command=dosomething)

filmenu1 = Menu(menu, tearoff=0)

filmenu1.add_command(label="Help", command=openhelp)

menu.add_cascade(label="File", menu=filmenu)
menu.add_cascade(label="Help", menu=filmenu1)

frame1 = Frame(bg="gray")
frame1.pack(fill=BOTH)

global txt_edit

txt_edit = Text(master=frame1, width=100, height=200, bg="#1f1f1f", fg="#ffffff")
txt_edit.pack(side=LEFT, fill=BOTH, expand=YES)

popup = Menu(window, tearoff=0)
popup.add_command(label="Copy", command=copy)  # , command=next) etc...
popup.add_command(label="Paste", command=paste)
popup.add_command(label="Cut", command=cut)
popup.add_separator()
popup.add_command(label="Delete", command=delete)


def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()

window.bind("<Button-3>", do_popup)

window.config(menu=menu)
window.title(" Qditor")
mainloop()



























