from tkinter import *
from login_form import LoginForm
import loading_page as lp


def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()


# def page2():
#     window = Tk()
#     ChatPage(window)
#     window.mainloop()

if __name__ == '__main__':
    if lp.a == None:
        page()
        # page2()

        # elif phase == 2:
        #     page()
