from customtkinter import *

win = CTk()
win.geometry('400x300')
win.title('Соціальне опитування')
def button_adaptive():
   window_width = win.winfo_width()
   btn.configure(width=window_width-120, height=win.winfo_height()/4)
   win.after(500,button_adaptive)

btn = CTkButton(win, text='Кнопка', width=300, height=100)
btn.place(x=50, y=40)

button_adaptive()

win.mainloop()