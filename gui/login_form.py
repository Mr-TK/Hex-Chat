from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import Canvas
from tkinter import FLAT
import os
# import PlaceHolder as t
from common.user import User
from gui.chat_page import ChatPage
from core.ServerConnection import Serverconnection
from common.Variables_Modules import MyChat
# import TxtPlaceHolder as tp


class LoginForm:
    def __init__(self, window):
        self.window = window
        self.height = 600
        self.width = 950
        #window places at center
        self.x = (self.window.winfo_screenwidth()//2)-(self.width//2)
        self.y = (self.window.winfo_screenheight()//2)-(self.height//2)
        self.window.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
        self.window.config(background='black')
        self.window.title('HEX Chat 1.0')
        self.window.resizable(False, False)
        # self.lgn_frame = Frame(self.window, bg='black')

        #logo code
        self.side_logo = Image.open('../venv/images/image_1.png')
        photo = ImageTk.PhotoImage(self.side_logo)
        self.side_logo_label = Label(self.window, image=photo, bg='black')
        self.side_logo_label.image = photo
        self.side_logo_label.place(x=70, y=40)
        
        #left image code
        self.side_image = Image.open('../venv/images/ci2.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.window, image=photo, bg='black')
        self.side_image_label.image = photo
        self.side_image_label.place(x=50, y=190)

        # profile image code
        # self.profile_image = Image.open('images\\pro.png')
        # photo = ImageTk.PhotoImage(self.profile_image)
        # self.profile_image_label = Label(self.window, image=photo, bg='black')
        # self.profile_image_label.image = photo
        # self.profile_image_label.place(x=630, y=90)

        self.login_bttn = PhotoImage(file='../venv/images/pro1.png')
        self.img_label = Label(image=self.login_bttn)
        # self.img_label.place(x=630, y=90)
        self.my_button = Button(self.window, image=self.login_bttn, command=self.profile_photo, bg='black', bd=0,
         borderwidth=0, activebackground='black')
        self.my_button.place(x=630,y=90)

        # my_label = Label(self.window, text="")
        # my_label.pack(pady=20)

        self.sign_in_label = Label(self.window, text='Sign In', bg='black', fg='white', 
        font=("Ebrima Bold", 20))
        self.sign_in_label.place(x=635, y=200)

        #============First Name=======================

        # first name
        self.first_name = Label(self.window, text='First Name', bg='black', fg='#4f4e4d',
                                font=("Ebrima Bold", 12))
        self.first_name.place(x=530, y=275)
        # input inside first name
        self.first_name_entry = Entry(self.window, highlightthickness=0,
                                      relief=FLAT, bg='black', fg='#6b6a69', font=("Ebrima Bold", 12))
        self.first_name_entry.focus()
        self.first_name_entry.configure(bg='black', insertbackground='#1ABCA6')
        self.first_name_entry.place(x=560, y=300, width=270)
        # line in the first name
        self.first_name_line = Canvas(self.window, width=300, height=2.0, bg='white', highlightthickness=0, )
        self.first_name_line.place(x=530, y=325)

        #===================Last Name==================

        self.last_name = Label(self.window, text='Last Name', bg='black', fg='#4f4e4d',
                               font=("Ebrima Bold", 12))
        self.last_name.place(x=530, y=350)
        # input
        self.last_name_entry = Entry(self.window, highlightthickness=0,
                                     relief=FLAT, bg='black', fg='#6b6a69', font=("Ebrima Bold", 12))
        self.first_name_entry.bind("<Return>", lambda funct1: self.last_name_entry.focus())
        self.last_name_entry.configure(bg='black', insertbackground='#1ABCA6')
        self.last_name_entry.place(x=560, y=380, width=265)
        # line in the last name
        self.last_name_line = Canvas(self.window, width=300, height=2.0, bg='white', highlightthickness=0, )
        self.last_name_line.place(x=530, y=405)

        #==================Nickname========================

        self.nick_name = Label(self.window, text='Nickname', bg='black', fg='#4f4e4d',
                               font=("Ebrima Bold", 12))
        self.nick_name.place(x=530, y=430)

        self.nick_name_entry = Entry(self.window, highlightthickness=0,
                                     relief=FLAT, bg='black', fg='#6b6a69', font=("Ebrima Bold", 12))
        self.last_name_entry.bind("<Return>", lambda funct1: self.nick_name_entry.focus())
        self.nick_name_entry.configure(bg='black', insertbackground='#1ABCA6')
        self.nick_name_entry.place(x=560, y=460, width=265)
        self.nick_name_line = Canvas(self.window, width=300, height=2.0, bg='white', highlightthickness=0, )
        self.nick_name_line.place(x=530, y=485)

        #======================Connect Button======================
        
        self.cnct_bttn = Image.open('../venv/images/button_1.png')
        photo = ImageTk.PhotoImage(self.cnct_bttn)
        self.cnct_bttn_label = Label(self.window, image=photo, bg='black')
        self.cnct_bttn_label.image = photo
        self.cnct_bttn_label.place(x=550, y=520)
        self.cnct_bttn = Button(self.window, text='CONNECT', font=("Ebrima Bold", 12),
        width=23, bd=0, bg='#16A69C', cursor='hand2', activebackground='#16A69C', fg='white',
        command=lambda: self.connect_action(window))
        self.cnct_bttn.place(x=562, y=524)
        if self.cnct_bttn == 0:
            self.window.destroy()

        # self.window = window
        # self.window.geometry('950x600')
        # self.window.resizable(False, False)
        # self.window.state('zoomed')

    def profile_photo(self):
        self.image_path = filedialog.askopenfilename()
        image_name = os.path.basename(self.image_path)
        self.image_extension = image_name[image_name.rfind('.')+1:]

        if self.image_path:
            user_image = Image.open(self.image_path)
            user_image = user_image.resize((100, 100), Image.ANTIALIAS)
            user_image.save('resized'+image_name)
            user_image.close()

            self.image_path = 'resized'+image_name
            user_image = Image.open(self.image_path)

            user_image = ImageTk.PhotoImage(user_image)
            self.img_label = Label(self.window)
            self.img_label.place(x=630, y=90)
            self.img_label.image = user_image
            self.img_label.config(image=user_image)
# ============== Initial Loading ends Here ================================


    def connect_action(self, window):
        # saving the user information
        print("in the login", self.nick_name_entry.get())
        User.set_nickname(self.nick_name_entry.get())
        User.set_fname(self.first_name_entry.get())
        User.set_lname(self.last_name_entry.get())

        #creating the mqtt connection
        Serverconnection.MQTTConnect(User.get_nickname())

        #closing the login window and opening the chat window
        self.window.destroy()
        MyChat(self)
        MyChat.get_chat()



