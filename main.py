from tkinter import *
import os
from PIL import Image, ImageTk


class BankAccount:
    def __init__(self, login, password, balance=0):
        self.login = login
        self.password = password
        self.balance = balance
        self.create_user()

    def create_user(self):
        if self.login == '' or self.password == '':
            notif.config(text='Необходимо заполнить все поля', fg='red')






# Создание главного окна
main = Tk()  # Tk() - конструктор, инициализирующий окно
main.title('Банковая система')  # устанавливаем заголовок окна
main.geometry('300x300')  # устанавливаем размер окна


def create_account():

    login = s_up_login.get()
    password = s_up_pass.get()
    BankAccount(login, password)



# Содздание окна регистрации
def sign_up():
    global s_up_login
    global s_up_pass
    global notif
    s_up_login = StringVar()
    s_up_pass = StringVar()

    sign_up_screen = Toplevel(main)
    sign_up_screen.title('Sign Up')
    main.geometry('200x200')

    # Labels
    Label(sign_up_screen, text='Введите логин и пароль').grid(row=0, sticky=N, pady=10)  # row - строка
    Label(sign_up_screen, text='Login').grid(row=1, sticky=W)
    Label(sign_up_screen, text='Password').grid(row=2, sticky=W)
    notif = Label(sign_up_screen, font=('Calibri', 12))
    notif.grid(row=4, sticky=N, pady=10)

    # Entries
    Entry(sign_up_screen, textvariable=s_up_login).grid(row=1, column=1)
    Entry(sign_up_screen, textvariable=s_up_pass).grid(row=2, column=1)

    # Buttons
    Button(sign_up_screen, text='Sign In', font=('Calibri', 12), width=15, command=create_account).grid(row=3, sticky=N,
                                                                                                       pady=10)


# Создание картинки
img = Image.open('data/images/bank.PNG')
img = img.resize((170, 170))
img = ImageTk.PhotoImage(img)

# Labels
Label(main, text='Самый безопасный банк').pack(side=TOP)
Label(main, image=img).pack(side=TOP)

# Buttons
Button(main, text='Sign Up', font=('Calibri', 12), width=15, command=sign_up).pack(side=TOP, pady=10)
Button(main, text='Log In', font=('Calibri', 12), width=15).pack(side=TOP)

main.mainloop()
