#imports are here
from tkinter import *

if __name__ == "__main__":
    root = Tk()

    # creating a label widged
    myLabel = Label(root, text="Hello World")
    # showing it onto the screen
    myLabel.pack()
    # start the loop
    root.mainloop()