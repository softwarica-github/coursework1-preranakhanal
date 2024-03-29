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
    
    def completed_TopLevel():
        WIN_top = Toplevel(bg='white')
        WIN_top.title("Sucess")  
        WIN_top.geometry('300x150')
        tfont_tup = ("Comic Sans MS", 15)
        def reset_click():
            reset()
            WIN_top.destroy()
            
            
        def close_click():
            WIN_top.destroy()
            WIN.destroy()
        
        message = Label(WIN_top, bg='white', text="Wordlist generation completed!", font=tfont_tup, justify="center",foreground="black")  
        message.pack()
        
        reset_button = Button(WIN_top, bg='white', text="Reset", background='Red', foreground="Black", font=("Comic Sans MS", 12), command=reset_click)
        reset_button.place(x=108, y=80)
        
        close_button = Button(WIN_top, bg='white', text="Close", background='Red', foreground="Black", font=("Comic Sans MS", 12), command=close_click)
        close_button.place(x=180, y=80)
        
        WIN_top.mainloop()
    
    def generate():
    # Get the selected character sets
        characters = ''
        if small_letter_var.get() == 1:
            characters += string.ascii_lowercase
        if capital_letter_var.get() == 1:
            characters += string.ascii_uppercase
        if number_var.get() == 1:
            characters += string.digits
        if special_var.get() == 1:
            characters += string.punctuation
        if custom_char_entry.get() != '':
            characters += custom_char_entry.get()

        # Get the word length
        length = int(pass_length_entry.get())

        # Calculate the total number of words
        total_words = len(characters) ** length

        # Open the output file
        with open(file_location.get(), 'w') as f:
            # Generate all combinations of the characters of the specified length
            for i, word in enumerate(itertools.product(characters, repeat=length), 1):
                # Write the word to the file
                f.write(''.join(word) + '\n')

                # Update the progress bar
                progress = i / total_words * 100
                progress_bar['value'] = progress
                percentage_label['text'] = f"{progress:.2f}%"  # Update the percentage label
                WIN.update_idletasks()
                time.sleep(0.01)

        completed_TopLevel()
    
    def reset():
        # Reset all fields and progress bar
        small_letter_var.set(0)
        capital_letter_var.set(0)
        number_var.set(0)
        special_var.set(0)
        custom_char_entry.config(state=DISABLED)
        custom_char_entry.delete(0, END)
        pass_length_entry.delete(0, END)
        file_location.delete(0, END)
        progress_bar['value'] = 0  

    progress_bar = ttk.Progressbar(WIN, length=475, mode='determinate')
    progress_bar.place(x=30, y=260)
    
    
    percentage_label = Label(WIN, text="", font=tfont_canvas, bg="white", fg="black")
    percentage_label.place(x=515, y=260)  # Adjust the position as needed

    generate_button = Button(WIN, text="Generate", font=tfont_canvas, bg="black", fg="white", command=generate)
    generate_button.place(x=250, y=300)
    
    reset_button = Button(WIN, text="Reset", font=tfont_canvas, bg="black", fg="white", command=reset)
    reset_button.place(x=350, y=300)
    
    WIN.mainloop()
    
worldlist_generator()
    