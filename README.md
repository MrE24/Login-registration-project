# Login-registration-project
Easy Login project that allows a user to enter a user and a password that stores in a file which then is read to verify if it's true and lead to anything of your preference
#
import os
from tkinter import  *
screen=Tk()

def login_sucess():
    screen3 = Toplevel(screen)
    screen3.geometry("400x600")
    screen3.title("Cuenta")
    Label(screen3, text = "Login succesful").pack()





def login_verify():
    print("working...")
    username1 = username_Verify.get()
    password1 = password_Verify.get()
    user_entry2.delete(0, END)
    password_entry2.delete(0, END)
    list_o_files = os.listdir()
    if username1 in list_o_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            print("password incorrect")
    else:
        print("username not registered")
def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text="registration succesful")
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("login")
    screen2.geometry("300x250")
    Label(screen2, text = "instert details").pack()
    Label(screen2, text="").pack()

    global username_Verify
    global password_Verify
    global user_entry2
    global password_entry2
    username_Verify = StringVar()
    password_Verify = StringVar()



    Label(screen2, text="username").pack()
    user_entry2 = Entry(screen2, textvariable = username_Verify)
    user_entry2.pack()
    Label(screen2, text="password").pack()
    password_entry2 = Entry(screen2, textvariable = password_Verify)
    password_entry2.pack()
    Label(screen2, text="").pack()
    Button(screen2, text = "login", height = 1, width = 10, command = login_verify).pack()















    
def register():
    global username
    global password
    global screen1
    global username_entry
    global password_entry
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details").pack()
    Label(screen1, text="").pack()
    Label(screen1, text = "username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    Label(screen1, text ="password * ").pack()
    password_entry = Entry(screen1, textvariable = password)

    username_entry.pack()
    password_entry.pack()
    Button(screen1, text="Register", width="10", height="1", command=register_user).pack()

def main_screen():
    global screen
    screen.geometry("300x250")
    screen.title("Database")
    Label(text = "Data 1.0", bg = "grey",width = "300", height = "2", font = ("Calibri", 13)).pack()

    Button(text ="Login", width = "30", height = "2", command = login).pack()
    Label( text = "").pack()
    Button(text ="Register", width = "30", height = "2", command = register).pack()
    screen.mainloop()
main_screen()

#if Error on Verify try () at the end#


