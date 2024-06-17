import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import messagebox

back_ground_clr = '#383838'


###----------------------------------DATABASE CONNECTION CODE --------------------------------###
# Function to connect to MySQL database (Main Data base --> quizbee_db)
def connect_to_db():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='QuizBee',
                                             user='root',
                                             password='Nik@1234')
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None
###----------------------------------END DATABASE CONNECTION CODE ----------------------------###



###----------------------------------MISCLINIOUS FUNCTIONS CODE ------------------------------###
#Function to back window
def go_back():
    root.destroy() 
# Function to clear window contents
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
###----------------------------------END MISCLINIOUS FUNCTIONS CODE --------------------------###



###----------------------------------AUTHENTICATION FUNCTIONS CODE ---------------------------###
def sign_in(user, password):
    username = user.get()
    passwd = password.get()

    try:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, passwd))
            user_data = cursor.fetchone()
            
            if user_data:
                messagebox.showinfo("Login Success", f"Welcome {username.capitalize()}! You are logged in as a {user_data['role'].capitalize()}.")
                clear_window()
                show_user_profile(username)  # Call to display user profile after successful login
                if user_data['role'] == "admin":
                    show_admin_dashboard()
                elif user_data['role'] == "teacher":
                    show_teacher_dashboard()
                else:
                    show_student_dashboard()
            else:
                messagebox.showerror("Login Failed", "Invalid Username or Password")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def show_user_profile(username):
    try:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT name, email, role, password FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            user_data = cursor.fetchone()
            
            clear_window()
            root.title("User Profile")
            
            profile_frame = Frame(root, bg=back_ground_clr)
            profile_frame.pack(pady=20)
            
            Label(profile_frame, text="User Profile", font=('Microsoft YaHei UI Light', 23, 'bold'), bg="white", fg='#57a1f8').pack(pady=20)
            
            Label(profile_frame, text=f"Name: {user_data['name']}", bg="white", fg="black", font=('Microsoft YaHei UI Light', 14)).pack(pady=5)
            Label(profile_frame, text=f"Email: {user_data['email']}", bg="white", fg="black", font=('Microsoft YaHei UI Light', 14)).pack(pady=5)
            Label(profile_frame, text=f"Role: {user_data['role'].capitalize()}", bg="white", fg="black", font=('Microsoft YaHei UI Light', 14)).pack(pady=5)
            Label(profile_frame, text="Password: **********", bg="white", fg="black", font=('Microsoft YaHei UI Light', 14)).pack(pady=5)
            
            back_button = Button(profile_frame, text="Back", font=('Microsoft YaHei UI Light', 15), bg="#57a1f8", fg="white", command=show_login_form)
            back_button.pack(pady=10)
            
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

###----------------------------------END AUTHENTICATION FUNCTIONS CODE -----------------------###



###----------------------------------DASHBOARDS CODE -----------------------------------------###


