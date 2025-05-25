from customtkinter import *
from PIL import Image, ImageFilter, ImageEnhance

img = Image.open("3.png")
enhancer = ImageEnhance.Contrast(img)
image = enhancer.enhance(0.5).show()
img.filter(ImageFilter.EMBOSS  ).show()

ImageEnhance.Contrast(img).enhance(0.0).show()

window = CTk()
window.geometry("400x300")
window.maxsize(400, 300)

CTK_img = CTkImage(img, size=(100,400))

lable  =CTkLabel(window,image= CTK_img,text="")
lable.pack()


window.mainloop()