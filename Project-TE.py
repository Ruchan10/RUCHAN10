from tkinter import *
from tkinter import filedialog
from tkinter import font

win = Tk()
win.title('Notepad')
win.iconbitmap('eagle.png')
win.geometry("1200x660")

# Create main frame
frame0 = Frame(win)
frame0.pack(pady=5)

# Create scroll bar
text_scroll = Scrollbar(frame0)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
text0 = Text(frame0, width=98, height=26, font=("helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
text0.pack()

# Configure scrollbar
text_scroll.config(command=text0.yview)

# CreateMenu
menu0 = Menu(win)
win.config(menu=menu0)

# Add file menu
file_menu = Menu(menu0, tearoff=False)
menu0.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.quit)

# Add edit
edit_menu = Menu(menu0, tearoff=False)
menu0.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add status bar
status_bar = Label(win, text="Ready", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


win.mainloop()