def show_admin_dashboard():
    clear_window()

    # Load icons (ensure the paths are correct)
    toggle_icon = PhotoImage(file='images/toggle_btn_icon.png')
    user_icon = PhotoImage(file='images/User.png')
    teacher_icon = PhotoImage(file='images/Teacher.png')
    student_icon = PhotoImage(file='images/Students.png')
    exit_icon = PhotoImage(file='images/Exit.png')

    # Store references to images to prevent garbage collection
    root.toggle_icon = toggle_icon
    root.user_icon = user_icon
    root.teacher_icon = teacher_icon
    root.student_icon = student_icon
    root.exit_icon = exit_icon
    
    menu_bar_frame = Frame(root, bg=back_ground_clr)

    toggle_menu_btn = Button(menu_bar_frame, image=toggle_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr)
    toggle_menu_btn.place(x=4, y=10)
    
    user_btn = Button(menu_bar_frame, image=user_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr, command=lambda: indicate(user_btn_indicator, user_page))
    user_btn.place(x=9, y=130, width=30, height=40)
    user_btn_indicator = Label(menu_bar_frame, bg=back_ground_clr)
    user_btn_indicator.place(x=3, y=130, width=3, height=35)
    
    teacher_btn = Button(menu_bar_frame, image=teacher_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr, command=lambda: indicate(teacher_btn_indicator, teacher_page))
    teacher_btn.place(x=9, y=190, width=30, height=40)
    teacher_btn_indicator = Label(menu_bar_frame, bg=back_ground_clr)
    teacher_btn_indicator.place(x=3, y=190, width=3, height=35)
    
    students_btn = Button(menu_bar_frame, image=student_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr, command=lambda: indicate(students_btn_indicator,student_page))
    students_btn.place(x=9, y=250, width=30, height=40)
    students_btn_indicator = Label(menu_bar_frame, bg=back_ground_clr)
    students_btn_indicator.place(x=3, y=250, width=3, height=35)
    
    exit_btn = Button(menu_bar_frame, image=exit_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr, command=lambda: indicate(exit_btn_indicator, show_login_form))
    exit_btn.place(x=9, y=310, width=30, height=40)
    exit_btn_indicator = Label(menu_bar_frame, bg=back_ground_clr)
    exit_btn_indicator.place(x=3, y=310, width=3, height=35)
    
    menu_bar_frame.pack(side=LEFT)
    menu_bar_frame.pack_propagate(False)
    menu_bar_frame.configure(width=45, height=500)
    
    main_frame = Frame(root, bg='Grey')
    main_frame.pack(side=LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(height=500, width=955)

    def indicate(lb, page=None):
        hide_indicators()
        lb.config(bg='white')
        delete_page()
        if page:
            page()

    def hide_indicators():
        user_btn_indicator.config(bg=back_ground_clr)
        teacher_btn_indicator.config(bg=back_ground_clr)
        students_btn_indicator.config(bg=back_ground_clr)
        exit_btn_indicator.config(bg=back_ground_clr)

    def delete_page():
        for frame in main_frame.winfo_children():
            frame.destroy()
        
    def user_page():
        user_frame = Frame(main_frame)
        lb = Label(user_frame, text="User profile page")
        lb.pack()
        user_frame.pack(padx=20)
        
    def teacher_page():
        root.title("Manage Teachers") 
        teacher_frame = Frame(main_frame,width=955,height=500,bg='black')
        back_ground_clr = 'black'
        
        # Load icons (ensure the paths are correct)
        add_teacher_icon = PhotoImage(file='images/Add.png')
        remove_teacher_icon = PhotoImage(file='images/Remove.png')
        more_icon = PhotoImage(file='images/More.png')

        # Store references to images to prevent garbage collection
        teacher_frame.add_teacher_icon = add_teacher_icon
        teacher_frame.remove_teacher_icon = remove_teacher_icon
        teacher_frame.more_dashboard_icon = more_icon

        # Calculate the spacing between buttons
        button_width = 128
        num_buttons = 3
        total_buttons_width = button_width * num_buttons
        spacing = (880 - total_buttons_width) // (num_buttons + 1)

        # Create buttons with images only, ensuring they display the full image
        add_teacher_btn = Button(teacher_frame, image=add_teacher_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr, command=add_teacher)
        add_teacher_btn.place(x=spacing, y=180, width=button_width, height=128)

        remove_teacher_btn = Button(teacher_frame, image=remove_teacher_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr, command=remove_teacher)
        remove_teacher_btn.place(x=spacing * 2 + button_width, y=180, width=button_width, height=128)

        more_btn = Button(teacher_frame, image=more_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr)
        more_btn.place(x=spacing * 3 + button_width * 2, y=180, width=button_width, height=128)

        # Add labels under each button
        Label(teacher_frame, text="Add Teacher", bg=back_ground_clr, fg="white").place(x=spacing, y=320, width=button_width)
        Label(teacher_frame, text="Remove Teacher", bg=back_ground_clr, fg="white").place(x=spacing * 2 + button_width, y=320, width=button_width)
        Label(teacher_frame, text="More", bg=back_ground_clr, fg="white").place(x=spacing * 3 + button_width * 2, y=320, width=button_width)

        teacher_frame.pack()

    def student_page():
        root.title("Manage Students") 
        student_frame = Frame(main_frame,width=955,height=500,bg='black')


        # Load icons (ensure the paths are correct)
        add_student_icon = PhotoImage(file='images/Add.png')
        remove_student_icon = PhotoImage(file='images/Remove.png')
        more_icon = PhotoImage(file='images/More.png')

        # Store references to images to prevent garbage collection
        student_frame.add_student_icon = add_student_icon
        student_frame.remove_student_icon = remove_student_icon
        student_frame.more_icon = more_icon

        # Calculate the spacing between buttons
        button_width = 128
        num_buttons = 3
        total_buttons_width = button_width * num_buttons
        spacing = (955 - total_buttons_width) // (num_buttons + 1)

        # Create buttons with images only, ensuring they display the full image
        add_student_btn = Button(student_frame, image=add_student_icon, bg='black', bd=0, activebackground='black', command=add_student)
        add_student_btn.place(x=spacing, y=180, width=button_width, height=128)

        remove_student_btn = Button(student_frame, image=remove_student_icon, bg='black', bd=0, activebackground='black', command=remove_student)
        remove_student_btn.place(x=spacing * 2 + button_width, y=180, width=button_width, height=128)

        more_btn = Button(student_frame, image=more_icon, bg='black', bd=0, activebackground='black')
        more_btn.place(x=spacing * 3 + button_width * 2, y=180, width=button_width, height=128)

        # Add labels under each button
        Label(student_frame, text="Add Student", bg='black', fg="white").place(x=spacing, y=320, width=button_width)
        Label(student_frame, text="Remove Student", bg='black', fg="white").place(x=spacing * 2 + button_width, y=320, width=button_width)
        Label(student_frame, text="More", bg='black', fg="white").place(x=spacing * 3 + button_width * 2, y=320, width=button_width)

        student_frame.pack()

    def add_teacher():
        clear_window()
        root.title("Add Teacher")
        button_width = 128
        MainFrame=Frame(root,bg=back_ground_clr)
        MainFrame.pack()
        MainFrame.propagate(0)
        MainFrame.configure(width=1000, height=500)
        heading = Label(MainFrame, text="Add Teacher", fg='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold'), bg=back_ground_clr)
        heading.place(x=350, y=5)
        #-------------------BUTTON ----------#
        back_icon = PhotoImage(file='images/Back.png')
        add_teacher_icon = PhotoImage(file='images/AddBtn.png')

        root.add_student_icon = add_teacher_icon
        root.back_icon = back_icon


        back_btn = Button(MainFrame, image=back_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr,command=show_admin_dashboard)
        back_btn.place( y=18, width=button_width, height=12)

    
    
        #-------------------BACK BUTTON ----------#


        InputFrame=Frame(MainFrame,bg='#8B8878')
        InputFrame.pack(pady=100)
        InputFrame.propagate(0)
        InputFrame.configure(width=750, height=250)  


        #Full name entry
        Fullname = Entry(InputFrame, width=25, fg="White",bg='#8B8878', border=0, font=('Microsoft YaHei UI Light', 11))
        Fullname.place(x=30, y=50)
        FullNameheading = Label(InputFrame, text="Full Name", fg='#CCCCCC', font=('Microsoft YaHei UI',9,), bg='#8B8878')
        FullNameheading.place(x=25,y=70)
        Frame(InputFrame, width=220, height=2, bg="Black").place(x=25, y=70)

        # User name entry
        Username = Entry(InputFrame, width=25, fg="White",bg='#8B8878', border=0, font=('Microsoft YaHei UI Light', 11))
        Username.place(x=300, y=50)
        UserNameheading = Label(InputFrame, text="Username", fg='#CCCCCC', font=('Microsoft YaHei UI',9,), bg='#8B8878')
        UserNameheading.place(x=300,y=70)
        Frame(InputFrame, width=220, height=2, bg="Black").place(x=300, y=70)

        # email entry
        Email = Entry(InputFrame, width=25, fg="Black",bg='#8B8878', border=0, font=('Microsoft YaHei UI Light', 11))
        Email.place(x=30, y=100)
        Emailheading = Label(InputFrame, text="Email", fg='white', font=('Microsoft YaHei UI Light',9,), bg='#8B8878')
        Emailheading.place(x=25,y=120)
        Frame(InputFrame, width=400, height=2, bg="Black").place(x=25, y=120)

        #password
        Password = Entry(InputFrame, width=25, fg="Black",bg='#8B8878', border=0, font=('Microsoft YaHei UI Light', 11))
        Password.place(x=30, y=150)
        Passwordheading = Label(InputFrame, text="Password", fg='white', font=('Microsoft YaHei UI Light',9,), bg='#8B8878')
        Passwordheading.place(x=25,y=170)
        Frame(InputFrame, width=220, height=2, bg="Black").place(x=25, y=170)

        Button(InputFrame, image=add_teacher_icon, bd=0, width=250, bg="#8B8878",activebackground='#8B8878', command=lambda: add_teacher_to_db(Fullname.get(), Username.get(), Email.get(), Password.get())).pack(side=BOTTOM)

    def add_teacher_to_db(name, username, email, password):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                query = "INSERT INTO users (name, username, email, password, role) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (name, username, email, password, 'teacher'))
                connection.commit()
                messagebox.showinfo("Success", "Teacher added successfully!")
                cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection and connection.is_connected():
                connection.close()

    def remove_teacher():
        clear_window()
        root.title("Remove Teacher")

        clear_window()
        root.title("Add Teacher")
        button_width = 128
        MainFrame=Frame(root,bg=back_ground_clr)
        MainFrame.pack()
        MainFrame.propagate(0)
        MainFrame.configure(width=1000, height=500)

        back_icon = PhotoImage(file='images/Back.png')
        root.back_icon = back_icon
        back_btn = Button(MainFrame, image=back_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr,command=show_admin_dashboard)
        back_btn.place( y=18, width=button_width, height=12)

        
        remove_icon = PhotoImage(file='images/RemoveBtn.png')
        root.remove_teacher_icon = remove_icon

        InputFrame=Frame(MainFrame,bg='#8B8878')
        InputFrame.pack(pady=100)
        InputFrame.propagate(0)
        InputFrame.configure(width=750, height=250)  

        Label(InputFrame, text="Remove Teacher", font=('Microsoft YaHei UI Light', 23, 'bold'), bg='#8B8878', fg='#57a1f8').pack(pady=20)
    
        Label(InputFrame, text="Enter Username of Teacher to remove", bg='#8B8878').pack(pady=5)
        entry_username = Entry(InputFrame, width=30, bg='white')
        entry_username.pack(pady=5)
       
        Button(InputFrame, image=remove_icon, bd=0, width=150, bg='#8B8878',activebackground='#8B8878', command=lambda: remove_teacher_from_db(entry_username.get())).pack(pady=20)

    def remove_teacher_from_db(username):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                # Start a transaction
                connection.start_transaction()
            
                # Delete from Teachers table
                query_teachers = "DELETE FROM teachers WHERE username = %s"
                cursor.execute(query_teachers, (username,))
            
                # Delete from Users table
                query_users = "DELETE FROM users WHERE username = %s AND role = 'teacher'"
                cursor.execute(query_users, (username,))
            
                # Commit the transaction
                connection.commit()
            
                if cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Teacher removed successfully!")
                else:
                    messagebox.showinfo("Error", "No teacher found with that username.")
                
                cursor.close()
        except Error as e:
            # Rollback the transaction in case of error
            if connection:
                connection.rollback()
            print("Error while connecting to MySQL", e)
        finally:
            if connection and connection.is_connected():
                connection.close()

    def add_student():
        clear_window()
        root.title("Add Student")
        button_width = 128

        MainFrame=Frame(root,bg=back_ground_clr)
        MainFrame.pack()
        MainFrame.propagate(0)
        MainFrame.configure(width=1000, height=500)
        heading = Label(MainFrame, text="Add Student", fg='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold'), bg=back_ground_clr)
        heading.place(x=350, y=5)
        #-------------------BUTTON ----------#
        back_icon = PhotoImage(file='images/Back.png')
        add_teacher_icon = PhotoImage(file='images/AddBtn.png')

        root.back_icon = back_icon
        root.add_student_icon = add_teacher_icon

        back_btn = Button(MainFrame, image=back_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr,command=show_admin_dashboard)
        back_btn.place( y=18, width=button_width, height=12)

        #-------------------BACK BUTTON ----------#


        InputFrame=Frame(MainFrame,bg='#8B8878')
        InputFrame.pack(pady=100)
        InputFrame.propagate(0)
        InputFrame.configure(width=750, height=250)  


        #Full name entry
        Fullname = Entry(InputFrame, width=25, fg="White",bg='#8B8878', border=0, font=('Microsoft YaHei UI Light', 11))
        Fullname.place(x=30, y=50)
        FullNameheading = Label(InputFrame, text="Full Name", fg='#CCCCCC', font=('Microsoft YaHei UI',9,), bg='#8B8878')
        FullNameheading.place(x=25,y=70)
        Frame(InputFrame, width=220, height=2, bg="Black").place(x=25, y=70)

        # User name entry
        Username = Entry(InputFrame, width=25, fg="White",bg='#8B8878', border=0, font=('Microsoft YaHei UI Light', 11))
        Username.place(x=300, y=50)
        UserNameheading = Label(InputFrame, text="Username", fg='#CCCCCC', font=('Microsoft YaHei UI',9,), bg='#8B8878')
        UserNameheading.place(x=300,y=70)
        Frame(InputFrame, width=220, height=2, bg="Black").place(x=300, y=70)

        # email entry
        Email = Entry(InputFrame, width=25, fg="Black",bg='#8B8878', border=0, font=('Microsoft YaHei UI Light', 11))
        Email.place(x=30, y=100)
        Emailheading = Label(InputFrame, text="Email", fg='white', font=('Microsoft YaHei UI Light',9,), bg='#8B8878')
        Emailheading.place(x=25,y=120)
        Frame(InputFrame, width=220, height=2, bg="Black").place(x=25, y=120)

        # Course entry
        Course = Entry(InputFrame, width=25, fg="White",bg='#8B8878', border=0, font=('Microsoft YaHei UI Light', 11))
        Course.place(x=300, y=100)
        CourseNameheading = Label(InputFrame, text="Course", fg='#CCCCCC', font=('Microsoft YaHei UI',9,), bg='#8B8878')
        CourseNameheading.place(x=300,y=120)
        Frame(InputFrame, width=220, height=2, bg="Black").place(x=300, y=120)


        #password
        Password = Entry(InputFrame, width=25, fg="Black",bg='#8B8878', border=0, font=('Microsoft YaHei UI Light', 11))
        Password.place(x=30, y=150)
        Passwordheading = Label(InputFrame, text="Password", fg='white', font=('Microsoft YaHei UI Light',9,), bg='#8B8878')
        Passwordheading.place(x=25,y=170)
        Frame(InputFrame, width=220, height=2, bg="Black").place(x=25, y=170)

        Button(InputFrame, image=add_teacher_icon, bd=0, width=250, bg="#8B8878",activebackground="#8B8878", command=lambda: add_student_to_db(Fullname.get(),Course.get(), Username.get(), Email.get(), Password.get())).pack(side=BOTTOM)

    def add_student_to_db(name, subject, username, email, password):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                query = "INSERT INTO users (name, subject, username, email, password, role) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (name, subject, username, email, password, 'student'))
                connection.commit()
                messagebox.showinfo("Success", "Student added successfully!")
                cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection and connection.is_connected():
                connection.close()

    def remove_student():
        clear_window()
        root.title("Remove Student")
        button_width = 128
        MainFrame=Frame(root,bg=back_ground_clr)
        MainFrame.pack()
        MainFrame.propagate(0)
        MainFrame.configure(width=1000, height=500)

        back_icon = PhotoImage(file='images/Back.png')
        root.back_icon = back_icon
        back_btn = Button(MainFrame, image=back_icon, bg=back_ground_clr, bd=0, activebackground=back_ground_clr,command=show_admin_dashboard)
        back_btn.place( y=18, width=button_width, height=12)

        
        remove_icon = PhotoImage(file='images/RemoveBtn.png')
        root.remove_student_icon = remove_icon

        InputFrame=Frame(MainFrame,bg='#8B8878')
        InputFrame.pack(pady=100)
        InputFrame.propagate(0)
        InputFrame.configure(width=750, height=250)  

        Label(InputFrame, text="Remove Student", font=('Microsoft YaHei UI Light', 23, 'bold'), bg='#8B8878', fg='#57a1f8').pack(pady=20)
    
        Label(InputFrame, text="Enter Username of Student to remove", bg='#8B8878').pack(pady=5)
        entry_username = Entry(InputFrame, width=30, bg='white')
        entry_username.pack(pady=5)
       
        Button(InputFrame, image=remove_icon, bd=0, width=150, bg='#8B8878',activebackground='#8B8878', command=lambda: remove_student_from_db(entry_username.get())).pack(pady=20)

    def remove_student_from_db(username):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                # Start a transaction
                connection.start_transaction()

                # Delete from Students table
                query_students = "DELETE FROM students WHERE username = %s"
                cursor.execute(query_students, (username,))
                students_deleted = cursor.rowcount

                # Delete from Users table
                query_users = "DELETE FROM users WHERE username = %s AND role = 'student'"
                cursor.execute(query_users, (username,))
                users_deleted = cursor.rowcount

                # Commit the transaction
                connection.commit()

                if students_deleted > 0 and users_deleted > 0:
                    messagebox.showinfo("Success", "Student removed successfully from both tables!")
                else:
                    messagebox.showinfo("Error", "No student found with that username.")

                cursor.close()
        except Error as e:
            # Rollback the transaction in case of error
            if connection:
                connection.rollback()
            print("Error while connecting to MySQL", e)
        finally:
            if connection and connection.is_connected():
                connection.close()###----------------------------------END ADMIN DASHBOARDS CODE -------------------------------###



