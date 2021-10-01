from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

win = Tk()
win.title('Notepad')
win.iconbitmap('note.ico')
win.geometry("1200x680")

# Declare variables
global open_status_name
open_status_name = False


# Create new file function
def new_file():
    # Delete previous data
    my_text.delete("1.0", END)

    # Changing texts after new file is created
    win.title('New File - TextPad')

    # Update status bar
    status_bar.config(text="New File            ")


# Create a function to open files
def open_file():
    # Delete previous data
    my_text.delete("1.0", END)

    # Take file name
    text_file = filedialog.askopenfilename(initialdir="C:/docs/", title="Open File", filetypes=(("Text Files", "*.txt"),
                                                                                                ("HTML Files","*.html"),
                                                                                                ("Python Files","*.py"),
                                                                                                ("All Files", "*.*")))

    # Check if a file is selected
    if text_file:
        global open_status_name
        open_status_name = text_file

    # Update status bars
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("C:/docs/", "")
    win.title(f'{name} - Textpad')

    # Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

# To save file
def save_file():
    global open_status_name

    # If the file is opened and saved
    if open_status_name:
        # Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()
        status_bar.config(text=f'Saved: {open_status_name}        ')

    # If new file and save
    else:
        saveas_file()

# Save As function
def saveas_file():
    text_file = filedialog.asksaveasfile(defaultextension=".*", initialdir="C:/docs/", title="Save File", filetypes=(("Text Files", "*.txt"),
                                                                                                                     ("HTML Files", "*.html"),
                                                                                                                     ("Python Files", "*.py")))


    name = "C:/docs/"
    status_bar.config(text=f'Saved: {name}        ')
    win.title(f'{name} - Textpad')

    # Save the file
    text_file = open(text_file.name, 'w')
    text_file.write(my_text.get(1.0, END))
    # Close the file
    text_file.close()


# Cut the selected Text
def cut_text(e):
    global selected
    if e:
        selected = win.clipboard_get()
    else:
        if my_text.selection_get():
            # Take selected text from text box
            selected = my_text.selection_get()
            # Delete the selected text
            my_text.delete("sel.first", "sel.last")
            # Clear the previously cut or copied text and add current one
            win.clipboard_clear()
            win.clipboard_append(selected)


# Copy the selectedText
def copy_text(e):
    global selected
    if e:
        selected = win.clipboard_get()

    if my_text.selection_get():
        # Take the selected text from text box
        selected = my_text.selection_get()
        win.clipboard_clear()
        win.clipboard_append(selected)


# Paste Text
def paste_text(e):
    global selected
    if e:
        selected = win.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

# Bold the text
def bold_it():
    # Create the tag
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    # Configure a tag
    my_text.tag_configure("bold", font=bold_font)

    # Define current tags
    current_tags = my_text.tag_names("sel.first")

    # See if tag has been set
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


# Italics the text
def italics_it():
    # Creating the font
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    # Configure a tag
    my_text.tag_configure("italic", font=italics_font)

    # Define current tags
    current_tags = my_text.tag_names("sel.first")

    # See if tag has been set
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


# Change text color
def text_color():
    # Pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        # Creating the color
        color_font = font.Font(my_text, my_text.cget("font"))

        # Configure a tag
        my_text.tag_configure("colored", font=color_font, foreground=my_color)

        # Define current tags
        current_tags = my_text.tag_names("sel.first")

        # See if tag has been set
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")


# BG Color
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)


# Change the whole text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)


# Create a toolbar
toolbar_frame = Frame(win)
toolbar_frame.pack(side=BOTTOM)

# Create main frame
my_frame = Frame(win)
my_frame.pack(pady=5)

# Vertical scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizontal scrollbar
hor_scroll = Scrollbar(my_frame, orient="horizontal")
hor_scroll.pack(side=BOTTOM, fill=X)

# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("helvetica", 16), selectbackground="light blue", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

# Configure scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# CreateMenu
my_menu = Menu(win)
win.config(menu=my_menu)

# Add status bar
status_bar = Label(toolbar_frame, text="Status:- Blank", anchor=E)
status_bar.grid(ipady=15, row=1, columnspan=4, pady=(0,5))

# Add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command= new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command= saveas_file)

# Drawing a l  ine to separate it
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.quit)

# Add edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="Ctrl + X")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="Ctrl + C")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="Ctrl + V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="Ctrl + Z")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="Ctrl + Y")

# Add color menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Change Selected Text", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)


# Edit bindings
win.bind('<Control-Key-x>', cut_text)
win.bind('<Control-Key-c>', copy_text)
win.bind('<Control-Key-v>', paste_text)

# Create buttons on toolbar
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5, pady=(5, 0))

italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx=5, pady=(5, 0))

color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=2, padx=5, pady=(5, 0))

undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=3, padx=5, pady=(5, 0))

redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=4, padx=5, pady=(5, 0))

win.mainloop()
