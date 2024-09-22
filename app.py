from tkinter import *
import os
import tkinter
# shutdown: This is the command used to control shutdown, restart, or logoff operations in Windows.
"""
"shutdown -l":
The shutdown command is commonly used in operating systems (like Windows or Unix-based systems) to perform shutdown-related operations, 
including logging off, shutting down, or rebooting the system.
-l is a specific flag that means "log off" the current user.
"""
"""
The shutdown command (and particularly -l for logging off) is platform-dependent. 
The behavior of shutdown -l works on Windows. In Unix/Linux, there are similar commands,
 but shutdown -l wouldn’t log off the user; instead,
 you'd typically use a different command like logout or exit.
"""

# making function of all the function
def restart():
    os.system("shutdown /r /t 1")

"""
/r: This switch tells the system to "restart" instead of shutting down. Without this, 
the shutdown command would simply shut down the system.

/t 1: This option sets the time delay before the restart occurs. The number after /t is the delay in seconds. 
In this case, it is set to 1 second, meaning the system will restart 1 second after the command is issued.
"""
def Restart_time():
    os.system("shutdown /r /t 20")


def Log_Out():
    os.system("shutdown -l")


def fshutdown():
    os.system("shutdown /s /t 1")


st = Tk() #class

st.title("shutDown APP")
st.geometry("200x200")
st.config(bg="blue")
r_button = Button( #it is class
    st,
    text="Restart",
    font=("Time New Roma", 15, "bold"),
    relief=RAISED,
    cursor="plus",
    takefocus="restart",
    command=restart
)
r_button.place(x=30, y=60, height=50, width=200)
rt_button = Button(
    st,
    text="Restart time",
    font=("Time New Roma", 15, "bold"),
    relief=RAISED,
    cursor="plus",
    takefocus="restart time",
    command=Restart_time
)
rt_button.place(x=30, y=140, height=50, width=200) #function

Log_out = Button(
    st,
    text="Log Out",
    font=("Time New Roma", 15, "bold"),
    relief=RAISED,
    cursor="plus",
    takefocus="Log Out",
    command=Log_Out
)
Log_out.place(x=30, y=220, height=50, width=200)

shutDown = Button(
    st,
    text="ShutDown",
    font=("Time New Roma", 15, "bold"),
    relief=RAISED,
    cursor="plus",
 
    command=fshutdown
)
shutDown.place(x=30, y=300, height=50, width=200)

st.mainloop()