def show_teacher_dashboard():
    root.title("Teacher Dashboard")
    Label(root, text="Welcome to the Teacher Dashboard", font=('Microsoft YaHei UI Light', 23, 'bold'), bg="white", fg='#57a1f8').pack(pady=20)

    # Placeholder buttons for teacher functionalities
    Button(root, text="Create Quiz", font=('Microsoft YaHei UI Light', 15), bg="#57a1f8", fg="white", command=create_quiz).pack(pady=10)
    Button(root, text="View Results", font=('Microsoft YaHei UI Light', 15), bg="#57a1f8", fg="white", command=view_results).pack(pady=10)
    Button(root, text="Manage Questions", font=('Microsoft YaHei UI Light', 15), bg="#57a1f8", fg="white", command=manage_questions).pack(pady=10)
    Button(root, text="Add Student", font=('Microsoft YaHei UI Light', 15), bg="#57a1f8", fg="white", command=add_student_by_teacher).pack(pady=10)

    def create_quiz():
        messagebox.showinfo("Create Quiz", "This feature is under construction.")

    def view_results():
        messagebox.showinfo("View Results", "This feature is under construction.")

    def manage_questions():
        messagebox.showinfo("Manage Questions", "This feature is under construction.")

    def add_student_by_teacher():
        clear_window()
        root.title("Add Student")

        Label(root, text="Add Student", font=('Microsoft YaHei UI Light', 23, 'bold'), bg="white", fg='#57a1f8').pack(pady=20)

        Label(root, text="Name", bg='white').pack(pady=5)
        entry_name = Entry(root, width=30, bg='white')
        entry_name.pack(pady=5)

        Label(root, text="Subject", bg='white').pack(pady=5)
        entry_subject = Entry(root, width=30, bg='white')
        entry_subject.pack(pady=5)

        Label(root, text="Username", bg='white').pack(pady=5)
        entry_username = Entry(root, width=30, bg='white')
        entry_username.pack(pady=5)

        Label(root, text="Email", bg='white').pack(pady=5)
        entry_email = Entry(root, width=30, bg='white')
        entry_email.pack(pady=5)

        Label(root, text="Password", bg='white').pack(pady=5)
        entry_password = Entry(root, width=30, show='*', bg='white')
        entry_password.pack(pady=5)

        Button(root, text="Add Student", width=20, pady=7, bg="#57a1f8", fg="white", command=lambda: add_student_to_db(entry_name.get(), entry_subject.get(), entry_username.get(), entry_email.get(), entry_password.get())).pack(pady=20)
        back_button = Button(root, text="Back", font=('Microsoft YaHei UI Light', 15), bg="#57a1f8", fg="white", command=show_teacher_dashboard)
        back_button.pack(pady=10)###----------------------------------END TEACHER DASHBOARDS CODE ----------------------------###

