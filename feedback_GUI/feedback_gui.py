#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

    #2 frames in root
    #1st frame will have logo inside of label widget
    #1st frame will have a header saying thank you as a label
    #1st frame will also have a message saying leavea comment as a label

    #frame 2 will have name, email and comments as labels, name and email entry widgets and text widget for comment section
    #frame2 will also have 2 buttons, submit and clear

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#e1d8b9")   
        self.style.configure("TButton", background="#e1d8b9")   
        self.style.configure("TLabel", background="#e1d8b9", font = ("Arial, 11"))   
        self.style.configure("Header.TLabel", background="#e1d8b9", font = ("Arial", 18, "bold"))   

        master.title("Explore California Feedback")
        master.resizable(False, False)
        master.configure(background = "#e1d8b9")
         
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        self.logo = PhotoImage(file = "tour_logo.gif")
        ttk.Label(self.header_frame, image = self.logo).grid(column = 0, row = 0, rowspan = 2)

        ttk.Label(self.header_frame, text="Thanks for Joining our Tour!", style="Header.TLabel").grid(column = 1, row = 0)
        ttk.Label(self.header_frame, wraplength=300, justify="center", text=("We're glad you chose Explore California for your recent adventure."
                                          " Please tell us what you thought about the 'Desert to Sea' tour.")).grid(column = 1, row = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        ttk.Label(self.frame_content, text="Name:").grid(column = 0, row = 0, padx=10, sticky=SW)
        ttk.Label(self.frame_content, text="Email:").grid(column = 1, row = 0, padx=10, sticky=SW)
        ttk.Label(self.frame_content, text="Comment:").grid(column = 0, row = 2, padx=10, sticky=SW)

        self.entry_name = ttk.Entry(self.frame_content, width=24,font=("Arial", 10))
        self.entry_name.grid(column = 0, row = 1,padx=10,pady=5,sticky=SW)
        self.entry_email = ttk.Entry(self.frame_content, width=24,font=("Arial", 10))
        self.entry_email.grid(column = 1, row = 1,padx=10,pady=5,sticky=SW )
        self.text_comments = Text(self.frame_content, width=50, height=10, font=("Arial", 10))
        self.text_comments.grid(column = 0, row = 3, columnspan=2,padx=10)

        ttk.Button(self.frame_content, text="Submit", command=self.submit).grid(column = 0, row = 4,sticky=E,pady=10,padx=10)
        ttk.Button(self.frame_content, text="Clear", command=self.clear).grid(column = 1, row = 4,sticky=W,pady=10,padx=10)

    def submit(self):
        print(f"Name: {self.entry_name.get()}")
        print(f"Email: {self.entry_email.get()}")
        print(f"Comments: {self.text_comments.get(1.0, 'end')}")
        self.clear()
        messagebox.showinfo(title="Explore California Feedback", message="Comment Submitted!")
    def clear(self):
        self.entry_name.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.text_comments.delete(1.0, "end")
        



def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
