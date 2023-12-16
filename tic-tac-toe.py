import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.maxsize(270,265)
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=('normal', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)

        self.window.mainloop()

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.update_button(row, col)

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()

    def update_button(self, row, col):
        button = self.window.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player, state=tk.DISABLED)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True  
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                button = self.window.grid_slaves(row=i, column=j)[0]
                button.config(text="", state=tk.NORMAL)
                self.board[i][j] = ""
        self.current_player = "X"


if __name__ == "__main__":
    TicTacToe()
