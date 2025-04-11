import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

class MazeBankApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MAZE BANK")
        self.root.geometry("700x600")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        
        # Store references to windows
        self.main_window = None
        self.current_window = None
        
        self.create_main_menu()
        
    def create_main_menu(self):
        # Clear any existing window
        if self.current_window:
            self.current_window.destroy()
        
        self.current_window = self.root
        self.main_window = self.current_window
        
        # Load Maze Bank logo
        try:
            response = requests.get("https://pbs.twimg.com/profile_images/891404814818652160/bm4rOKWS_400x400.jpg")
            img_data = response.content
            logo_img = Image.open(BytesIO(img_data))
            logo_img = logo_img.resize((100, 100), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
        except:
            self.logo = None
        
        # Main frame
        main_frame = tk.Frame(self.current_window, bg="white", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Header line with logo, bank name and balance
        header_line = tk.Frame(main_frame, bg="white")
        header_line.pack(fill="x")
        
        # Logo and bank name on left
        bank_name_frame = tk.Frame(header_line, bg="white")
        bank_name_frame.pack(side="left")
        
        if self.logo:
            logo_label = tk.Label(bank_name_frame, image=self.logo, bg="white")
            logo_label.image = self.logo
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
                 text="Account balance: $137,396.00", 
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
                 text="AKKIPANDYE", 
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
        deposit_btn = tk.Button(button_container, text="DEPOSIT", **button_style, 
                               command=self.create_deposit_window)
        deposit_btn.pack(pady=10)
        deposit_btn.bind("<Enter>", on_enter)
        deposit_btn.bind("<Leave>", on_leave)
        
        withdraw_btn = tk.Button(button_container, text="WITHDRAW", **button_style, 
                                command=self.create_withdrawal_window)
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
    
    def create_withdrawal_window(self):
        # Hide main menu
        self.root.withdraw()
        
        withdraw_win = tk.Toplevel()
        withdraw_win.title("MAZE BANK - Withdraw")
        withdraw_win.geometry("700x600")
        withdraw_win.configure(bg="white")
        withdraw_win.resizable(False, False)
        
        # Set close behavior to return to main menu
        withdraw_win.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(withdraw_win))
        
        self.current_window = withdraw_win
        
        # Main frame
        main_frame = tk.Frame(withdraw_win, bg="white", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Header line with bank name
        header_line = tk.Frame(main_frame, bg="white")
        header_line.pack(fill="x")
        
        # Bank name on left
        bank_text_frame = tk.Frame(header_line, bg="white")
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
                 text="Account balance $137,396.00", 
                 font=("Arial", 12, "bold"), 
                 fg="black", 
                 bg="white").pack(anchor="e")
        
        # Thick red line separator
        red_line = tk.Frame(main_frame, height=4, bg="#ff0000")
        red_line.pack(fill="x", pady=20)
        
        # Username and prompt in red box
        user_prompt_frame = tk.Frame(main_frame, bg="#ff0000", padx=10, pady=15)
        user_prompt_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(user_prompt_frame, 
                 text="AKKIPANDYE", 
                 font=("Arial", 12, "bold"), 
                 fg="white", 
                 bg="#ff0000").pack(anchor="w")
        
        tk.Label(user_prompt_frame, 
                 text="Select the amount you wish to withdraw from this account.", 
                 font=("Arial", 14, "bold"), 
                 fg="white", 
                 bg="#ff0000").pack(anchor="center", pady=(10, 0))
        
        # Button styling for amount buttons
        amount_button_style = {
            "font": ("Arial", 12, "bold"),
            "width": 15,
            "height": 2,
            "bg": "white",
            "fg": "black",
            "bd": 1,
            "relief": "solid",
            "highlightthickness": 0,
            "activebackground": "#eeeeee",
            "activeforeground": "black",
            "borderwidth": 1,
            "highlightbackground": "#cccccc"
        }
        
        # Amount buttons container
        amount_frame = tk.Frame(main_frame, bg="white")
        amount_frame.pack(pady=20)
        
        # First row of buttons
        row1_frame = tk.Frame(amount_frame, bg="white")
        row1_frame.pack(pady=10)
        
        # Create amount buttons with commands
        amounts_row1 = ["$50", "$100", "$500"]
        for amount in amounts_row1:
            tk.Button(row1_frame, text=amount, **amount_button_style,
                     command=lambda amt=amount: self.show_confirmation("withdrew", amt)).pack(side="left", padx=10)
        
        # Second row of buttons
        row2_frame = tk.Frame(amount_frame, bg="white")
        row2_frame.pack(pady=10)
        
        amounts_row2 = ["$1,000", "$2,500", "$5,000"]
        for amount in amounts_row2:
            tk.Button(row2_frame, text=amount, **amount_button_style,
                     command=lambda amt=amount: self.show_confirmation("withdrew", amt)).pack(side="left", padx=10)
        
        # Main Menu button at bottom
        menu_button_style = {
            "font": ("Arial", 12, "bold"),
            "width": 15,
            "height": 2,
            "bg": "#ff0000",
            "fg": "white",
            "bd": 1,
            "relief": "solid",
            "highlightthickness": 0,
            "activebackground": "#cc0000",
            "activeforeground": "white",
            "borderwidth": 1,
            "highlightbackground": "#ff0000",
            "command": lambda: self.on_window_close(withdraw_win)
        }
        
        menu_frame = tk.Frame(main_frame, bg="white")
        menu_frame.pack(pady=20)
        
        tk.Button(menu_frame, text="Main Menu", **menu_button_style).pack()
    
    def create_deposit_window(self):
        # Hide main menu
        self.root.withdraw()
        
        deposit_win = tk.Toplevel()
        deposit_win.title("MAZE BANK - Deposit")
        deposit_win.geometry("700x600")
        deposit_win.configure(bg="white")
        deposit_win.resizable(False, False)
        
        # Set close behavior to return to main menu
        deposit_win.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(deposit_win))
        
        self.current_window = deposit_win
        
        # Main frame
        main_frame = tk.Frame(deposit_win, bg="white", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Header line with bank name
        header_line = tk.Frame(main_frame, bg="white")
        header_line.pack(fill="x")
        
        # Bank name on left
        bank_text_frame = tk.Frame(header_line, bg="white")
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
                 text="Account balance $137,396.00", 
                 font=("Arial", 12, "bold"), 
                 fg="black", 
                 bg="white").pack(anchor="e")
        
        # Thick red line separator
        red_line = tk.Frame(main_frame, height=4, bg="#ff0000")
        red_line.pack(fill="x", pady=20)
        
        # Username and prompt in red box
        user_prompt_frame = tk.Frame(main_frame, bg="#ff0000", padx=10, pady=15)
        user_prompt_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(user_prompt_frame, 
                 text="AKKIPANDYE", 
                 font=("Arial", 12, "bold"), 
                 fg="white", 
                 bg="#ff0000").pack(anchor="w")
        
        tk.Label(user_prompt_frame, 
                 text="Select the amount you wish to deposit into this account.", 
                 font=("Arial", 14, "bold"), 
                 fg="white", 
                 bg="#ff0000").pack(anchor="center", pady=(10, 0))
        
        # Button styling for amount buttons
        amount_button_style = {
            "font": ("Arial", 12, "bold"),
            "width": 15,
            "height": 2,
            "bg": "white",
            "fg": "black",
            "bd": 1,
            "relief": "solid",
            "highlightthickness": 0,
            "activebackground": "#eeeeee",
            "activeforeground": "black",
            "borderwidth": 1,
            "highlightbackground": "#cccccc"
        }
        
        # Amount buttons container
        amount_frame = tk.Frame(main_frame, bg="white")
        amount_frame.pack(pady=20)
        
        # First row of buttons
        row1_frame = tk.Frame(amount_frame, bg="white")
        row1_frame.pack(pady=10)
        
        # Create amount buttons with commands
        amounts_row1 = ["$50", "$100", "$500"]
        for amount in amounts_row1:
            tk.Button(row1_frame, text=amount, **amount_button_style,
                     command=lambda amt=amount: self.show_confirmation("deposited", amt)).pack(side="left", padx=10)
        
        # Second row of buttons
        row2_frame = tk.Frame(amount_frame, bg="white")
        row2_frame.pack(pady=10)
        
        amounts_row2 = ["$1,000", "$2,500", "$5,000"]
        for amount in amounts_row2:
            tk.Button(row2_frame, text=amount, **amount_button_style,
                     command=lambda amt=amount: self.show_confirmation("deposited", amt)).pack(side="left", padx=10)
        
        # Main Menu button at bottom
        menu_button_style = {
            "font": ("Arial", 12, "bold"),
            "width": 15,
            "height": 2,
            "bg": "#ff0000",
            "fg": "white",
            "bd": 1,
            "relief": "solid",
            "highlightthickness": 0,
            "activebackground": "#cc0000",
            "activeforeground": "white",
            "borderwidth": 1,
            "highlightbackground": "#ff0000",
            "command": lambda: self.on_window_close(deposit_win)
        }
        
        menu_frame = tk.Frame(main_frame, bg="white")
        menu_frame.pack(pady=20)
        
        tk.Button(menu_frame, text="Main Menu", **menu_button_style).pack()
    
    def on_window_close(self, window):
        window.destroy()
        self.root.deiconify()  # Show main window again
        self.create_main_menu()
    
    def show_confirmation(self, action, amount):
        # Create a top-level window for the confirmation
        confirmation = tk.Toplevel(self.current_window)
        confirmation.title("Transaction Complete")
        confirmation.geometry("400x200")
        confirmation.configure(bg="white")
        confirmation.resizable(False, False)
        
        # Center the window
        window_width = confirmation.winfo_reqwidth()
        window_height = confirmation.winfo_reqheight()
        position_right = int(confirmation.winfo_screenwidth()/2 - window_width/2)
        position_down = int(confirmation.winfo_screenheight()/2 - window_height/2)
        confirmation.geometry(f"+{position_right}+{position_down}")
        
        # Add message
        msg = tk.Label(confirmation, 
                      text=f"You successfully {action} {amount}.", 
                      font=("Arial", 14, "bold"), 
                      bg="white")
        msg.pack(expand=True, pady=40)
        
        # Add OK button
        ok_btn = tk.Button(confirmation, 
                          text="OK", 
                          font=("Arial", 12, "bold"),
                          width=10,
                          bg="#ff0000",
                          fg="white",
                          command=confirmation.destroy)
        ok_btn.pack(pady=10)
        
        # Make the window modal
        confirmation.grab_set()
    
    def run(self):
        self.root.mainloop()

# Create and run the application
app = MazeBankApp()
app.run()