def show_student_dashboard():
    root.title("Student Dashboard")
    Label(root, text="Welcome to the Student Dashboard", font=('Microsoft YaHei UI Light', 23, 'bold'), bg="white", fg='#57a1f8').pack(pady=20)
    # Add more widgets and functionalities as needed

###----------------------------------END DASHBOARDS CODE -------------------------------------###


###----------------------------------AUTHENTICATION CODE  (LOGIN/SIGNIN) --------------------###
# Function to show sign-up form
def show_signup_form():
    clear_window()
    root.title("Sign Up")

    Label(root, text="Sign Up", font=('Microsoft YaHei UI Light', 23, 'bold'), bg="white", fg='#57a1f8').pack(pady=20)
    
    Label(root, text="Name", bg='white').pack(pady=5)
    entry_name = Entry(root, width=30, bg='white')
    entry_name.pack(pady=5)
    
    Label(root, text="Username", bg='white').pack(pady=5)
    entry_username = Entry(root, width=30, bg='white')
    entry_username.pack(pady=5)
    
    Label(root, text="Email", bg='white').pack(pady=5)
    entry_email = Entry(root, width=30, bg='white')
    entry_email.pack(pady=5)
    
    Label(root, text="Password", bg='white').pack(pady=5)
    entry_password = Entry(root, width=30, show='*', bg='white')
    entry_password.pack(pady=5)
    
    Button(root, text="Sign Up", width=20, pady=7, bg="#57a1f8", fg="white", command=lambda: sign_up_user(entry_name.get(), entry_username.get(), entry_email.get(), entry_password.get())).pack(pady=20)
    Button(root, text="Back to Login", width=20, pady=7, bg="#57a1f8", fg="white", command=show_login_form).pack(pady=10)

