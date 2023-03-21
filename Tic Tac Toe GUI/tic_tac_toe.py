import tkinter as tk
from tkinter import messagebox
from tkinter import font

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x300")
        self.configure(bg="white")
        self.activePlayer = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.font = font.Font(family='Helvetica', size=15, weight='bold')

        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text="", width=10, height=3, font=self.font,
                                   command=lambda i=i, j=j: self.on_button_click(i, j), background= '#ffd343')
                button.grid(row=i, column=j)
                self.board[i][j] = button

    def on_button_click(self, i, j):
        if self.board[i][j]["text"] == "":
            self.board[i][j]["text"] = self.activePlayer
            self.check_winner()
            self.activePlayer = "O" if self.activePlayer == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.check_line(self.board[i][0]["text"], self.board[i][1]["text"], self.board[i][2]["text"]):
                self.show_winner()
                self.reset()
                return
            if self.check_line(self.board[0][i]["text"], self.board[1][i]["text"], self.board[2][i]["text"]):
                self.show_winner()
                self.reset()
                return

        if self.check_line(self.board[0][0]["text"], self.board[1][1]["text"], self.board[2][2]["text"]) or \
                self.check_line(self.board[0][2]["text"], self.board[1][1]["text"], self.board[2][0]["text"]):
            self.show_winner()
            self.reset()
            return

        # Check for draw
        if all(button["text"] != "" for row in self.board for button in row):
            messagebox.showinfo("Draw", "It's a draw!")
            self.reset()

    def check_line(self, a, b, c):
        return a == b == c != ""

    def show_winner(self):
        message = f"Player {self.activePlayer} wins!"
        messagebox.showinfo("Congratulations!", message)

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j]["text"] = ""

        self.activePlayer = "X"

    if __name__ == "__main__":
        app = TicTacToe()
        app.mainloop()
