import tkinter as tk
application=tk.Tk()
from tkinter import messagebox
application.title("DRIVER'S INTELLECT TEST")
application.geometry("1000x800+400+100")
application.configure(bg="gold")

def submit():
    answers=["A","B","C"]
    question1=question1_entry.get()
    question2=question2_entry.get()
    question3=question3_entry.get()
    feedback1=[question1,question2,question3]

    if question1 in feedback1[0]==answers[0] and question2 in feedback1[1]==answers[1] and question3 in feedback1[2]==answers[2]:
        messagebox.showinfo("Result","You pass")
    elif question1 in feedback1[0]==answers[0] and question2 in feedback1[1]==answers[1]:
        messagebox.showinfo("Result","You pass")
    elif question2 in feedback1[1]==answers[1] and question3 in feedback1[2]==answers[2]:
        messagebox.showinfo("Result","You pass")
    elif question1 in feedback1[0]==answers[0] and question3 in feedback1[2]==answers[2]:
        messagebox.showinfo("Result","You pass")
    else:
        messagebox.showinfo("Result","You fail")


question1_label=tk.Label(text="1. What does a stop sign indicate?  ",font=("Algerian",13),width=30,height=3,bg="white")
question1_label.grid(row=0,column=2,padx=20,pady=20)

question1_entry=tk.Entry(font=("Algerian",13))
question1_entry.grid(row=0,column=3,padx=5,pady=6)

question1_option1_label=tk.Label(text="A. Stop ",font=("Serif",13),width=20,height=1,bg="white")
question1_option1_label.grid(row=1,column=2,padx=20)

question1_option2_label=tk.Label(text="B. Go ",font=("Serif",13),width=20,height=1,bg="white")
question1_option2_label.grid(row=2,column=2,padx=20,pady=20)

question1_option3_label=tk.Label(text="C. Wait ",font=("Serif",13),width=20,height=1,bg="white")
question1_option3_label.grid(row=3,column=2,padx=20)


question2_label=tk.Label(text="2. Should we obey traffic signs?  ",font=("Algerian",13),width=30,height=3,bg="white")
question2_label.grid(row=5,column=2,padx=20,pady=20)

question2_entry=tk.Entry(font=("Algerian",13))
question2_entry.grid(row=5,column=3,padx=5,pady=6)

question2_option1_label=tk.Label(text="A. No ",font=("Serif",13),width=20,height=1,bg="white")
question2_option1_label.grid(row=6,column=2,padx=20)

question2_option2_label=tk.Label(text="B. Yes ",font=("Serif",13),width=20,height=1,bg="white")
question2_option2_label.grid(row=7,column=2,padx=20,pady=20)

question2_option3_label=tk.Label(text="C. Maybe ",font=("Serif",13),width=20,height=1,bg="white")
question2_option3_label.grid(row=8,column=2,padx=20)


question3_label=tk.Label(text="3. Is it okay to drink and drive?  ",font=("Algerian",13),width=30,height=3,bg="white")
question3_label.grid(row=10,column=2,padx=20,pady=20)

question3_entry=tk.Entry(font=("Algerian",13))
question3_entry.grid(row=10,column=3,padx=5,pady=6)

question3_option1_label=tk.Label(text="A. Yes ",font=("Serif",13),width=20,height=1,bg="white")
question3_option1_label.grid(row=11,column=2,padx=20)

question3_option2_label=tk.Label(text="B. Maybe ",font=("Serif",13),width=20,height=1,bg="white")
question3_option2_label.grid(row=12,column=2,padx=20,pady=20)

question3_option3_label=tk.Label(text="C. No ",font=("Serif",13),width=20,height=1,bg="white")
question3_option3_label.grid(row=13,column=2,padx=20)


submit_button=tk.Button(text="Submit",font=("Algerian",13), command=submit)
submit_button.grid(row=15,column=5,padx=140,pady=35)



application.mainloop()