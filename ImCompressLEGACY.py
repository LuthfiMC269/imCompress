import tkinter as tk
from tkinter import filedialog
from PIL import Image


def browse_file():
    global filename
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    file_entry.config(state="normal")
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)
    file_entry.config(state="disabled")
    qual()
    sample()
    print("file selected: " + filename)


def qual():
    global quality
    quality = var.get()
    print("variable selected: " + str(quality))


def sample():
    global sampling
    sampling = inter.get()
    print("Sampling selected: " + str(sampling))


def smpstring():
    if sampling == 1:
        return "lanczos"
    else:
        return "Nearest"


def go():
    if filename:
        try:
            image = Image.open(filename)
            width, height = image.size
            new_size = (width // 2, height // 2)
            resized_image = image.resize(new_size, sampling)
            # 1 lancozs 4 box
            resized_image = resized_image.convert("RGB")
            resized_image.save('compressed_image_' + str(quality) + "% " + smpstring() + ".jpg",
                               optimize=True, quality=quality)
            success_label.config(text="Image compressed successfully!")
        except Exception as e:
            success_label.config(text=f"Error: {e}")


def exit_app():
    window.destroy()


# initalize window
window = tk.Tk()
var = tk.IntVar()
inter = tk.IntVar()
window.resizable(True, True)
window.title("Image Compresser")
window.geometry("650x250")
# window.configure(bg="#1F1F1F")
# Title label
title_label = tk.Label(window, text="Image Compressor", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# File selection Frame
frame_file = tk.Frame(window)
frame_file.pack(pady=5)

# File label
text_label = tk.Label(frame_file, text="Choose file to be compressed")
text_label.pack(side="left", padx=5)
# File entry
file_entry = tk.Entry(frame_file, width=50, state="disabled")
file_entry.pack(side="left", padx=5)

# Browse button
browse_button = tk.Button(frame_file, text="Browse", command=browse_file)
browse_button.pack(side="left", padx=5)

# Qual Sel Frame
qual_frame = tk.Frame(window)
qual_frame.pack(pady=10)

# Quality Selection

Q2 = tk.Radiobutton(qual_frame, text="60% Quality", variable=var, value=60, command=qual)
Q2.pack(side="left", padx=5)
Q2.select()
Q3 = tk.Radiobutton(qual_frame, text="70% Quality", variable=var, value=70, command=qual)
Q3.pack(side="left", padx=5)
Q4 = tk.Radiobutton(qual_frame, text="80% Quality", variable=var, value=80, command=qual)
Q4.pack(side="left", padx=5)
Q5 = tk.Radiobutton(qual_frame, text="90% Quality", variable=var, value=90, command=qual)
Q5.pack(side="left", padx=5)
Q6 = tk.Radiobutton(qual_frame, text="100% Quality", variable=var, value=100, command=qual)
Q6.pack(side="left", padx=5)

# Sampling Sel Frame
sampling_frame = tk.Frame(window)
sampling_frame.pack(pady=10)

# Sampling Selection

I2 = tk.Radiobutton(sampling_frame, text="Lanczos Interpolation", variable=inter, value=1, command=sample)
I2.pack(side="left", padx=5)
I2.select()
I3 = tk.Radiobutton(sampling_frame, text="Nearest Interpolation", variable=inter, value=0, command=sample)
I3.pack(side="left", padx=5)

# Button Frame
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

# Go button
go_button = tk.Button(frame_buttons, text="Go", command=go, width=10)
go_button.pack(side="left", padx=5)

# Exit button
exit_button = tk.Button(frame_buttons, text="Exit", command=exit_app, width=10)
exit_button.pack(side="left", padx=5)

# Status frame
status_frame = tk.Frame(window)
status_frame.pack(pady=3)

# Status Label
success_label = tk.Label(status_frame, text="STATUS")
success_label.pack(padx=5)

window.mainloop()
