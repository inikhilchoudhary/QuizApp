from tkinter import *

root = Tk()
root.title('QuizBee') 
root.wm_iconbitmap('QuizBeeLogo.ico') 
root.geometry('800x500')
root.minsize(800,500)
root.config(background='black')


button_image = PhotoImage(file="Drag_Drop.png")

# Define the function to be called when the button is clicked
def start_quiz():
    pass

# Customize and place the button with an image
start_button = Button(root, image=button_image, command=start_quiz, bd=0, highlightthickness=0)
start_button.pack()

# Make sure the image reference is kept alive
start_button.image = button_image


root.mainloop()
