import customtkinter as tk
import webbrowser
import os
import sys

from gevent.monkey import patch_sys

root = tk.CTk()

def resource_path(relative_path):
    """ Get the absolute path to the resource, whether in development or in PyInstaller bundle """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def show_message(title):
    # Create a Toplevel window (popup)
    message_window = tk.CTkToplevel()
    message_window.title(title)
    message_window.configure(fg_color="light green")
    message_window.resizable(False,False)

    width, height = 500,300
    display_width = root.winfo_screenwidth()
    display_height = root.winfo_screenheight()
    left = int((display_width / 2) - (width / 2))
    top = int((display_height / 2) - (height / 2))

    # Set the window size
    message_window.geometry(f"{width}x{height}+{left}+{top}")

    # Add a label for the message
    message_label = tk.CTkLabel(message_window, text="Contact : ", wraplength=250,text_color="black",font=("Times New Roman",30))
    message_label.pack(pady=20, padx=20)
    web_button = tk.CTkButton(message_window,text="Website",text_color="black",font=("Times New Roman",25),fg_color="orange",command=lambda :webbrowser.open("https://methash-dinelka.blogspot.com/"))
    web_button.pack(pady=10)
    github_button = tk.CTkButton(message_window, text="Github", text_color="black", font=("Times New Roman", 25),fg_color="orange",command=lambda: webbrowser.open("https://github.com/MethashDinelka"))
    github_button.pack(pady=10)
    fb_button = tk.CTkButton(message_window, text="Facebook", text_color="black", font=("Times New Roman", 25),fg_color="orange",command=lambda: webbrowser.open("https://www.facebook.com/profile.php?id=100084332928167"))
    fb_button.pack(pady=10)

    # Add an "OK" button to close the message window
    ok_button = tk.CTkButton(message_window, text="Close", command=message_window.destroy,font=("Times New Roman", 25),fg_color="red",text_color="black")
    ok_button.pack(pady=10)

    # Center the message window
    message_window.transient()
    message_window.grab_set()

def submit():
    sub = entry_subject.get()
    marks = int(entry_mark.get())
    if (marks>=75):
        grade = f"A pass for {sub}! Excellent :) ."
    elif (marks<75)and(marks>=65):
        grade = f"B pass for {sub}! Well Done!"
    elif (marks<65)and(marks>=55):
        grade = f"C pass for {sub}! Good...Work More."
    elif (marks<55)and(marks>=40):
        grade = f"S pass for {sub}! Work Hard."
    else:
        grade = f"F pass for {sub}! You Should Work Hard More."
    result_label.configure(text=f"From the Examination You have Got {grade}",text_color="green",font=("Times New Roman",20),fg_color="transparent")

def close():
    root.destroy()

width, height = 700, 600

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int((display_width / 2) - (width / 2))
top = int((display_height / 2) - (height / 2))

tk.set_appearance_mode("system")
root.title("Result Calculator")
root.iconbitmap(resource_path("icon.ico"))
root.configure(fg_color="white")
root.geometry(f"{width}x{height}+{left}+{top}")
root.resizable(False, False)

label_name = tk.CTkLabel(root,text="Result Calculator",font=("Calibri (Body)",50),text_color="black")
label_name.pack()
label_credit = tk.CTkLabel(root, text="Software By Methash Dinelka ©", text_color="black",font=("Calibri (Body)",18))
label_credit.pack()

empptylab = tk.CTkLabel(root,fg_color="transparent",text=" ")
empptylab.pack()
empptylab2 = tk.CTkLabel(root,fg_color="transparent",text=" ")
empptylab2.pack()

subject = tk.CTkLabel(root,fg_color="transparent",text="Subject : ",font=("Times New Roman",30),text_color="blue")
subject.pack()

entry_subject = tk.CTkEntry(root,width=500,placeholder_text="Enter The Name Of The Subject :)")
entry_subject.pack()

empptylab3 = tk.CTkLabel(root,fg_color="transparent",text=" ")
empptylab3.pack()

mark = tk.CTkLabel(root,fg_color="transparent",text="Marks : ",font=("Times New Roman",30),text_color="blue")
mark.pack()
entry_mark = tk.CTkEntry(root,width=500,placeholder_text="Enter The Mark Obtained For The Subject :)")
entry_mark.pack()

emptylab4 = tk.CTkLabel(root,fg_color="transparent",text=" ")
emptylab4.pack()

submit = tk.CTkButton(root,text="Submit",fg_color="green",font=("Aerial",20),command=submit)
submit.pack()

emptylab5 = tk.CTkLabel(root,fg_color="transparent",text=" ")
emptylab5.pack()

result_label = tk.CTkLabel(root,text="www.methash-dinelka.blogspot.com",text_color="black")
result_label.pack()

close_button = tk.CTkButton(root,text="Close",text_color="white",fg_color="red",font=("Times New Roman",25),command=close)
close_button.pack()

show_message_button = tk.CTkButton(root, text="More Info.",command=lambda: show_message(title="Contact - Methash Dinelka"),fg_color="yellow",font=("Times New Roman",24),text_color="black")
show_message_button.pack(pady=50)

root.mainloop()