from tkinter import *
import pyautogui
import time

def bfn():
    time.sleep(3)
    for i in range(int(amount.get())):
        time.sleep(0.25)
        pyautogui.write(ttx.get())
        pyautogui.press("enter")

root = Tk()

canvas = Canvas(root, width=600, height=260)
canvas.pack()

root.title("Spam Bot")
frame = Frame(root, bg="black")
#(relx,rely,relwidth,relheight)
frame.place(relx=0.157,rely=0.1,relwidth=0.7,relheight=0.8)
label = Label(frame, text="Spam X", bg="black", fg="orange")
label.place(relx=0.1,rely=0.37,relwidth=0.4,relheight=0.23)
label2 = Label(frame, text="Enter text to spam :", bg= "black", fg="orange")
label2.place(relx=0.001,rely=0.01,relwidth=0.4,relheight=0.4)
btn = Button(frame, text="Spam!", command=bfn)
btn.place(relx=0.38,rely=0.7,relwidth=0.23,relheight=0.23)
amount = Entry(frame)
amount.place(relx=0.36,rely=0.37,relwidth=0.23,relheight=0.23)
ttx = Entry(frame)
ttx.place(relx=0.38,rely=0.1,relwidth=0.23,relheight=0.23)

mainloop()