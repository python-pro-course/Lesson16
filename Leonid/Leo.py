from tkinter import *
import os
from PIL import Image, ImageTk
from time import sleep


# Classы
class Bank_ack:
    def __init__(self, log, pas, balance=0):
        self.login = log
        self.password = pas
        self.balance = balance
        self.create_user()

    def create_user(self):

        if self.login == '' or self.password == '' or self.login == ' ' or self.password == ' ':
            notif.config(text='Заполните все поля', fg='red')
        if self.login != '':
            notif.config(text='Регистрация...', fg='green')









# ФУНКЦИИ
def create_account():
    log = sign_up_login.get()
    pas = sign_up_password.get()
    Bank_ack(log, pas)

def sign_up():
    global sign_up_login
    global sign_up_password
    global notif
    sign_up_login = StringVar()
    sign_up_password = StringVar()


    sign_up_window = Toplevel(main)
    sign_up_window.title('Регистрация')
    sign_up_window.geometry('500x400')

    # Labels
    Label(sign_up_window, text='          Введите логин и пароль', font=('Calibri', 25)).grid(row=0, sticky=N, pady=10)
    Label(sign_up_window, text='      Логин: ', font=('Calibri', 15)).grid(row=1, sticky=W)
    Label(sign_up_window, text='      Пароль: ', font=('Calibri', 15)).grid(row=2, sticky=W)
    notif = Label(sign_up_window, font=('Calibri', 25))
    notif.grid(row=3, sticky=N, pady= 10)


    # Entries
    Entry(sign_up_window, textvariable=sign_up_login).grid(row=1, column=0)
    Entry(sign_up_window, textvariable=sign_up_password).grid(row=2, column=0)

    # Buttons
    Button(sign_up_window, text='Зарегистрироваться', font=('Calibri', 12), width=25, command=create_account).grid(row=4, sticky=N ,pady=10)

def login():
    sign_up_window = Toplevel(main)
    sign_up_window.title('Вход')
    sign_up_window.geometry('400x500')




# main
main = Tk()
main.title('Банк')
main.geometry('400x500')

# image
img = Image.open('image/img1.png')
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)

# Labels
Label(main, text='Самый простой банк', font=('Calibri', 25)).pack(side=TOP)
Label(main, image=img).pack(side=TOP)

# Button
Button(main, text='Регистрация', font=('Calibri', 12), width=15, command=sign_up).pack(side=TOP, pady=10)
Button(main, text='Вход', font=('Calibri', 12), width=15, command=login).pack(side=TOP, pady=10)


main.mainloop()



