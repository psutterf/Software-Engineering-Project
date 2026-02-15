from tkinter import *
from PIL import Image, ImageTk

from PlayerEntry import PlayerEntry

# create splash screen object
splash_root = Tk()
splash_root.title("Photon")
splash_root.geometry("1200x800")
splash_root.resizable(False, False)

# resize splash screen image to match the window's size
image = Image.open("logo.png")
resized_img = image.resize((1200, 800))
img = ImageTk.PhotoImage(resized_img)

splash_label = Label(splash_root, image = img)
splash_label.image = img
splash_label.pack()

def main():
    # close splash screen
    splash_root.destroy()

    # call function to open player entry screen
    playerScreen = PlayerEntry()

# display splash screen for 5 seconds, then call main
splash_root.after(5000, main)

mainloop()