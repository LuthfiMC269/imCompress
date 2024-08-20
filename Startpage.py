import tkinter as tk
from tkinter import filedialog
from Process import create_textframe2


def browse_file():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    print("file selected: " + filename)
    return filename


def switch_to_textframe2(parent, textframe1):
    filename = browse_file()
    if filename:  # Proceed only if a file is selected
        # Destroy frame
        textframe1.destroy()

        # Create and place textframe2
        create_textframe2(parent, filename)


def create_textframe1(parent):
    textframe1 = tk.Frame(parent, bg="#373737")
    textframe1.place(relx=0.26, y=0, relwidth=0.74, relheight=1)

    l1 = tk.Label(textframe1, text="Let's Start!", bg="#373737", fg="white", font=("Poppins-bold", 25, "bold"))
    l1.place(relx=0.5, rely=0.4, anchor="center")
    l2 = tk.Label(textframe1, text="Choose Image you want to compress", bg="#373737", fg="white",
                  font=("Helvetica", 16))
    l2.place(relx=0.5, rely=0.47, anchor="center")
    browse_button = tk.Button(textframe1, text="Browse", font=("Helvetica", 15), command=lambda: switch_to_textframe2(parent, textframe1),
                              fg="#FFFFFF", bg="#46c24b", activebackground="#169d1c", activeforeground="#FFFFFF", width=10, height=1, border=0, padx=16, pady=8, cursor="hand2")
    browse_button.place(relx=0.5, rely=0.58, anchor="center")
    browse_button.bind("<Enter>", lambda e: 
            browse_button.config(
                bg="#28a72d"
            )
        )
    browse_button.bind("<Leave>", lambda e: 
            browse_button.config(
                bg="#46c24b"
            )
        )
    return textframe1
