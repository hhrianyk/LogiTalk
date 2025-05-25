from customtkinter import *

window = CTk()
window.geometry('400x300')
window.configure(fg_color='yellow')
window.title('First App')

text = CTkLabel(window, text='Hello Logika!', fg_color='blue', width=400, height=150, font=('Arial', 20, 'bold'))
text.pack()


window.mainloop()


