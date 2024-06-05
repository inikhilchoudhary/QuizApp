from tkinter import *
root=Tk()
root.geometry('500x400')
'''
menu_bar_color='#383838'

#icon
toggle_icon=PhotoImage(file='Images/toggle_btn_icon.png')
user_icon=PhotoImage(file='Images/User.png')
teacher_icon=PhotoImage(file='Images/Teacher.png')
student_icon=PhotoImage(file='Images/Students.png')
exit_icon=PhotoImage(file='Images/Exit.png')

#switch indicator
def switch_indicator(indicator_lb):
    user_btn_indicator.config(bg=menu_bar_color)
    students_btn_indicator.config(bg=menu_bar_color)
    teacher_btn_indicator.config(bg=menu_bar_color)
    exit_btn_indicator.config(bg=menu_bar_color)
    indicator_lb.config(bg='white')



menu_bar_frame=Frame(root,bg=menu_bar_color)

toggle_menu_btn=Button(menu_bar_frame,image=toggle_icon,bg=menu_bar_color,bd=0,activebackground=menu_bar_color)
toggle_menu_btn.place(x=4,y=10)

user_btn=Button(menu_bar_frame,image=user_icon,bg=menu_bar_color,bd=0,activebackground=menu_bar_color,command= lambda:switch_indicator(indicator_lb=user_btn_indicator))
user_btn.place(x=9,y=130,width=30,height=40)

teacher_btn=Button(menu_bar_frame,image=teacher_icon,bg=menu_bar_color,bd=0,activebackground=menu_bar_color,command= lambda:switch_indicator(indicator_lb=teacher_btn_indicator))
teacher_btn.place(x=9,y=250,width=30,height=40)

students_btn=Button(menu_bar_frame,image=student_icon,bg=menu_bar_color,bd=0,activebackground=menu_bar_color,command= lambda:switch_indicator(indicator_lb=students_btn_indicator))
students_btn.place(x=9,y=190,width=30,height=40)

exit_btn=Button(menu_bar_frame,image=exit_icon,bg=menu_bar_color,bd=0,activebackground=menu_bar_color,command= lambda:switch_indicator(indicator_lb=exit_btn_indicator))
exit_btn.place(x=9,y=310,width=30,height=40)
#same other buttons 

#now indicator of active 
user_btn_indicator=Label(menu_bar_frame,bg='white')
user_btn_indicator.place(x=3,y=130,width=3,height=40)

students_btn_indicator=Label(menu_bar_frame,bg=menu_bar_color)
students_btn_indicator.place(x=3,y=190,width=3,height=40)

teacher_btn_indicator=Label(menu_bar_frame,bg=menu_bar_color)
teacher_btn_indicator.place(x=3,y=250,width=3,height=40)

exit_btn_indicator=Label(menu_bar_frame,bg=menu_bar_color)
exit_btn_indicator.place(x=3,y=310,width=3,height=40)


menu_bar_frame.pack(side=LEFT,fill=Y,padx=3,pady=4)
menu_bar_frame.pack_propagate()

menu_bar_frame.configure(width=45)

'''


options_frames=Frame(root,bg="red")


options_frames.pack(side=LEFT)
options_frames.propagate(False)
options_frames.configure(width=100,height=400)

main_frame=Frame(root,highlightbackground="black",highlightthickness=2)


main_frame.pack(side=LEFT)
main_frame.propagate(False)
main_frame.configure(height=400,width=500)


root.mainloop()

