from customtkinter import *
from random import *


def show_diff_pass(value):
   global diff_password
   diff_password = int(value)
   count_password_chars_label.configure(text=f'{int(value)}')
   generate_password()




def generate_password():
   global diff_password
   chars = [char for char in 'qwertyuiopasdfghjklzxcvbnm']
   spec_chars = [char for char in '!@#$%^&*()_+']
   available_value = []
   result = ''
   if l_chars_btn.get():
       available_value += chars
   if up_chars_btn.get():
       available_value += [char.upper() for char in chars]
   if spec_chars_btn.get():
       available_value += spec_chars
   if number_chars_btn.get():
       available_value += [str(i) for i in range(0, 10)]


   for i in range(diff_password):
       result += choice(available_value)


   password_entry.delete(0, 'end')
   password_entry.insert(0, result)


diff_password = 4
window = CTk()
window.geometry("400x300")
window.maxsize(400, 300)
window.title('GP')


set_appearance_mode('dark')
set_default_color_theme('green')


password_entry = CTkEntry(window, width=220)
password_entry.grid(row=0, column=0, padx=10, pady=10)


btn_generate = CTkButton(window, text='Generate', command=generate_password)
btn_generate.grid(row=0, column=1, padx=10)


settings_frame_left = CTkFrame(window, width=200)
settings_frame_left.grid(row=1, column=0)


l_chars_btn = CTkCheckBox(settings_frame_left, text='Малі літери', width=220)
l_chars_btn.pack(pady=5)


up_chars_btn = CTkCheckBox(settings_frame_left, text='Великі літери', width=220)
up_chars_btn.pack(pady=5)


spec_chars_btn = CTkCheckBox(settings_frame_left, text='Спеціальні символи', width=220)
spec_chars_btn.pack(pady=5)


number_chars_btn = CTkCheckBox(settings_frame_left, text='Числа', width=220)
number_chars_btn.pack(pady=5)


# права сторона
settings_frame_right = CTkFrame(window)
settings_frame_right.grid(row=1, column=1)


count_password_chars_slider = CTkSlider(settings_frame_right, from_=4, to=64, orientation='vertical', command=show_diff_pass)
count_password_chars_slider.pack(side='right')


count_password_chars_label = CTkLabel(settings_frame_right, text='4', width=80)
count_password_chars_label.pack(side='left', padx=20)


window.mainloop()
