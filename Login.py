from tkinter import *
from tkinter import messagebox
#------------------------------------------------------------------------------------------------------------
root=Tk()
root.title('QuizBee')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
root.wm_iconbitmap('QuizBeeLogo.ico') 

#------------------------------------------------------------------------------------------------------------
#Login page Image
LoginImg=PhotoImage(file="login.png")
Label(root,image=LoginImg,bg="white").place(x=50,y=50)
#------------------------------------------------------------------------------------------------------------
#Login detail frame
LoginFrame=Frame(root,width=350,height=350,bg="white")
LoginFrame.place(x=500,y=50)

heading=Label(LoginFrame,text="Sign In",fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
#-----------------------------------------------------------------------------------------------------------------
#username entry
user=Entry(LoginFrame,width=25,fg="Black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
Frame(LoginFrame,width=295,height=2,bg="Black").place(x=25,y=107)
#password entry
password=Entry(LoginFrame,width=25,fg="Black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
password.place(x=30,y=150)
password.insert(0,'Password')
Frame(LoginFrame,width=295,height=2,bg="Black").place(x=25,y=180)

Button(LoginFrame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg="white",border=0).place(x=35,y=210)

Label(LoginFrame,text="Dont have an account?",fg="Black",bg="white",font=('Microsoft YaHei UI Light',8)).place(x=50,y=250)
#-----------------------------------------------------------------------------------------------------------------
root.mainloop()