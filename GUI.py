import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import main

def get_input_folder():
    input_folder = filedialog.askdirectory(title="select where you saved the google takeout files")
    input_entry.delete(0, tk.END)  # Clear the entry widget
    input_entry.insert(0, input_folder)

def get_output_folder():
    output_folder = filedialog.askdirectory(title="Select where you would like to save your photos")
    output_entry.delete(0, tk.END)  # Clear the entry widget
    output_entry.insert(0, output_folder)

def run_program():
    user_in = input_entry.get()
    user_out = output_entry.get()
    if not user_in or not user_out: #user must select both input and output for it to work
        tk.messagebox.showerror("Error", "you must select both input and output folders before running the program.")
        return
    try: #makes sure there aren't any errors
        main.main(user_in, user_out)
        tk.messagebox.showinfo("Done", f"You're all set! \n Your photos are ready at: \n {user_out}")
        app.destroy()
    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Google Photos Organizer")
app.geometry("600x350")
# Labels
title = ctk.CTkLabel(app, text="Google Photos Organizer", font=("Arial", 20, "bold"))
input_label = ctk.CTkLabel(app, text="Input Folder:", font=("Arial", 12))
output_label = ctk.CTkLabel(app, text="Output Folder:", font=("Arial", 12))

# Entries
input_entry = ctk.CTkEntry(app, placeholder_text= "Please select where you extracted your takeout files")
output_entry = ctk.CTkEntry(app, placeholder_text= "Please select where you would like to save your files")

# Buttons
input_button = ctk.CTkButton(app, text="Browse", command=get_input_folder, font=("Arial", 12, "bold"))
output_button = ctk.CTkButton(app, text="Browse", command=get_output_folder, font=("Arial", 12, "bold"))
go_button = ctk.CTkButton(app, text="Go!", command=run_program, font=("Arial", 15, "bold"))

# Layout using grid manager
title.grid(row=0, column=0, columnspan=3,padx=10, pady=10, sticky="we")

input_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
input_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")
input_button.grid(row=2, column=0, padx=10, pady=5, sticky="w")

output_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
output_entry.grid(row=4, column=1, padx=10, pady=5, sticky="we")
output_button.grid(row=4, column=0, padx=10, pady=5, sticky="w")

go_button.grid(row=5, column=0, columnspan=3, padx=10, pady=60, sticky="we")

# Adjust column weights to make the Entry widgets expand horizontally
app.grid_columnconfigure(1, weight=1)

app.mainloop()



