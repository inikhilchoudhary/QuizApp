from customtkinter import *
from tkinter import messagebox
from mysql.connector import connect, Error

back_ground_clr = 'black'

# Initialize the main window
root = CTk()

# Set the title of the window
root.title("CustomTkinter Window")
root.geometry('1000x500')

def go_back():
    root.destroy()

# Function to clear window contents
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def show_admin_dashboard():
    clear_window()

    # Load icons (ensure the paths are correct)
    toggle_icon = CTkImage(file='images/toggle_btn_icon.png')
    user_icon = CTkImage(file='images/User.png')
    teacher_icon = CTkImage(file='images/Teacher.png')
    student_icon = CTkImage(file='images/Students.png')
    exit_icon = CTkImage(file='images/Exit.png')

    menu_bar_frame = CTkFrame(master=root, fg_color=back_ground_clr)

    toggle_menu_btn = CTkButton(master=menu_bar_frame, image=toggle_icon, fg_color=back_ground_clr)
    toggle_menu_btn.place(x=4, y=10)
    
    user_btn = CTkButton(master=menu_bar_frame, image=user_icon, fg_color=back_ground_clr, command=lambda: indicate(user_btn_indicator, user_page))
    user_btn.place(x=9, y=130, width=30, height=40)
    user_btn_indicator = CTkLabel(master=menu_bar_frame, fg_color=back_ground_clr)
    user_btn_indicator.place(x=3, y=130, width=3, height=35)
    
    teacher_btn = CTkButton(master=menu_bar_frame, image=teacher_icon, fg_color=back_ground_clr, command=lambda: indicate(teacher_btn_indicator, teacher_page))
    teacher_btn.place(x=9, y=190, width=30, height=40)
    teacher_btn_indicator = CTkLabel(master=menu_bar_frame, fg_color=back_ground_clr)
    teacher_btn_indicator.place(x=3, y=190, width=3, height=35)
    
    students_btn = CTkButton(master=menu_bar_frame, image=student_icon, fg_color=back_ground_clr, command=lambda: indicate(students_btn_indicator, student_page))
    students_btn.place(x=9, y=250, width=30, height=40)
    students_btn_indicator = CTkLabel(master=menu_bar_frame, fg_color=back_ground_clr)
    students_btn_indicator.place(x=3, y=250, width=3, height=35)
    
    exit_btn = CTkButton(master=menu_bar_frame, image=exit_icon, fg_color=back_ground_clr, command=lambda: indicate(exit_btn_indicator, show_login_form))
    exit_btn.place(x=9, y=310, width=30, height=40)
    exit_btn_indicator = CTkLabel(master=menu_bar_frame, fg_color=back_ground_clr)
    exit_btn_indicator.place(x=3, y=310, width=3, height=35)
    
    menu_bar_frame.pack(side=LEFT)
    menu_bar_frame.pack_propagate(False)
    menu_bar_frame.configure(width=45, height=500)
    
    main_frame = CTkFrame(master=root, fg_color='Grey')
    main_frame.pack(side=LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(height=500, width=955)

    def indicate(lb, page=None):
        hide_indicators()
        lb.config(fg_color='white')
        delete_page()
        if page:
            page()

    def hide_indicators():
        user_btn_indicator.config(fg_color=back_ground_clr)
        teacher_btn_indicator.config(fg_color=back_ground_clr)
        students_btn_indicator.config(fg_color=back_ground_clr)
        exit_btn_indicator.config(fg_color=back_ground_clr)

    def delete_page():
        for frame in main_frame.winfo_children():
            frame.destroy()
        
    def user_page():
        user_frame = CTkFrame(main_frame)
        lb = CTkLabel(user_frame, text="User profile page")
        lb.pack()
        user_frame.pack(padx=20)
        
    def teacher_page():
        root.title("Manage Teachers") 
        teacher_frame = CTkFrame(main_frame, width=955, height=500, fg_color=back_ground_clr)
        
        # Load icons (ensure the paths are correct)
        add_teacher_icon = CTkImage(file='images/Add.png')
        remove_teacher_icon = CTkImage(file='images/Remove.png')
        more_icon = CTkImage(file='images/More.png')

        # Calculate the spacing between buttons
        button_width = 128
        num_buttons = 3
        total_buttons_width = button_width * num_buttons
        spacing = (880 - total_buttons_width) // (num_buttons + 1)

        # Create buttons with images only, ensuring they display the full image
        add_teacher_btn = CTkButton(teacher_frame, image=add_teacher_icon, fg_color=back_ground_clr, command=add_teacher)
        add_teacher_btn.place(x=spacing, y=180, width=button_width, height=128)

        remove_teacher_btn = CTkButton(teacher_frame, image=remove_teacher_icon, fg_color=back_ground_clr, command=remove_teacher)
        remove_teacher_btn.place(x=spacing * 2 + button_width, y=180, width=button_width, height=128)

        more_btn = CTkButton(teacher_frame, image=more_icon, fg_color=back_ground_clr)
        more_btn.place(x=spacing * 3 + button_width * 2, y=180, width=button_width, height=128)

        # Add labels under each button
        CTkLabel(teacher_frame, text="Add Teacher", fg_color=back_ground_clr, text_color="white").place(x=spacing, y=320, width=button_width)
        CTkLabel(teacher_frame, text="Remove Teacher", fg_color=back_ground_clr, text_color="white").place(x=spacing * 2 + button_width, y=320, width=button_width)
        CTkLabel(teacher_frame, text="More", fg_color=back_ground_clr, text_color="white").place(x=spacing * 3 + button_width * 2, y=320, width=button_width)

        teacher_frame.pack()

    def student_page():
        root.title("Manage Students") 
        student_frame = CTkFrame(main_frame, width=955, height=500, fg_color=back_ground_clr)

        # Load icons (ensure the paths are correct)
        add_student_icon = CTkImage(file='images/Add.png')
        remove_student_icon = CTkImage(file='images/Remove.png')
        more_icon = CTkImage(file='images/More.png')

        # Calculate the spacing between buttons
        button_width = 128
        num_buttons = 3
        total_buttons_width = button_width * num_buttons
        spacing = (955 - total_buttons_width) // (num_buttons + 1)

        # Create buttons with images only, ensuring they display the full image
        add_student_btn = CTkButton(student_frame, image=add_student_icon, fg_color=back_ground_clr, command=add_student)
        add_student_btn.place(x=spacing, y=180, width=button_width, height=128)

        remove_student_btn = CTkButton(student_frame, image=remove_student_icon, fg_color=back_ground_clr, command=remove_student)
        remove_student_btn.place(x=spacing * 2 + button_width, y=180, width=button_width, height=128)

        more_btn = CTkButton(student_frame, image=more_icon, fg_color=back_ground_clr)
        more_btn.place(x=spacing * 3 + button_width * 2, y=180, width=button_width, height=128)

        # Add labels under each button
        CTkLabel(student_frame, text="Add Student", fg_color=back_ground_clr, text_color="white").place(x=spacing, y=320, width=button_width)
        CTkLabel(student_frame, text="Remove Student", fg_color=back_ground_clr, text_color="white").place(x=spacing * 2 + button_width, y=320, width=button_width)
        CTkLabel(student_frame, text="More", fg_color=back_ground_clr, text_color="white").place(x=spacing * 3 + button_width * 2, y=320, width=button_width)

        student_frame.pack()

    show_admin_dashboard()
    
    def add_teacher():
        pass  # Implement this function

    def remove_teacher():
        pass  # Implement this function

    def add_student():
        pass  # Implement this function

    def remove_student():
        pass  # Implement this function

    root.mainloop()
