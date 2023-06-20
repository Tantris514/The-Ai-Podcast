import tkinter as tk
import os
import time

def load_files(directory):
    files = sorted((f for f in os.listdir(directory) if f.endswith('.txt')), key=lambda x: int(x.split('.')[0]))
    for file in files:
        if file not in loaded_files:
            with open(os.path.join(directory, file), "r") as f:
                file_content = f.read()
                loaded_files.add(file)
                current_color = 'even' if len(loaded_files) % 2 == 0 else 'odd'
                text.insert(tk.END, file_content + '\n\n', current_color)

def update_text():
    load_files(directory_path)
    root.after(1000, update_text)  # check the directory every second

root = tk.Tk()
root.geometry('400x300')

text = tk.Text(root, wrap='word')
text.pack(fill=tk.BOTH, expand=True)

# define the tag "even"
text.tag_config("even", foreground="blue")

# define the tag "odd"
text.tag_config("odd", foreground="pink")

directory_path = "discussion"  # specify your directory path here
loaded_files = set()

update_text()  # initial directory check
root.mainloop()
