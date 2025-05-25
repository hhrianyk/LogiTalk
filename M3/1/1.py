from customtkinter import *

window = CTk()
window.title('Task2')
window.geometry("400x400")

text_field = CTkTextbox(window, width=380, height=280)
text_field.pack(pady=10)

text_entry = CTkEntry(window, width=380)
text_entry.pack(pady=10)

btn = CTkButton(window, text='Клік', width=380)
btn.pack()

window.mainloop()