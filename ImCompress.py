import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
from Startpage import create_textframe1

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Function to update the image size when the window is resized
def update_image(event):
    width, height = img.size
    ratio = width / height
    new_height = 1600
    new_width = int(ratio * new_height)
    img_resized = img.resize((new_width, new_height))
    tkimage = ImageTk.PhotoImage(img_resized)
    # Update the label image
    imagelabel.config(image=tkimage)
    imagelabel.image = tkimage


# initalize window
Startpage = tk.Tk()
Startpage.resizable(False, False)
Startpage.title("Image Compresser")
Startpage.geometry("1600x800")

# Frame
containerframe = create_textframe1(Startpage)
imageframe1 = tk.Frame(Startpage)

# place layout
imageframe1.place(x=0, y=0, relwidth=0.26, relheight=1)
containerframe.place(relx=0.26, y=0, relwidth=0.74, relheight=1)
img = Image.open(resource_path("icon.png"))

# Create the label and pack to fill the frame
imagelabel = tk.Label(imageframe1, background="red")
imagelabel.pack(expand=True, fill="both")
imageframe1.bind("<Configure>", update_image)

# Start the main loop
Startpage.mainloop()
