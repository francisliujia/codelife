from tkinter import *

window = Tk()
window.title("my computer science glossary")
window.configure(background="black")

photo =PhotoImage(file='website.jpeg')
Label (window, image=photo, fg='white',font='none for 12 bold', bg='black').grid(row=1, colum=0, sticky=W)


window.mainloop()