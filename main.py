import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def create_maze_bank_ui():
    root = tk.Tk()
    root.title("MAZE BANK")
    root.geometry("700x600")
    root.configure(bg="white")
    # Prevent window resizing
    root.resizable(False, False)
    
    # Load Maze Bank logo
    try:
        response = requests.get("https://pbs.twimg.com/profile_images/891404814818652160/bm4rOKWS_400x400.jpg")
        img_data = response.content
        logo_img = Image.open(BytesIO(img_data))
        logo_img = logo_img.resize((100, 100), Image.Resampling.LANCZOS)
        logo = ImageTk.PhotoImage(logo_img)
    except:
        logo = None
    
    # Main frame
    main_frame = tk.Frame(root, bg="white", padx=20, pady=20)
    main_frame.pack(expand=True, fill="both")
    
    # Header line with logo, bank name and balance
    header_line = tk.Frame(main_frame, bg="white")
    header_line.pack(fill="x")
    
    # Logo and bank name on left
    bank_name_frame = tk.Frame(header_line, bg="white")
    bank_name_frame.pack(side="left")
    
    if logo:
        logo_label = tk.Label(bank_name_frame, image=logo, bg="white")
        logo_label.image = logo
        logo_label.pack(side="left", padx=(0, 10))
    
    bank_text_frame = tk.Frame(bank_name_frame, bg="white")
    bank_text_frame.pack(side="left")
    
    tk.Label(bank_text_frame, 
             text="MAZE BANK", 
             font=("Arial", 24, "bold"), 
             fg="black", 
             bg="white").pack(anchor="w")
    
    tk.Label(bank_text_frame, 
             text="OF LOS SANTOS", 
             font=("Arial", 12), 
             fg="black", 
             bg="white").pack(anchor="w")
    
    # Account balance on right
    balance_frame = tk.Frame(header_line, bg="white")
    balance_frame.pack(side="right")
    
    tk.Label(balance_frame, 
             text="Account balance: $3.72", 
             font=("Arial", 12, "bold"), 
             fg="black", 
             bg="white").pack(anchor="e")
    
    # Thick red line separator
    red_line = tk.Frame(main_frame, height=4, bg="#ff0000")
    red_line.pack(fill="x", pady=20)
    
    # Combined username and service prompt in one red square (full width)
    user_service_frame = tk.Frame(main_frame, bg="#ff0000", padx=10, pady=15)
    user_service_frame.pack(fill="x", pady=(0, 20))
    
    tk.Label(user_service_frame, 
             text="Ruslans Depo", 
             font=("Arial", 12, "bold"), 
             fg="white", 
             bg="#ff0000").pack(anchor="w")
    
    tk.Label(user_service_frame, 
             text="Choose a service.", 
             font=("Arial", 14, "bold"), 
             fg="white", 
             bg="#ff0000").pack(anchor="center", pady=(10, 0))
    
    # Button styling
    button_style = {
        "font": ("Arial", 12, "bold"),
        "width": 20,
        "height": 2,
        "bg": "#ff0000",
        "fg": "white",
        "bd": 1,
        "relief": "solid",
        "highlightthickness": 0,
        "activebackground": "#cc0000",
        "activeforeground": "white",
        "borderwidth": 1,
        "highlightbackground": "#ff0000"
    }
    
    # Hover effects
    def on_enter(e):
        e.widget.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
    
    def on_leave(e):
        e.widget.config(highlightbackground="#ff0000", highlightcolor="#ff0000", highlightthickness=1)
    
    # Button container
    button_container = tk.Frame(main_frame, bg="white")
    button_container.pack(pady=20)
    
    # Create buttons
    deposit_btn = tk.Button(button_container, text="DEPOSIT", **button_style)
    deposit_btn.pack(pady=10)
    deposit_btn.bind("<Enter>", on_enter)
    deposit_btn.bind("<Leave>", on_leave)
    
    withdraw_btn = tk.Button(button_container, text="WITHDRAW", **button_style)
    withdraw_btn.pack(pady=10)
    withdraw_btn.bind("<Enter>", on_enter)
    withdraw_btn.bind("<Leave>", on_leave)
    
    trans_log_btn = tk.Button(button_container, text="TRANSACTION LOG", **button_style)
    trans_log_btn.pack(pady=10)
    trans_log_btn.bind("<Enter>", on_enter)
    trans_log_btn.bind("<Leave>", on_leave)
    
    # Apply rounded corners (simulated)
    for btn in [deposit_btn, withdraw_btn, trans_log_btn]:
        btn.config(highlightthickness=1)
    
    root.mainloop()
#sdasdas
create_maze_bank_ui()