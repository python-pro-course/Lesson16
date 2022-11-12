from tkinter import *
import os
from PIL import Image, ImageTk

# Создание главного окна
main = Tk()  # Tk() - конструктор, инициализирующий окно
main.title('Банковая система')  # устанавливаем заголовок окна
main.geometry('300x300')  # устанавливаем размер окна


# Содздание окна регистрации
def sign_up():
    sign_up_screen = Toplevel(main)
    sign_up_screen.title('Sign Up')
    main.geometry('200x200')

    # Labels
    Label(sign_up_screen, text='Введите логин и пароль').grid(row=0, sticky=N, pady=10)  # row - строка
    Label(sign_up_screen, text='Login').grid(row=1, sticky=W)
    Label(sign_up_screen, text='Password').grid(row=2, sticky=W)




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
