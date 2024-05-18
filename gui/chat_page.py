from tkinter import *
from PIL import ImageTk, Image
from tkinter import Canvas
import tkinter.ttk as ttk
# import PlaceHolder as t
from datetime import datetime
from common.user import User
from core.ServerConnection import Serverconnection
# import TxtPlaceHolder as tp

class ChatPage():
    global entry_2
    def __init__(self, window):
        window = Tk()
        self.window = window
        # self.parent = parent
        self.height = 600
        self.width = 950
        #window places at center
        self.x = (self.window.winfo_screenwidth()//2)-(self.width//2)
        self.y = (self.window.winfo_screenheight()//2)-(self.height//2)
        self.window.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
        self.window.config(background='black')
        self.window.resizable(False, False)
        self.window.title('HEX Chat 1.0')
        
        self.canvas = Canvas(self.window, bg = "#000000",height = 600,width = 950,bd = 0, highlightthickness = 0, relief = "ridge")

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(0.0, 0.0, 100.0, 600.0, fill="#16A69C", outline="")
    
        #=============================Logo=============================

        # image_image_1 = Image.open("images/image_2.png")
        # photo0 = ImageTk.PhotoImage(image_image_1)
        # self.logo_label = Label(self.window, image=photo0, bg='black')
        # self.logo_label.image = photo0
        # self.logo_label.place(x=610, y=20)
        # image_1 = self.canvas.create_image(775.0,66.0,image=image_image_1)
        
        #=============================Enter Channel========================
    
        
        entry_image_1 = Image.open('../venv/images/e1.png')
        photo1 = ImageTk.PhotoImage(entry_image_1)
        self.entry_1_label = Label(self.window, image=photo1, bg='black')
        self.entry_1_label.image = photo1
        self.entry_1_label.place(x=595, y= 20)
        self.entry_1 = Entry(self.canvas,bd=0, bg="#D9D9D9", fg="#7E7E7D", highlightthickness=0, font=('Gill Sans MT', 14))
        self.entry_1.place(x=607, y=24, height=25)
        
        #============================Submit Button=======================

        button_image_1 = Image.open('../venv/images/b1.png')
        photo2 = ImageTk.PhotoImage(button_image_1)
        self.button_1_label = Label(self.canvas, image=photo2, bg='black')
        self.button_1_label.image = photo2
        self.button_1_label.place(x=820, y=20)
        self.button_1 = Button(self.canvas, borderwidth=0, highlightthickness=0, command=lambda: print(self.entry_1.get()), bg='#16A69C',
        text='Subscribe',font=('Gill Sans MT', 14),  fg='white', activebackground='#16A69C')
        self.button_1.place(x=838.0, y=23.0, width=80.0, height=26)

        #==========================Horizontal And vertical Line===========

        self.canvas.create_rectangle(99.0,50.0,579.9951782226562,51.50003051757812,fill="#FFFFFF",outline="")
        self.canvas.create_rectangle(582.0,0,580.0,680.0,fill="#F5F5F5",outline="")

        #=========================Text Box For Message Input===============

        # entry_image_2 = Image.open('images/e2.png')
        # photo3 = ImageTk.PhotoImage(entry_image_2)
        # self.entry_2_label = Label
        # # self.entry_2_field = StringVar()
        self.entry_2 = Text(self.canvas, bd=0, bg="#D9D9D9",fg="black",highlightthickness=0, font=('Gill Sans MT', 19))
        
        self.entry_2.place(x=100.0,y=560.0,width=350,height=40)
        self.entry_2.bind("<Return>", self.sent_message)
        #===============================Send Button=============================
        
        # button_image_2 = PhotoImage(file='images/b2.png')
        # self.button_bg_2 = self.canvas.create_image(507,579.0,image=button_image_2)
        self.button_2 = Button(self.canvas, text='SEND',font=('Gill Sans MT', 18),fg='white',borderwidth=0,highlightthickness=0,
        command=self.sent_message,relief="flat", bg='#16A69C', activebackground='#16A69C')
        self.button_2.place(x=451.0,y=560.0,width=128,height=40)

        self.canvas.create_rectangle(580.0,303.0,950.0,304.0,fill="#F5F5F5",outline="")
        self.canvas.create_rectangle(580.0,358.0,950.0,359.0,fill="#F5F5F5",outline="")
        self.canvas.create_rectangle(580.0,477.0,950.0,478.0,fill="#FFFFFF",outline="")
    
        #=============================Chat Window================================
      
        self.frame = Frame()
        self.frame.place(x=100, y=52, width=480, height=510)
        self.canvas1 = Canvas(self.frame, bg='#121212', highlightthickness=0)
        self.scrollable_frame = Frame(self.canvas1, bg='#121212')
        self.scrollable_window = self.canvas1.create_window((0,0), window=self.scrollable_frame, anchor='nw')

        def configure_scroll_region(e):
            self.canvas1.configure(scrollregion=self.canvas1.bbox('all'))

        def resize_frame(e):
            self.canvas1.itemconfig(self.scrollable_window, width=e.width)

        self.scrollable_frame.bind("<Configure>", configure_scroll_region)
        self.canvas1.configure(scrollregion=self.canvas1.bbox('all'))
        self.scrollbar = ttk.Scrollbar(self.frame, command=self.canvas1.yview, orient=VERTICAL)
        self.canvas1.config(yscrollcommand=self.scrollbar.set)
        self.canvas1.yview_moveto(1.0)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas1.bind("<Configure>", resize_frame)
        self.canvas1.pack(fill="both", expand=True)


        #========================== Time/Name Label =============================

        self.m_frame = Frame(self.scrollable_frame, bg="#d9d5d4")

        self.t_label = Label(self.m_frame, bg="#d9d5d4", text=datetime.now().strftime('%H:%M'), font=('Gill Sans MT', 14))
        self.t_label.pack()#x=10,y=20, height=20, width=440
        self.user = User.get_name()
        self.m_label = Label(self.m_frame, wraplength=250, text=f"Happy Chatting {self.user}",
                           font=('Gill Sans MT', 14), bg="#16A69C", width=43)
        self.m_label.pack(fill="x")#x=10, y=40, width=440, height=25
        self.m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")
        # self.canvas.pack(fill="both", expand=True)


        # t = vm.threading.Thread(target=self.receive_data)
        # # t.setDaemon(True)
        # t.start()


        

    def sent_message(self,event=None):
        self.message = self.entry_2.get('1.0', 'end-1c')
        Serverconnection.on_sendMessage(User.fname+":> "+self.message)
        print(self.message)
        if self.message:
            if event:
                self.message = self.message.strip()
            self.entry_2.delete('1.0', 'end-1c')

            self.m_frame = Frame(self.scrollable_frame, bg="#121212")
            self.m_frame.columnconfigure(0, weight=1)
            self.user = User.get_nickname()
            self.t_label = Label(self.m_frame, bg="#121212", fg="white", text=datetime.now().strftime('%H:%M') + ' : ' + self.user,
                               font="lucida 7 bold", justify="right", anchor="e")
            self.t_label.grid(row=0, column=0, padx=2, sticky="e")
            self.n_label = Label(self.m_frame, bg="#121212", fg="white", text=self.user,
                               font="lucida 7 bold", justify="right", anchor="e")
            self.n_label.grid(row=0, column=0, padx=4, pady=1, sticky="e")
            
            self.m_label = Label(self.m_frame, wraplength=250, text=self.message, fg="black", bg="#16A69C",
                               font="lucida 9 bold", justify="left",
                               anchor="e")
            self.m_label.grid(row=1, column=0, padx=2, pady=2, sticky="e")
            self.i_label = Label(self.m_frame, bg="#595656")
            self.i_label.grid(row=0, column=1, rowspan=2, sticky="e")
            self.m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")
            self.canvas1.update_idletasks()
            self.canvas1.yview_moveto(1.0)

        # def recieve_data(self):
        #     while True:
        #         message = self.publish
        #         data_packet = Serverconnection.on_msg(message)
        #         self.recieve_message(data_packet)


    def recieve_message(self, msg):
        message = msg

        self.m_frame = Frame(self.scrollable_frame, bg="#121212")

        # self.message = Serverconnection.on_sendMessage(self.publish)
        # print('recieved')

        self.m_frame.columnconfigure(1, weight=1)

        self.t_label = Label(self.m_frame, bg="#121212", fg="white", text=datetime.now().strftime('%H:%M'),
                             font="lucida 7 bold",
                             justify="left", anchor="w")
        self.t_label.grid(row=0, column=1, padx=2, sticky="w")

        self.m_label = Label(self.m_frame, wraplength=250, fg="black", bg="#16A69C", text=message,
                             font="lucida 9 bold",
                             justify="left",
                             anchor="w")
        self.m_label.grid(row=1, column=1, padx=2, pady=2, sticky="w")

        self.i_label = Label(self.m_frame, bg="#595656")
        # self.i_label.image = im
        self.i_label.grid(row=0, column=0, rowspan=2)

        self.m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    # self.window.mainloop()
        
   



