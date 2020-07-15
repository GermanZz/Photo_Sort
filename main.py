from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from datetime import datetime


def choose_dir():
    dir_path = filedialog.askdirectory()
    entry_path.delete(0, END)
    entry_path.insert(0, dir_path)


def run():
    curr_path = entry_path.get()
    if curr_path:
        for folder, subfolder, files in os.walk(curr_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime('%Y-%m-%d')
                date_folder = os.path.join(curr_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo(title='Success', message='Sorting has been done!')
        entry_path.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Path shouldn\'t be empty')


root = Tk()
root.title('PhotoSort')
root.iconbitmap('lg.ico')
root.geometry('500x120+500+280')

s = ttk.Style()
s.configure('Run.TButton', font=('Helvetica', 14))
s.configure('Open.TButton', font=('Helvetica', 12))

frame = Frame(root, bg='#56ADFF', bd=5)
frame.pack(fill=X, pady=10, padx=10)

entry_path = ttk.Entry(frame)
entry_path.pack(side=LEFT, expand=1, fill=X, ipady=2)

btn_open = ttk.Button(frame, text='Select Folder', style='Open.TButton', command=choose_dir)
btn_open.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, text='Run', style='Run.TButton', command=run)
btn_start.pack(fill=X, padx=10, pady=10)

root.mainloop()
