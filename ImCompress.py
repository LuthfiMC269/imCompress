import tkinter as tk
from tkinter import filedialog
from PIL import Image

def browse_file():
  """Opens a file dialog to select an image file."""
  global filename
  filename = filedialog.askopenfilename(
      initialdir="/",
      title="Select a File",
      filetypes=[("Image files", "*.jpg *.jpeg *.png")]
  )
  file_entry.delete(0, tk.END)
  file_entry.insert(0, filename)

def qual():
  global quality
  quality = var.get()
  print("variable selected: " + str(quality))

def go():
  if filename:
    try:
      print("Go button clicked, filename:", filename)
      # Add your image compression logic here
      image = Image.open(filename)
      width, height = image.size
      new_size = (width // 2, height // 2)
      resized_image = image.resize(new_size)
      resized_image = resized_image.convert("RGB")
      resized_image.save('compressed_image_'+str(quality)+"%.jpg", optimize=True, quality=quality)
      success_label.config(text="Image compressed successfully!")
    except Exception as e:
      success_label.config(text=f"Error: {e}")
  else:
    # Display error message if no file is chosen
    success_label.config(text="Please choose an image file first!")


def exit_app():
  """Closes the application."""
  root.destroy()

root = tk.Tk()
var = tk.IntVar()
root.title("Image Compressor")
# Title label
title_label = tk.Label(root, text="Image Compressor", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# File selection Frame
frame_file = tk.Frame(root)
frame_file.pack(pady=5)

# File entry
file_entry = tk.Entry(frame_file, width=50)
file_entry.pack(side="left", padx=5)

# Browse button
browse_button = tk.Button(frame_file, text="Browse", command=browse_file)
browse_button.pack(side="left", padx=5)

# Qual Sel Frame
qual_frame = tk.Frame(root)
qual_frame.pack(pady=10)
# Quality Selection
Q1 = tk.Radiobutton(qual_frame, text="50% Quality", variable=var, value=50, command=qual)
Q1.pack(side="left", padx=5)
Q2 = tk.Radiobutton(qual_frame, text="60% Quality", variable=var, value=60, command=qual)
Q2.pack(side="left", padx=5)
Q3 = tk.Radiobutton(qual_frame, text="100% Quality", variable=var, value=100, command=qual)
Q3.pack(side="left", padx=5)

# Button Frame
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# Go button
go_button = tk.Button(frame_buttons, text="Go", command=go, width=10)
go_button.pack(side="left", padx=5)

# Exit button
exit_button = tk.Button(frame_buttons, text="Exit", command=exit_app, width=10)
exit_button.pack(side="left", padx=5)

# Status frame
status_frame = tk.Frame(root)
status_frame.pack(pady=3)

success_label = tk.Label(status_frame, text="STATUS")
success_label.pack(padx=5)
root.mainloop()