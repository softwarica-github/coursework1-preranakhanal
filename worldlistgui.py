from tkinter import *
from tkinter import filedialog,ttk
import itertools
import string
import time

def worldlist_generator():
    WIN = Tk()
    WIN.title('Random Wordlist Generator')
    WIN.geometry('600x400')
    tfont_title = ("Comic Sans MS", 15)
    WIN.config(bg="black")
    
    title = Label(WIN, text="Random Wordlist Generator", font=tfont_title , bg="black", fg="white")
    title.place(x=180, y=5)
    background = Canvas(WIN, bg="white", width=560, height=340)
    background.pack(padx=(15,15), pady=(40,20))
    tfont_canvas = ("Comic Sans MS", 12)
    
    characterset_label = Label(WIN, text="Character Set", font=tfont_canvas, bg="white", fg="black")
    characterset_label.place(x=30, y=40)
    
    small_letter_var = IntVar()
    small_letter_checkbox = Checkbutton(WIN, text="a-z", font=tfont_canvas, bg="white", fg="black", variable=small_letter_var)
    small_letter_checkbox.place(x=50, y=70)
    
    capital_letter_var = IntVar()
    capital_letter_checkbox = Checkbutton(WIN, text="A-Z", font=tfont_canvas, bg="white", fg="black", variable=capital_letter_var)
    capital_letter_checkbox.place(x=170, y=70)
    
    number_var = IntVar()
    number_checkbox = Checkbutton(WIN, text="0-9", font=tfont_canvas, bg="white", fg="black", variable=number_var)
    number_checkbox.place(x=290, y=70)
    
    special_var = IntVar()
    special_checkbox = Checkbutton(WIN, text="Common Special", font=tfont_canvas, bg="white", fg="black", variable=special_var)
    special_checkbox.place(x=410, y=70)
    
    Label(WIN, text="Custom Characters:", font=tfont_canvas, bg="white", fg="black").place(x=30, y=110)
    custom_char_entry = Entry(WIN, font=tfont_canvas, state=DISABLED , border=1 )

    def enable_custom_chars():
        if special_var.get() == 1:
            custom_char_entry.config(state=NORMAL)
        else:
            custom_char_entry.config(state=DISABLED)

    special_checkbox.config(command=enable_custom_chars)
    custom_char_entry.place(x=200, y=115)
    
    pass_length_label = Label(WIN, text="Password Length:", font=tfont_canvas, bg="white", fg="black")
    pass_length_label.place(x=30, y=150)
    pass_length_entry = Spinbox(WIN, from_=1, to=100, font=tfont_canvas, width=5) 
    pass_length_entry.place(x=200, y=150)
    
    worldlist_output = Label(WIN, text="Wordlist Output:", font=tfont_canvas, bg="white", fg="black")
    worldlist_output.place(x=30, y=190)
    
    # Place where the file location is showed as per Browsing
    file_location = Entry(WIN, font=tfont_canvas, width=30)
    file_location.place(x=200, y=190)
    
    def browse():
        file_location.delete(0, END)
        file_location.insert(0, filedialog.askopenfilename())
        
    browse_button = Button(WIN, text="Browse", font=tfont_canvas, command=browse)
    browse_button.place(x=490, y=185)
    

    WIN.mainloop()
    
worldlist_generator()
    