from customtkinter import *
win = CTk()

win.geometry('400x400')
win.title('Clicker')
font = ('Arial', 30, 'bold')

score = 0
score_text = CTkLabel(win, text=f'{score}', font=font)
score_text.pack(pady=15)

def click():
    global score
    score += 1
    score_text.configure(text=f"{score}")

click_btn = CTkButton(win, text='click', width=300, height=300, font=font, command=click)
click_btn.pack()
win.mainloop()

