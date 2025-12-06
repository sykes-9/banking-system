from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox

# ----------------------
# ABSTRACT CLASS: Account
# ----------------------


class Account(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


# ----------------------
# CLASS: SavingsAccount
# ----------------------
class SavingsAccount(Account):

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"{amount} deposited. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"{amount} withdrawn. New balance: {self.__balance}"
        else:
            return "Insufficient balance or invalid amount"

    def get_balance(self):
        return self.__balance


# ----------------------
# GUI: Bank App
# ----------------------
class BankApp:
    def __init__(self):
        self.account = None  # Will be created after user inputs name & balance
        self.root = tk.Tk()
        self.root.title("Bank Account GUI")
        self.root.geometry("400x400")
        self.root.config(bg="#1e1e1e")

        # ----------------------
        # Welcome / Input Frame
        # ----------------------
        self.input_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.input_frame.pack(pady=50)

        tk.Label(
            self.input_frame,
            text="Welcome to Bank System",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(
            self.input_frame,
            text="Enter Name:",
            font=("Arial", 12),
            fg="white",
            bg="#1e1e1e"
        ).grid(row=1, column=0, sticky="e", pady=5)
        self.name_entry = tk.Entry(self.input_frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, pady=5)

        tk.Label(
            self.input_frame,
            text="Starting Balance:",
            font=("Arial", 12),
            fg="white",
            bg="#1e1e1e"
        ).grid(row=2, column=0, sticky="e", pady=5)
        self.balance_entry = tk.Entry(self.input_frame, font=("Arial", 12))
        self.balance_entry.grid(row=2, column=1, pady=5)

        tk.Button(
            self.input_frame,
            text="Start Account",
            width=15,
            bg="#4caf50",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.create_account
        ).grid(row=3, column=0, columnspan=2, pady=20)

        self.root.mainloop()

    # ----------------------
    # Create account after input
    # ----------------------
    def create_account(self):
        name = self.name_entry.get().strip()
        balance_text = self.balance_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Please enter a name")
            return

        try:
            balance = float(balance_text)
            if balance < 0:
                messagebox.showerror("Error", "Balance cannot be negative")
                return
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number for balance")
            return

        # Create SavingsAccount
        self.account = SavingsAccount(name, balance)

        # Remove input frame and show main banking GUI
        self.input_frame.destroy()
        self.show_main_gui()

    # ----------------------
    # Main banking GUI
    # ----------------------
    def show_main_gui(self):
        # Owner and Balance Labels
        tk.Label(
            self.root,
            text=f"Owner: {self.account.owner}",
            font=("Arial", 14),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=10)

        self.balance_label = tk.Label(
            self.root,
            text=f"Balance: {self.account.get_balance()}",
            font=("Arial", 16, "bold"),
            fg="#4caf50",
            bg="#1e1e1e"
        )
        self.balance_label.pack(pady=10)

        # Amount Entry
        self.amount_entry = tk.Entry(self.root, width=20, font=("Arial", 12))
        self.amount_entry.insert(0, "Enter amount")
        self.amount_entry.bind("<FocusIn>", self.clear_placeholder)
        self.amount_entry.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Deposit",
            width=12,
            bg="#4caf50",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.deposit
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame,
            text="Withdraw",
            width=12,
            bg="#f44336",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.withdraw
        ).grid(row=0, column=1, padx=10)

    # ----------------------
    # Clear placeholder text
    # ----------------------
    def clear_placeholder(self, event):
        if self.amount_entry.get() == "Enter amount":
            self.amount_entry.delete(0, tk.END)

    # ----------------------
    # Deposit money
    # ----------------------
    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            msg = self.account.deposit(amount)
            self.update_balance()
            messagebox.showinfo("Deposit", msg)
            self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    # ----------------------
    # Withdraw money
    # ----------------------
    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            msg = self.account.withdraw(amount)
            self.update_balance()
            messagebox.showinfo("Withdraw", msg)
            self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    # ----------------------
    # Update balance label
    # ----------------------
    def update_balance(self):
        self.balance_label.config(
            text=f"Balance: {self.account.get_balance()}"
        )


# ----------------------
# RUN APP
# ----------------------
if __name__ == "__main__":
    BankApp()
