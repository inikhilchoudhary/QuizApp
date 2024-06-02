from tkinter import *
from tkinter import messagebox

# Mock database (for demonstration purposes)
users_db = {
    "teacher": {"password": "teacher123", "role": "teacher"},
    "student": {"password": "student123", "role": "student"}
}

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def sign_in():
    username = user.get()
    passwd = password.get()
    if username in users_db and users_db[username]["password"] == passwd:
        role = users_db[username]["role"]
        messagebox.showinfo("Login Success", f"Welcome {username.capitalize()}! You are logged in as a {role.capitalize()}.")
        # Clear the window and show the appropriate dashboard
        clear_window()
        if role == "teacher":
            show_teacher_dashboard()
        else:
            show_student_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

def show_teacher_dashboard():
    root.title("Teacher Dashboard")
    Label(root, text="Welcome to the Teacher Dashboard", font=('Microsoft YaHei UI Light', 23, 'bold'), bg="white", fg='#57a1f8').pack(pady=20)

    # Placeholder buttons for teacher functionalities
    Button(root, text="Create Quiz", font=('Microsoft YaHei UI Light', 15), bg="#57a1f8", fg="white", command=create_quiz).pack(pady=10)
    Button(root, text="View Results", font=('Microsoft YaHei UI Light', 15), bg="#57a1f8", fg="white", command=view_results).pack(pady=10)
    Button(root, text="Manage Questions", font=('Microsoft YaHei UI Light', 15), bg="#57a1f8", fg="white", command=manage_questions).pack(pady=10)

def create_quiz():
    messagebox.showinfo("Create Quiz", "This feature is under construction.")

def view_results():
    messagebox.showinfo("View Results", "This feature is under construction.")

def manage_questions():
    messagebox.showinfo("Manage Questions", "This feature is under construction.")

def show_student_dashboard():
    root.title("Student Dashboard")
    Label(root, text="Welcome to the Student Dashboard", font=('Microsoft YaHei UI Light', 23, 'bold'), bg="white", fg='#57a1f8').pack(pady=20)
    # Add more widgets and functionalities as needed

root = Tk()
root.title('QuizBee')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
root.wm_iconbitmap('QuizBeeLogo.ico') 

# Login page Image
LoginImg = PhotoImage(file="login.png")
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

Label(LoginFrame, text="Don't have an account?", fg="Black", bg="white", font=('Microsoft YaHei UI Light', 8)).place(x=60, y=250)
Button(LoginFrame, width=11, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8").place(x=168, y=250)

root.mainloop()