def sign_up_user(name, username, email, password):
    try:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, username, email, password, role) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (name, username, email, password, 'student'))
            connection.commit()
            messagebox.showinfo("Success", "Sign up successful!")
            cursor.close()
            show_login_form()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection and connection.is_connected():
            connection.close()

# Function to show login form
def show_login_form():
    clear_window()
    root.title('QuizBee')
    
    # Login page Image
    LoginImg = PhotoImage(file="images/login.png")
    Label(root, image=LoginImg, bg="white").place(x=50, y=50)

    # Login detail frame
    LoginFrame = Frame(root, width=350, height=350, bg="white")
    LoginFrame.place(x=500, y=50)

    heading = Label(LoginFrame, text="Sign In", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    # QuizBee Caption Frame
    CaptionFrame = Frame(root, width=950, height=350, bg="white")
    CaptionFrame.place(x=15, y=390)

    caption = Label(CaptionFrame, text="QuizBee: Smart Quizzes, For Smarter Students", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    caption.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    # Username entry
    user = Entry(LoginFrame, width=25, fg="Black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')

    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(LoginFrame, width=295, height=2, bg="Black").place(x=25, y=107)




    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        name = password.get()
        if name == '':
            password.insert(0, 'Password')

    # Password entry
    password = Entry(LoginFrame, width=25, fg="Black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11), show='*')
    password.place(x=30, y=150)
    password.insert(0, 'Password')

    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    Frame(LoginFrame, width=295, height=2, bg="Black").place(x=25, y=180)

    # Sign In button with functionality
    Button(LoginFrame, width=39, pady=7, text="Sign In", bg="#57a1f8", fg="white", border=0, command=sign_in).place(x=35, y=210)

    Button(LoginFrame, width=39, pady=7, text="Sign In", bg="#57a1f8", fg="white", border=0, command=lambda: sign_in(user, password)).place(x=35, y=210)

    root.mainloop()
###----------------------------------END AUTHENTICATION CODE  (LOGIN/SIGNIN) ----------------###


###----------------------------------TKINTER WINDOW CODE ------------------------------------###

root = Tk()
root.title('QuizBee')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.wm_iconbitmap('QuizBeeLogo.ico') 

show_login_form()