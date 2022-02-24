from tkinter import *
import random
import string
import pyperclip
import os

root = Tk()
pass_str = StringVar()
root.geometry('410x500')
root.resizable(0,0)
root.title('Password Manager')
root.config(bg='lavender')
Label(root, text="PASSWORD MANAGER",font='arial 15 bold italic',bg='lavender').pack(pady=20)

pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 italic',bg='lavender').pack()
pass_len = IntVar()
Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=20, font="arial 10 italic").pack()

pass_str = StringVar()
password_b = StringVar()
username = StringVar()
topic = StringVar()
p1 = StringVar()
p2 = StringVar()
password_global = StringVar()


def generator():

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits)

    for y in range(pass_len.get()-4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    pass_str.set(password)


Button(root, text="GENERATE PASSWORD", command=generator,bg='azure').pack(pady=20)

Entry(root, textvariable=pass_str).pack()


def copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text='COPY TO CLIPBOARD', command=copy_password).pack(pady=20)
Label(root, text='Website/App Name',bg='lavender').pack()
Entry(root,textvariable=topic).pack()


def sign_up():
    up = Toplevel(root)
    up.geometry('250x300')
    up.config(bg='lavender')
    up.resizable(0,0)
    print("User registration in process... ")
    Label(up, text="Please enter details below",bg='lavender').pack()
    Label(up, text="Username",bg='lavender').pack(pady=20)
    username_entry = Entry(up)
    username_entry.pack()
    Label(up,text='Password',bg='lavender').pack(pady=20)
    password_entry = Entry(up,textvariable=password_b, show='*')
    password_entry.pack()

    def registration():
        username_info = username_entry.get()
        password_info = password_entry.get()
        file = open((username_info)+'.txt', "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        file.close()
        Label(up, text="Registration Success", fg="green", font=("calibri", 11),bg='lavender').pack()

    register_button = Button(up,text='Register',command=registration).pack(pady=20)


def login_screen():
    logging_screen = Toplevel(root,bg='alice blue')
    logging_screen.title('Login')
    logging_screen.geometry('200x225')
    logging_screen.resizable(0,0)
    logging_screen.config(bg='lavender')
    Label(logging_screen,text="Please enter details below", bg="lavender").pack()
    Label(logging_screen,text="Username", bg="lavender").pack()
    username_login = Entry(logging_screen)
    username_login.pack()
    Label(logging_screen, text='Password', bg='lavender').pack(pady=20)
    password_entry = Entry(logging_screen, textvariable=password_global, show='*')
    password_entry.pack()

    def login():
        username_a = username_login.get()
        password_a = password_global.get()
        files_list = os.listdir()
        if (username_a+'.txt') in files_list:
            my_file = open(username_a+'.txt',"a+")
            file3 = open(username_a + '.txt', "r")
            verify = file3.read().splitlines()
            if password_a in verify:
                print(username_a + str(' found'))
                print(pass_str.get() + '= password generated')
                my_file.write('-----------------------'+'\n')
                my_file.write(topic.get()+'\n')
                my_file.write(pass_str.get() + '\n')
                my_file.write('-----------------------'+'\n')
                my_file.close()

    Button(logging_screen,text='Login',command=login).pack(pady=20)


def save_password():
    print(pass_str.get())
    up = Toplevel(root)
    up.title("")
    up.geometry("200x200")
    up.resizable(0,0)
    Button(up,text='New User', command=sign_up).pack(pady=20)
    Button(up, text='Existing User', command=login_screen).pack(pady=20)


def view_saved_passwords():
    sps = Toplevel(root,bg='alice blue')
    sps.geometry("250x200")
    sps.resizable(0,0)
    sps.title('Login')
    Label(sps, text="Username", bg="lavender").pack(pady=5)
    username_login = Entry(sps)
    username_login.pack(pady=5)
    Label(sps, text="Password", bg="lavender").pack(pady=5)
    username_password = Entry(sps)
    username_password.pack(pady=5)

    def go():
        username_a = username_login.get()
        password_a = username_password.get()
        filename = username_login.get() + '.txt'
        files_list = os.listdir()
        if filename in files_list:
            file1 = open(filename)
            verify = file1.read().splitlines()
            print(verify)
            if password_a in verify:
                count = 0
                xyz = Toplevel(root, bg='alice blue')
                xyz.resizable(0,0)
                mylist = Listbox(xyz)
                scrollbar = Scrollbar(xyz, orient=VERTICAL, command=mylist.yview)
                mylist.config(yscrollcommand=scrollbar.set)
                scrollbar.pack(side=RIGHT, fill=Y)
                mylist.pack(side=LEFT, fill=BOTH, expand=True)
                with open(filename) as fp:
                    while True:
                        count += 1
                        line = fp.readline()
                        if not line:
                            break
                        print("Line{}: {}".format(count, line.strip()))
                        mylist.insert(END, line + '\n')

    Button(sps,text='Proceed',command=go).pack()
    sps.title('Passwords')


Button(root, text='Save', command=save_password).pack(pady=20)
Button(root, text='Saved Passwords', command=view_saved_passwords).pack()
root.mainloop()