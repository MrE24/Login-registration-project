# DEBUGGER

from tkinter import *
import os


screen = Tk()


# classes
#----------------------------------------------------------------------------------------------#


class user:
    def __init__(self, name, passw, enterprise):
        self.name = name
        self.passw = passw
        self.ent = enterprise
        self.total = self.passw+self.ent+self.name

    def verify(self):
        self.ver = self.total
        return self.ver

    def giv_name(self):
        return self.name

    def giv_passw(self):
        return self.passw

    def giv_enterprise(self):
        return self.ent


class company:
    def __init__(self, enterprise, max_users):
        self.com = enterprise
        self.max = max_users
        self.users = []

    def add_user(self, user):
        if len(self.users) < self.max:
            self.users.append(user)
            return True
        else:
            print("Maximum number of users on local device")
            return False


# variables/ent/usr/passw
#----------------------------------------------------------------------------------------------#
usr1 = user("admin",  "admin123", "EG.co")
usr2 = user("Tim", "21/1/98", "EG.co.as")
usr3 = user("John", "cat222", "EG.co.as")
usr4 = user("Martin", "green2apple", "EG.co.as")
usr5 = user("Stewart", "war999", "Opl.inc")
usr6 = user("Barnes", "smartcookie111", "Opl.inc")
usr7 = user("Namba", "LOLOLOL71",  "Opl.inc")


EGco = company("EG.co", 1)
EGcoas = company("Eg.co.as", 4)
OPl = company("Opl.inc", 4)
#-----------------------------------------------------------------------------------------------#


def login_verify():
    global user1
    global pass1
    global comp1
    user1 = box1.get()
    pass1 = box2.get()
    comp1 = box3.get()
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    ent_entry.delete(0, END)
    a = user1
    b = pass1
    c = comp1
    new_usr = user(a, b, c)
    if new_usr.verify() == usr1.verify() or usr2.verify() or usr3.verify() or usr4.verify() or usr5.verify() or usr6.verify() or usr7.verify():
        print("SUCCESFUL")
    elif new_usr.name != usr1.name or usr2.name or usr3.name or usr4.name or usr5.name or usr6.name or usr7.name:
        print(" error_message_name()  ")
    elif new_usr.passw != usr1.passw or usr2.passw or usr3.passw or usr4.passw or usr5.passw or usr6.passw or usr7.passw:
        print(" error_message_passw()  ")
    elif new_usr.ent != usr1.ent or usr2.ent or usr3.ent or usr4.ent or usr5.ent or usr6.ent or usr7.ent:
        print(" error_message_ent()  ")
    else:
        "ERROR!"


def enter_user():
    global screen1
    global box1, box2, box3, user_entry, pass_entry, ent_entry

    screen1 = Toplevel(screen)
    screen1.title("User-registration")
    screen1.geometry("300x250")
    Label(screen1, text="Instert details", bg="grey").pack()
    Label(screen1, text="")
    Label(screen1, text="")
    box1 = StringVar()
    box2 = StringVar()
    box3 = StringVar()

    Label(screen1, text="user").pack()
    user_entry = Entry(screen1, textvariable=box1)
    user_entry.pack()
    Label(screen1, text="password").pack()
    pass_entry = Entry(screen1, textvariable=box2)
    pass_entry.pack()
    Label(screen1, text="enterprise").pack()
    ent_entry = Entry(screen1, textvariable=box3)
    ent_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="login", height="2",
           width="10", command=login_verify).pack()


def main_screen():
    global screen
    screen.geometry("300x250")
    screen.title("Clss-app")
    Label(text="Data 1.1", bg="grey", width="300",
          height="2", font=("Calibri", "13")).pack()
    Label(text="").pack()

    Button(text="Enter", width="30", height="2", command=enter_user).pack()

    screen.mainloop()


main_screen()
