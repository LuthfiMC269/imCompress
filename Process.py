import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk


quality = 90
sampling = 1
updatedpath = 0


def qual(value):
    global quality
    quality = round(float(value))
    print("Quality value: " + str(quality))


def sample():
    global sampling
    sampling = inter.get()
    print("Sampling selected: " + str(sampling))


def smpstring():
    if sampling == 1:
        return "lanczos"
    else:
        return "Nearest"


def browse_file(frame, imagelabel):
    global updatedpath
    updatedpath = filedialog.askopenfilename(
        initialdir="/",
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if updatedpath != 0:
        # Update the image preview
        load_image(frame, updatedpath)
        imagelabel.destroy()
        print("file selected: " + updatedpath)


def load_image(frame, filename):
    image = Image.open(filename)
    width, height = image.size
    ratio = width / height
    new_height = 700
    new_width = int(ratio * new_height)
    image = image.resize((new_width, new_height), sampling)
    image = ImageTk.PhotoImage(image)
    img_label = tk.Label(frame, image=image, bg="#373737")
    img_label.image = image  # Keep a reference to avoid garbage collection
    img_label.place(relx=0, rely=0, relwidth=1, relheight=1)


def go(path):
    if updatedpath != 0:
        file = updatedpath
    else:
        file = path
    image = Image.open(file)
    width, height = image.size
    new_size = (width // 2, height // 2)
    resized_image = image.resize(new_size, sampling)
    # 1 lancozs 4 box
    resized_image = resized_image.convert("RGB")
    resized_image.save('compressed_image_' + str(quality) + "% " + smpstring() + ".jpg", optimize=True, quality=quality)
#           success_label.config(text="Image compressed successfully!")


#           success_label.config(text=f"Error: {e}")


def imgpreview(event, imgprev, imagelabel):
    width, height = imgprev.size
    ratio = width / height
    new_height = 700
    new_width = int(ratio * new_height)
    imgprevres = imgprev.resize((new_width, new_height), 1)
    imgprevtk = ImageTk.PhotoImage(imgprevres)
    imagelabel.config(image=imgprevtk)
    imagelabel.image = imgprevtk


def create_textframe2(parent, filename):
    global var, inter
    filepath = filename
    var = tk.IntVar()
    inter = tk.IntVar()
    stylebg = ttk.Style()
    stylebg.configure("TScale", background="#373737")
    textframe2 = tk.Frame(parent, bg="#373737")
    textframe2.place(relx=0.26, y=0, relwidth=0.74, relheight=1)

# Preview Text Frame and label
    previewframe = tk.Frame(textframe2, bg="red")
    previewframe.place(relx=0.01, y=0, relwidth=0.4, relheight=0.1)
    previewlabel = tk.Label(previewframe, text="Preview: ", font=("Poppins-bold", 32, "bold"),
                            anchor="w", bg="#373737", fg="white")
    previewlabel.pack(side="left", expand=True, fill="both")

    """Focus on this"""
# Image Preview FROM STARTPAGE
    imgframe = tk.Frame(textframe2, bg="red")
    imgframe.place(relx=0.02, rely=0.1, relwidth=0.8, relheight=0.6)
    imgprev = Image.open(filepath)
    imagelabel = tk.Label(imgframe, bg="#373737")
    imagelabel.pack(expand=True, fill="both")
    imgframe.bind("<Configure>", lambda event: imgpreview("event", imgprev, imagelabel))

# Option Frame
    optionframe = tk.Frame(textframe2, bg="#373737")
    optionframe.place(relx=0.02, rely=0.78, relwidth=0.8, relheight=0.2)
# Quality, Browse button Selection
    qualframe = tk.Frame(optionframe, bg="#373737")
    qualframe.place(relwidth=0.5, relheight=1)
    quallabel = tk.Label(optionframe, text="Quality", font=("Helvetica", 14), bg="#373737", fg="white")
    quallabel.place(relx=0.01, rely=0.01)
    quallabel2 = tk.Label(optionframe, text="Less", font=("Helvetica", 12), bg="#373737", fg="white")
    quallabel2.place(relx=0.01, rely=0.2)
    quallabel3 = tk.Label(qualframe, text="Detailed", font=("Helvetica", 12), bg="#373737", fg="white")
    quallabel3.place(relx=0.85, rely=0.19)
    qualscroll = ttk.Scale(qualframe, orient="horizontal", variable=var, command=qual, from_=50, to=100, style="TScale")
    qualscroll.place(relx=0.01, rely=0.3, relwidth=0.98, relheight=0.3)
    qualscroll.set(90)
    browsebutton = tk.Button(qualframe, text="Browse File", command=lambda: browse_file(imgframe, imagelabel),
                             font=("Helvetica", 14))
    browsebutton.place(relx=0.01, rely=0.62, relwidth=0.98, relheight=0.3)

# Interpolation, Process Button Selection
    interframe = tk.Frame(optionframe, bg="#373737")
    interframe.place(relx=0.51, relwidth=0.5, relheight=1)
    # Sampling Selection
    sample2 = tk.Radiobutton(interframe, text="Nearest Interpolation", fg="white", bg="#373737",
                             activebackground="#373737", activeforeground="white",
                             variable=inter, value=0, command=sample, font=("Helvetica", 14))
    sample2.select()
    sample2.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.5)
    sample1 = tk.Radiobutton(interframe, text="Lanczos Interpolation", fg="white", bg="#373737",
                             activebackground="#373737", activeforeground="white",
                             variable=inter, value=1, command=sample, font=("Helvetica", 14))
    sample1.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.5)
    process = tk.Button(interframe, text="Process", command=lambda: go(filepath), font=("Helvetica", 14))
    process.place(relx=0.01, rely=0.62, relwidth=0.98, relheight=0.3)


if __name__ == "__main__":
    # This block allows you to run textframe2 independently for debugging
    root = tk.Tk()
    root.geometry("1600x800")
    root.resizable(True, True)

    # Create and display textframe2
    create_textframe2(root, filename="icon.png")

    root.mainloop()
