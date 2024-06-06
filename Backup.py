from tkinter import *

root = Tk()
root.geometry('925x500')

menu_bar_color = '#383838'

# icon
toggle_icon = PhotoImage(file='Images/toggle_btn_icon.png')
user_icon = PhotoImage(file='Images/User.png')
teacher_icon = PhotoImage(file='Images/Teacher.png')
student_icon = PhotoImage(file='Images/Students.png')
exit_icon = PhotoImage(file='Images/Exit.png')

# switch indicator
def switch_indicator(indicator_lb):
    user_btn_indicator.config(bg=menu_bar_color)
    students_btn_indicator.config(bg=menu_bar_color)
    teacher_btn_indicator.config(bg=menu_bar_color)
    exit_btn_indicator.config(bg=menu_bar_color)
    indicator_lb.config(bg='white')

# switch frame
def show_frame(frame):
    frame.tkraise()

menu_bar_frame = Frame(root, bg=menu_bar_color)

toggle_menu_btn = Button(menu_bar_frame, image=toggle_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color)
toggle_menu_btn.place(x=4, y=10)

user_btn = Button(menu_bar_frame, image=user_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: [switch_indicator(user_btn_indicator), show_frame(user_frame)])
user_btn.place(x=9, y=130, width=30, height=40)

teacher_btn = Button(menu_bar_frame, image=teacher_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: [switch_indicator(teacher_btn_indicator), show_frame(teacher_frame)])
teacher_btn.place(x=9, y=250, width=30, height=40)

students_btn = Button(menu_bar_frame, image=student_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: [switch_indicator(students_btn_indicator), show_frame(students_frame)])
students_btn.place(x=9, y=190, width=30, height=40)

exit_btn = Button(menu_bar_frame, image=exit_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: [switch_indicator(exit_btn_indicator), show_frame(exit_frame)])
exit_btn.place(x=9, y=310, width=30, height=40)

# same other buttons

# now indicator of active
user_btn_indicator = Label(menu_bar_frame, bg='white')
user_btn_indicator.place(x=3, y=130, width=3, height=40)

students_btn_indicator = Label(menu_bar_frame, bg=menu_bar_color)
students_btn_indicator.place(x=3, y=190, width=3, height=40)

teacher_btn_indicator = Label(menu_bar_frame, bg=menu_bar_color)
teacher_btn_indicator.place(x=3, y=250, width=3, height=40)

exit_btn_indicator = Label(menu_bar_frame, bg=menu_bar_color)
exit_btn_indicator.place(x=3, y=310, width=3, height=40)

menu_bar_frame.pack(side=LEFT, fill=Y, padx=3, pady=4)
menu_bar_frame.pack_propagate()

menu_bar_frame.configure(width=45)

# Create main content frames
user_frame = Frame(root)
teacher_frame = Frame(root)
students_frame = Frame(root)
exit_frame = Frame(root)

for frame in (user_frame, teacher_frame, students_frame, exit_frame):
    frame.place(x=45, y=0, width=880, height=500)

# Add content to each frame
Label(user_frame, text="User Window", font=('Arial', 24)).pack(expand=True)
Label(teacher_frame, text="Teacher Window", font=('Arial', 24)).pack(expand=True)
Label(students_frame, text="Students Window", font=('Arial', 24)).pack(expand=True)
Label(exit_frame, text="Exit Window", font=('Arial', 24)).pack(expand=True)

# Show initial frame
show_frame(user_frame)

root.mainloop()
