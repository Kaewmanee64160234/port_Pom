import tkinter as tk
from PIL import Image, ImageTk

def resize_image(event):
    # Get the current window size
    window_width = event.width
    window_height = event.height

    # Calculate the new size for the image (50% of the window)
    new_width = int(window_width * 0.5)
    new_height = int(window_height * 0.5)

    # Resize the image
    resized_img = original_img.resize((new_width, new_height), Image.ANTIALIAS)
    new_photo = ImageTk.PhotoImage(resized_img)

    # Update the image in the label
    image_label.config(image=new_photo)
    image_label.image = new_photo  # Keep a reference to avoid garbage collection

# Create the main window
root = tk.Tk()
root.title("My Performance")

# Load the original image
image_path = "D:/pom/100993.jpg"  # Replace with the actual path to your image file
original_img = Image.open(image_path)

# Resize the original image to fit 50% of the window initially
initial_width = int(root.winfo_screenwidth() * 0.5)
initial_height = int(root.winfo_screenheight() * 0.5)
initial_resized_img = original_img.resize((initial_width, initial_height), Image.BILINEAR)
initial_photo = ImageTk.PhotoImage(initial_resized_img)

# Add widgets to the window
label = tk.Label(root, text="Welcome to My Performance GUI!")
label.pack(padx=10, pady=10)

# Add the initial resized image to the window
image_label = tk.Label(root, image=initial_photo)
image_label.pack(padx=10, pady=10)

# Bind the resize_image function to the window resize event
root.bind("<Configure>", resize_image)

# Run the GUI
root.mainloop()
