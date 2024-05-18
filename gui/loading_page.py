from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.ttk as ttk
from tkinter import Canvas
import sys
# import login_page 


window = Tk()
window.resizable(False, False)

height = 430
width = 530
#window places at center
x = (window.winfo_screenwidth()//2)-(width//2)
y = (window.winfo_screenheight()//2)-(height//2)
window.geometry('{}x{}+{}+{}'.format(width,height,x,y))
window.wm_attributes('-topmost', True)
#to make the window transparent 
# window.wm_attributes('-alpha', 0.9)
#-----------------------------------------------------------------

#removes the windows style
window.overrideredirect(1)
window.config(background='black')


exit_bttn = Button(
    window, text='X',
    command=lambda: exit_window(), 
    font=("yu gothic ui", 13, 'bold'), 
    fg='#16A69C',
    bg='black',
    bd=0,
    activebackground='black')

exit_bttn.place(x=502, y=0)

welcome_label = Label(
    window,
    text='WELCOME!',
    bg='black',
    fg='#16A69C',
    font=('CenturyGothic', 20,)
)
welcome_label.place(x=200, y=40)
image = PhotoImage(file='../venv/images/hex_chat1.png')
bg_label =Label(window, image=image, bg='black')
bg_label.place(x=160, y=100)

progress_label = Label(
    window,
    text="Please Wait....",
    font=('CenturyGothic', 13),
    bg='black',
    fg='#16A69C'
)
progress_label.place(x=210, y=350)
s = ttk.Style()
s.theme_use('clam')
s.configure("TProgressbar", background='#16A69C', throughcolor='#16A69C')

progress = Progressbar(window, orient=HORIZONTAL, length=500, mode='determinate', style='TProgressbar')
progress.place(x=15, y=380)


def exit_window():
    sys.exit(window.destroy())


# def top():
#     win = Toplevel()
#     login_page.LoginForm(win)
#     window.withdraw()
#     win.deiconify()

i = 0

def load():
    global i

    if i<=10:
        txt = 'Please Wait....' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(200, load)
        progress['value'] = 10*i
        i += 1
    else:
        window.destroy()
        return 0
        
        



a = load()
# # print(a)
window.mainloop()
    






