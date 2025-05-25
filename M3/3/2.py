from customtkinter import *
from PIL import Image, ImageFilter, ImageEnhance

win = CTk()
win.geometry('600x500')
set_default_color_theme('green')

image = Image.open('3.png')
image_ctk = CTkImage(light_image=image, size=(350, 200))


label_img = CTkLabel(win, text='', image=image_ctk)
label_img.pack(pady=100)


set_frame = CTkFrame(win)
set_frame.pack(side='bottom', pady=20)

btn_rotate = CTkButton(set_frame, text='Повернти на 90')
btn_rotate.grid(row=0, column=0, padx=10)

btn_l = CTkButton(set_frame, text='ЧБ' )
btn_l.grid(row=0, column=1, padx=10)


btn_blur = CTkButton(set_frame, text='Розмиття')
btn_blur.grid(row=0, column=2, padx=10)

label = CTkLabel(set_frame, text='Контраст')
label.grid(row=1, column=1)

slide_enchance = CTkSlider(set_frame, from_=0, to=100 )
slide_enchance.grid(row=2, column=1, pady=5)



win.mainloop()

