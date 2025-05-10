import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import json
from datetime import datetime
import random

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
        
        # Sample transaction data with reason added
        self.transactions = [
            {"date": "2023-05-15", "time": "14:30:22", "type": "Deposit", "amount": 500.00, "balance": 503.72, "reason": "Vanilla Unicorn"},
            {"date": "2023-05-10", "time": "09:15:47", "type": "Withdrawal", "amount": 50.00, "balance": 3.72, "reason": "Vanilla Unicorn"},
            {"date": "2023-05-01", "time": "16:45:12", "type": "Deposit", "amount": 100.00, "balance": 53.72, "reason": "Vanilla Unicorn"}
        ]
        
        self.current_balance = 3.72
        self.username = "Ruslans Depo"
        self.current_language = "english"  # Default language
        
        # Daily quotes data
        self.quotes = [
            {"quote": "Money often costs too much.", "author": "Ralph Waldo Emerson"},
            {"quote": "The safest way to double your money is to fold it over and put it in your pocket.", "author": "Kin Hubbard"},
            {"quote": "A bank is a place where they lend you an umbrella in fair weather and ask for it back when it begins to rain.", "author": "Robert Frost"},
            {"quote": "It's not how much money you make, but how much money you keep.", "author": "Robert Kiyosaki"},
            {"quote": "The art is not in making money, but in keeping it.", "author": "Proverb"},
            {"quote": "Banks are happy to lend you money if you can prove you don't need it.", "author": "Unknown"},
            {"quote": "Financial peace isn't the acquisition of stuff. It's learning to live on less than you make.", "author": "Dave Ramsey"},
            {"quote": "Never spend your money before you have it.", "author": "Thomas Jefferson"},
            {"quote": "The goal isn't more money. The goal is living life on your terms.", "author": "Chris Brogan"},
            {"quote": "Money is a terrible master but an excellent servant.", "author": "P.T. Barnum"}
        ]
        
        # Language dictionaries (updated with quote texts)
        self.language_texts = {
            "english": {
                "bank_name": "MAZE BANK",
                "bank_subtitle": "OF LOS SANTOS",
                "balance": "Account balance: ${:.2f}",
                "choose_service": "Choose a service.",
                "deposit": "DEPOSIT",
                "withdraw": "WITHDRAW",
                "trans_log": "TRANSACTION LOG",
                "daily_quote": "DAILY QUOTE",
                "withdraw_prompt": "Select the amount you wish to withdraw from this account.",
                "deposit_prompt": "Select the amount you wish to deposit into this account.",
                "trans_history": "Transaction History",
                "return_main": "Return to Main →",
                "view_json": "VIEW RAW JSON",
                "date": "DATE",
                "time": "TIME",
                "type": "TYPE",
                "amount": "AMOUNT",
                "balance_col": "BALANCE",
                "reason": "REASON",
                "success_deposit": "You successfully deposited {}.",
                "success_withdraw": "You successfully withdrew {}.",
                "prev_balance": "Previous balance: ${:.2f}",
                "new_balance": "New balance: ${:.2f}",
                "insufficient_funds": "Insufficient Funds",
                "insufficient_msg": "You don't have enough balance for this withdrawal.",
                "quote_of_day": "Quote of the Day",
                "close": "Close"
            },
            "latvian": {
                "bank_name": "MAZE BANKA",
                "bank_subtitle": "NO LOS SANTOS",
                "balance": "Konta atlikums: ${:.2f}",
                "choose_service": "Izvēlieties pakalpojumu.",
                "deposit": "IESNIEGT",
                "withdraw": "IZŅEMT",
                "trans_log": "DARĪJUMU ŽURNĀLS",
                "daily_quote": "DIENAS CITĀTS",
                "withdraw_prompt": "Atlasiet summu, kuru vēlaties izņemt no šī konta.",
                "deposit_prompt": "Atlasiet summu, kuru vēlaties ieskaitīt šajā kontā.",
                "trans_history": "Darījumu vēsture",
                "return_main": "Atgriezties →",
                "view_json": "SKAITĀMĀ JSON",
                "date": "DATUMS",
                "time": "LAIKS",
                "type": "VEIDS",
                "amount": "SUMMA",
                "balance_col": "ATLIKUMS",
                "reason": "IEMESLS",
                "success_deposit": "Jūs veiksmīgi iemaksājāt {}.",
                "success_withdraw": "Jūs veiksmīgi izņēmāt {}.",
                "prev_balance": "Iepriekšējais atlikums: ${:.2f}",
                "new_balance": "Jauns atlikums: ${:.2f}",
                "insufficient_funds": "Nepietiek līdzekļu",
                "insufficient_msg": "Jums nav pietiekami daudz naudas šim izņēmumam.",
                "quote_of_day": "Dienas citāts",
                "close": "Aizvērt"
            },
            "morse": {
                "bank_name": "-- .- --.. . / -... .- -. -.-",
                "bank_subtitle": "--- ..-. / .-.. --- ... / ... .- -. - --- ...",
                "balance": ".- -.-. -.-. --- ..- -. - / -... .- .-.. .- -. -.-. .: ${:.2f}",
                "choose_service": "-.-. .... --- --- ... . / .- / ... . .-. ...- .. -.-. . .-.-.-",
                "deposit": "-.. . .--. --- ... .. -",
                "withdraw": ".-- .. - .... -.. .-. .- .--",
                "trans_log": "- .-. .- -. ... .- -.-. - .. --- -. / .-.. --- --.",
                "daily_quote": "-.. .- .. .-.. -.-- / --.- ..- --- - .",
                "withdraw_prompt": "... . .-.. . -.-. - / - .... . / .- -- --- ..- -. - / -.-- --- ..- / .-- .. ... .... / - --- / .-- .. - .... -.. .-. .- .-- / ..-. .-. --- -- / - .... .. ... / .- -.-. -.-. --- ..- -. - .-.-.-",
                "deposit_prompt": "... . .-.. . -.-. - / - .... . / .- -- --- ..- -. - / -.-- --- ..- / .-- .. ... .... / - --- / -.. . .--. --- ... .. - / .. -. - --- / - .... .. ... / .- -.-. -.-. --- ..- -. - .-.-.-",
                "trans_history": "- .-. .- -. ... .- -.-. - .. --- -. / .... .. ... - --- .-. -.--",
                "return_main": ". . - ..- .-. -. / - --- / -- .- .. -. →",
                "view_json": "...- .. .-- / .-. .- .-- / .--- ... --- -.",
                "date": "-.. .- - .",
                "time": "- .. -- .",
                "type": "- -.-- .--. .",
                "amount": ".- -- --- ..- -. -",
                "balance_col": "-... .- .-.. .- -. -.-. .",
                "reason": ". .- ... --- -.",
                "success_deposit": "-.-- --- ..- / ... ..- -.-. -.-. . ... ... ..-. ..- .-.. .-.. -.-- / -.. . .--. --- ... .. - . -.. / {}.",
                "success_withdraw": "-.-- --- ..- / ... ..- -.-. -.-. . ... ... ..-. ..- .-.. .-.. -.-- / .-- .. - .... -.. .-. . .-- / {}.",
                "prev_balance": ".--. .-. . ... .. --- ..- ... / -... .- .-.. .- -. -.-. .: ${:.2f}",
                "new_balance": ".--- .- ..- -. ... / -... .- .-.. .- -. -.-. .: ${:.2f}",
                "insufficient_funds": ".. -. ... ..- ..-. ..-. .. -.-. .. . -. - / ..-. ..- -. -.. ...",
                "insufficient_msg": "-.-- --- ..- / -.. --- -. .----. - / .... .- ...- . / . -. --- ..- --. .... / -... .- .-.. .- -. -.-. . / ..-. --- .-. / - .... .. ... / .-- .. - .... -.. .-. .- .-- .- .-.. .-.-.-",
                "quote_of_day": "--.- ..- --- - . / --- ..-. / - .... . / -.. .- -.--",
                "close": "-.-. .-.. --- ... ."
            }
        }
        
        self.create_main_menu()
        self.show_daily_quote()  # Show quote when app starts
        
    def show_daily_quote(self):
        # Get a random quote
        quote_data = random.choice(self.quotes)
        quote = quote_data["quote"]
        author = quote_data["author"]
        
        # Create a top-level window for the quote
        quote_window = tk.Toplevel(self.root)
        quote_window.title(self.language_texts[self.current_language]["quote_of_day"])
        quote_window.geometry("500x300")
        quote_window.configure(bg="white")
        quote_window.resizable(False, False)
        
        # Center the window
        window_width = quote_window.winfo_reqwidth()
        window_height = quote_window.winfo_reqheight()
        position_right = int(quote_window.winfo_screenwidth()/2 - window_width/2)
        position_down = int(quote_window.winfo_screenheight()/2 - window_height/2)
        quote_window.geometry(f"+{position_right}+{position_down}")
        
        # Main frame
        main_frame = tk.Frame(quote_window, bg="white", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Quote label
        quote_label = tk.Label(main_frame, 
                             text=f'"{quote}"',
                             font=("Arial", 12, "italic"),
                             wraplength=400,
                             justify="center",
                             bg="white")
        quote_label.pack(expand=True, pady=(20, 10))
        
        # Author label
        author_label = tk.Label(main_frame, 
                              text=f"— {author}",
                              font=("Arial", 10),
                              bg="white")
        author_label.pack(pady=(0, 20))
        
        # Close button
        close_btn = tk.Button(main_frame, 
                            text=self.language_texts[self.current_language]["close"], 
                            font=("Arial", 12, "bold"),
                            width=10,
                            bg="#ff0000",
                            fg="white",
                            command=quote_window.destroy)
        close_btn.pack(pady=10)
        
        # Make the window modal
        quote_window.grab_set()
        quote_window.transient(self.root)
    
    def create_main_menu(self):
        # Clear any existing window
        if self.current_window and self.current_window != self.root:
            self.current_window.destroy()
            self.root.deiconify()
        
        # Clear the window if coming back from transaction log
        for widget in self.root.winfo_children():
            widget.destroy()
            
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
                 text=self.language_texts[self.current_language]["bank_name"], 
                 font=("Arial", 24, "bold"), 
                 fg="black", 
                 bg="white").pack(anchor="w")
        
        tk.Label(bank_text_frame, 
                 text=self.language_texts[self.current_language]["bank_subtitle"], 
                 font=("Arial", 12), 
                 fg="black", 
                 bg="white").pack(anchor="w")
        
        # Account balance on right
        balance_frame = tk.Frame(header_line, bg="white")
        balance_frame.pack(side="right")
        
        self.balance_label = tk.Label(balance_frame, 
                 text=self.language_texts[self.current_language]["balance"].format(self.current_balance), 
                 font=("Arial", 12, "bold"), 
                 fg="black", 
                 bg="white")
        self.balance_label.pack(anchor="e")
        
        # Language buttons frame
        lang_frame = tk.Frame(header_line, bg="white")
        lang_frame.pack(side="right", padx=10)
        
        # Language buttons
        tk.Button(lang_frame, text="EN", font=("Arial", 8), width=3, 
                 command=lambda: self.set_language("english")).pack(side="left", padx=2)
        tk.Button(lang_frame, text="LV", font=("Arial", 8), width=3, 
                 command=lambda: self.set_language("latvian")).pack(side="left", padx=2)
        tk.Button(lang_frame, text="MC", font=("Arial", 8), width=3, 
                 command=lambda: self.set_language("morse")).pack(side="left", padx=2)
        
        # Thick red line separator
        red_line = tk.Frame(main_frame, height=4, bg="#ff0000")
        red_line.pack(fill="x", pady=20)
        
        # Combined username and service prompt in one red square (full width)
        user_service_frame = tk.Frame(main_frame, bg="#ff0000", padx=10, pady=15)
        user_service_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(user_service_frame, 
                 text=self.username, 
                 font=("Arial", 12, "bold"), 
                 fg="white", 
                 bg="#ff0000").pack(anchor="w")
        
        tk.Label(user_service_frame, 
                 text=self.language_texts[self.current_language]["choose_service"], 
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
        deposit_btn = tk.Button(button_container, 
                               text=self.language_texts[self.current_language]["deposit"], 
                               **button_style, 
                               command=self.create_deposit_window)
        deposit_btn.pack(pady=10)
        deposit_btn.bind("<Enter>", on_enter)
        deposit_btn.bind("<Leave>", on_leave)
        
        withdraw_btn = tk.Button(button_container, 
                                text=self.language_texts[self.current_language]["withdraw"], 
                                **button_style, 
                                command=self.create_withdrawal_window)
        withdraw_btn.pack(pady=10)
        withdraw_btn.bind("<Enter>", on_enter)
        withdraw_btn.bind("<Leave>", on_leave)
        
        trans_log_btn = tk.Button(button_container, 
                                 text=self.language_texts[self.current_language]["trans_log"], 
                                 **button_style,
                                 command=self.show_transaction_log)
        trans_log_btn.pack(pady=10)
        trans_log_btn.bind("<Enter>", on_enter)
        trans_log_btn.bind("<Leave>", on_leave)
        
        # Add Daily Quote button
        quote_btn = tk.Button(button_container, 
                             text=self.language_texts[self.current_language]["daily_quote"], 
                             **button_style,
                             command=self.show_daily_quote)
        quote_btn.pack(pady=10)
        quote_btn.bind("<Enter>", on_enter)
        quote_btn.bind("<Leave>", on_leave)
        
        # Apply rounded corners
        for btn in [deposit_btn, withdraw_btn, trans_log_btn, quote_btn]:
            btn.config(highlightthickness=1)
    
    def set_language(self, language):
        self.current_language = language
        self.create_main_menu()  # Refresh the UI with new language
    
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
                 text=self.language_texts[self.current_language]["bank_name"], 
                 font=("Arial", 24, "bold"), 
                 fg="black", 
                 bg="white").pack(anchor="w")
        
        tk.Label(bank_text_frame, 
                 text=self.language_texts[self.current_language]["bank_subtitle"], 
                 font=("Arial", 12), 
                 fg="black", 
                 bg="white").pack(anchor="w")
        
        # Account balance on right
        balance_frame = tk.Frame(header_line, bg="white")
        balance_frame.pack(side="right")
        
        tk.Label(balance_frame, 
                 text=self.language_texts[self.current_language]["balance"].format(self.current_balance), 
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
                 text=self.username, 
                 font=("Arial", 12, "bold"), 
                 fg="white", 
                 bg="#ff0000").pack(anchor="w")
        
        tk.Label(user_prompt_frame, 
                 text=self.language_texts[self.current_language]["withdraw_prompt"], 
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
                     command=lambda amt=amount: self.handle_transaction("withdraw", amt)).pack(side="left", padx=10)
        
        # Second row of buttons
        row2_frame = tk.Frame(amount_frame, bg="white")
        row2_frame.pack(pady=10)
        
        amounts_row2 = ["$1,000", "$2,500", "$5,000"]
        for amount in amounts_row2:
            tk.Button(row2_frame, text=amount, **amount_button_style,
                     command=lambda amt=amount: self.handle_transaction("withdraw", amt)).pack(side="left", padx=10)
        
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
        
        tk.Button(menu_frame, text=self.language_texts[self.current_language]["return_main"], **menu_button_style).pack()
    
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
                 text=self.language_texts[self.current_language]["bank_name"], 
                 font=("Arial", 24, "bold"), 
                 fg="black", 
                 bg="white").pack(anchor="w")
        
        tk.Label(bank_text_frame, 
                 text=self.language_texts[self.current_language]["bank_subtitle"], 
                 font=("Arial", 12), 
                 fg="black", 
                 bg="white").pack(anchor="w")
        
        # Account balance on right
        balance_frame = tk.Frame(header_line, bg="white")
        balance_frame.pack(side="right")
        
        tk.Label(balance_frame, 
                 text=self.language_texts[self.current_language]["balance"].format(self.current_balance), 
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
                 text=self.username, 
                 font=("Arial", 12, "bold"), 
                 fg="white", 
                 bg="#ff0000").pack(anchor="w")
        
        tk.Label(user_prompt_frame, 
                 text=self.language_texts[self.current_language]["deposit_prompt"], 
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
                     command=lambda amt=amount: self.handle_transaction("deposit", amt)).pack(side="left", padx=10)
        
        # Second row of buttons
        row2_frame = tk.Frame(amount_frame, bg="white")
        row2_frame.pack(pady=10)
        
        amounts_row2 = ["$1,000", "$2,500", "$5,000"]
        for amount in amounts_row2:
            tk.Button(row2_frame, text=amount, **amount_button_style,
                     command=lambda amt=amount: self.handle_transaction("deposit", amt)).pack(side="left", padx=10)
        
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
        
        tk.Button(menu_frame, text=self.language_texts[self.current_language]["return_main"], **menu_button_style).pack()
    
    def show_transaction_log(self):
        # Hide main menu
        self.root.withdraw()
        
        # Create new window for transaction log
        trans_log_win = tk.Toplevel()
        trans_log_win.title("MAZE BANK - Transaction Log")
        trans_log_win.geometry("700x600")
        trans_log_win.configure(bg="white")
        trans_log_win.resizable(False, False)
        
        # Set close behavior to return to main menu
        trans_log_win.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(trans_log_win))
        
        self.current_window = trans_log_win
        
        # Main frame
        main_frame = tk.Frame(trans_log_win, bg="white", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Red square with username and return button
        user_frame = tk.Frame(main_frame, bg="#ff0000", padx=10, pady=15)
        user_frame.pack(fill="x", pady=(10, 20))
        
        # Top row with username and return button
        top_row = tk.Frame(user_frame, bg="#ff0000")
        top_row.pack(fill="x")
        
        tk.Label(top_row, 
                text=self.username, 
                font=("Arial", 12, "bold"), 
                fg="white", 
                bg="#ff0000").pack(side="left", anchor="w")
        
        # Return button inside the red square, aligned to the right
        return_btn = tk.Button(top_row, text=self.language_texts[self.current_language]["return_main"], 
                             font=("Arial", 10, "bold"), 
                             bg="white", fg="#ff0000",
                             bd=0, padx=10, pady=2,
                             command=lambda: self.on_window_close(trans_log_win))
        return_btn.pack(side="right", anchor="e")
        
        # Transaction History label centered
        tk.Label(user_frame, 
                text=self.language_texts[self.current_language]["trans_history"], 
                font=("Arial", 14, "bold"), 
                fg="white", 
                bg="#ff0000").pack(anchor="center", pady=(10, 0))
                
        # Create a frame for the styled transaction display
        log_frame = tk.Frame(main_frame, bg="white", padx=10, pady=10)
        log_frame.pack(expand=True, fill="both")
        
        # Create headers for the transaction table
        headers_frame = tk.Frame(log_frame, bg="#ff0000")
        headers_frame.pack(fill="x")
        
        # Define column widths
        date_width = 10
        time_width = 10
        type_width = 12
        amount_width = 10
        balance_width = 12
        reason_width = 15
        
        # Create header labels
        tk.Label(headers_frame, text=self.language_texts[self.current_language]["date"], width=date_width, font=("Arial", 10, "bold"), 
                bg="#ff0000", fg="white", padx=5, pady=5).pack(side="left")
        tk.Label(headers_frame, text=self.language_texts[self.current_language]["time"], width=time_width, font=("Arial", 10, "bold"), 
                bg="#ff0000", fg="white", padx=5, pady=5).pack(side="left")
        tk.Label(headers_frame, text=self.language_texts[self.current_language]["type"], width=type_width, font=("Arial", 10, "bold"), 
                bg="#ff0000", fg="white", padx=5, pady=5).pack(side="left")
        tk.Label(headers_frame, text=self.language_texts[self.current_language]["amount"], width=amount_width, font=("Arial", 10, "bold"), 
                bg="#ff0000", fg="white", padx=5, pady=5).pack(side="left")
        tk.Label(headers_frame, text=self.language_texts[self.current_language]["balance_col"], width=balance_width, font=("Arial", 10, "bold"), 
                bg="#ff0000", fg="white", padx=5, pady=5).pack(side="left")
        tk.Label(headers_frame, text=self.language_texts[self.current_language]["reason"], width=reason_width, font=("Arial", 10, "bold"), 
                bg="#ff0000", fg="white", padx=5, pady=5).pack(side="left")
        
        # Create a canvas with scrollbar for transaction entries
        canvas = tk.Canvas(log_frame, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=canvas.yview)
        
        scrollable_frame = tk.Frame(canvas, bg="white")
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, pady=(2, 0))
        scrollbar.pack(side="right", fill="y", pady=(2, 0))
        
        # Display transaction data in rows with reason
        for i, transaction in enumerate(self.transactions):
            row_bg = "#f0f0f0" if i % 2 == 0 else "white"
            row_frame = tk.Frame(scrollable_frame, bg=row_bg)
            row_frame.pack(fill="x", expand=True)
            
            tk.Label(row_frame, text=transaction["date"], width=date_width, font=("Arial", 10),
                    bg=row_bg, padx=5, pady=5, anchor="w").pack(side="left")
            tk.Label(row_frame, text=transaction["time"], width=time_width, font=("Arial", 10),
                    bg=row_bg, padx=5, pady=5, anchor="w").pack(side="left")
            
            # Set color for transaction type
            type_color = "#00aa00" if transaction["type"] == "Deposit" else "#dd0000"
            tk.Label(row_frame, text=transaction["type"], width=type_width, font=("Arial", 10, "bold"),
                    fg=type_color, bg=row_bg, padx=5, pady=5, anchor="w").pack(side="left")
            
            # Format amount with + or - sign
            amount_text = f"+${transaction['amount']:.2f}" if transaction["type"] == "Deposit" else f"-${transaction['amount']:.2f}"
            amount_color = "#00aa00" if transaction["type"] == "Deposit" else "#dd0000"
            
            tk.Label(row_frame, text=amount_text, width=amount_width, font=("Arial", 10),
                    fg=amount_color, bg=row_bg, padx=5, pady=5, anchor="w").pack(side="left")
            tk.Label(row_frame, text=f"${transaction['balance']:.2f}", width=balance_width, font=("Arial", 10, "bold"),
                    bg=row_bg, padx=5, pady=5, anchor="w").pack(side="left")
            tk.Label(row_frame, text=transaction["reason"], width=reason_width, font=("Arial", 10),
                    bg=row_bg, padx=5, pady=5, anchor="w").pack(side="left")
        
        # Alternative JSON view button
        json_button = tk.Button(main_frame, text=self.language_texts[self.current_language]["view_json"], 
                              font=("Arial", 10), bg="#ff0000", fg="white",
                              command=self.show_raw_json)
        json_button.pack(anchor="center", pady=10)
    
    def show_raw_json(self):
        # Create a new toplevel window for JSON view
        json_window = tk.Toplevel(self.current_window)
        json_window.title("Transaction Data - Raw JSON")
        json_window.geometry("500x400")
        
        # Text widget to display JSON
        text_widget = tk.Text(json_window, wrap="none", font=("Consolas", 10), 
                             bg="white", fg="black", padx=10, pady=10)
        text_widget.pack(expand=True, fill="both", side="left")
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(json_window, orient="vertical", command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        # Format and display the transactions as pretty JSON
        formatted_json = json.dumps(self.transactions, indent=4)
        text_widget.insert("1.0", formatted_json)
        text_widget.configure(state="disabled")  # Make it read-only
        
        # Make the window modal
        json_window.grab_set()
        json_window.transient(self.current_window)
    
    def handle_transaction(self, action_type, amount):
        # Extract amount value from button text (remove $ and commas)
        amount_clean = float(amount.replace('$', '').replace(',', ''))
        
        # Get current date and time
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        # Update balance
        old_balance = self.current_balance
        if action_type == "deposit":
            self.current_balance += amount_clean
            trans_type = "Deposit"
        else:  # withdraw
            # Check if there's enough balance
            if self.current_balance < amount_clean:
                messagebox.showerror(
                    self.language_texts[self.current_language]["insufficient_funds"],
                    self.language_texts[self.current_language]["insufficient_msg"]
                )
                return
            
            self.current_balance -= amount_clean
            trans_type = "Withdrawal"
        
        # Add transaction to log
        self.transactions.insert(0, {
            "date": date_str,
            "time": time_str,
            "type": trans_type,
            "amount": amount_clean,
            "balance": self.current_balance,
            "reason": "ATM Transaction"
        })
        
        # Show confirmation message
        self.show_confirmation(action_type, amount, old_balance)
    
    def on_window_close(self, window):
        window.destroy()
        self.root.deiconify()  # Show main window again
        self.create_main_menu()
    
    def show_confirmation(self, action_type, amount, old_balance=None):
        # Format message based on action
        if action_type == "deposit":
            verb = self.language_texts[self.current_language]["success_deposit"].format(amount)
        else:
            verb = self.language_texts[self.current_language]["success_withdraw"].format(amount)
        
        # Create a top-level window for the confirmation
        confirmation = tk.Toplevel(self.current_window)
        confirmation.title("Transaction Complete")
        confirmation.geometry("400x250")
        confirmation.configure(bg="white")
        confirmation.resizable(False, False)
        
        # Center the window
        window_width = confirmation.winfo_reqwidth()
        window_height = confirmation.winfo_reqheight()
        position_right = int(confirmation.winfo_screenwidth()/2 - window_width/2)
        position_down = int(confirmation.winfo_screenheight()/2 - window_height/2)
        confirmation.geometry(f"+{position_right}+{position_down}")
        
        # Container frame
        main_frame = tk.Frame(confirmation, bg="white", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Add messages
        msg = tk.Label(main_frame, 
                     text=verb,
                     font=("Arial", 14, "bold"), 
                     bg="white")
        msg.pack(expand=True, pady=(20, 10))
        
        # Add balance update if provided
        if old_balance is not None:
            balance_frame = tk.Frame(main_frame, bg="white")
            balance_frame.pack(pady=10)
            
            tk.Label(balance_frame,
                   text=self.language_texts[self.current_language]["prev_balance"].format(old_balance),
                   font=("Arial", 12),
                   bg="white").pack(anchor="w")
            
            tk.Label(balance_frame,
                   text=self.language_texts[self.current_language]["new_balance"].format(self.current_balance),
                   font=("Arial", 12, "bold"),
                   bg="white").pack(anchor="w")
        
        # Add OK button
        ok_btn = tk.Button(main_frame, 
                         text="OK", 
                         font=("Arial", 12, "bold"),
                         width=10,
                         bg="#ff0000",
                         fg="white",
                         command=confirmation.destroy)
        ok_btn.pack(pady=20)
        
        # Make the window modal
        confirmation.grab_set()
        confirmation.transient(self.current_window)
    
    def run(self):
        self.root.mainloop()

# Create and run the application
if __name__ == "__main__":
    app = MazeBankApp()
    app.run()
