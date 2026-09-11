"""
CodSoft Artificial Intelligence Internship - Task 2
Project: Tic-Tac-Toe AI with Minimax Algorithm (Graphical User Interface)
Author: Advait Dange
Repository: CODSOFT_TASKNO
"""

import math
import random
import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    """
    Modern Tkinter GUI for Unbeatable Tic-Tac-Toe AI.
    Features human vs AI gameplay, Minimax search engine,
    live score tracking, and difficulty selection.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI (Unbeatable Minimax) - Advait Dange")
        self.root.geometry("460x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.human = "X"
        self.ai = "O"
        self.board = [" " for _ in range(9)]
        self.game_over = False

        # Scores
        self.score_human = 0
        self.score_ai = 0
        self.score_draws = 0

        # UI Styling colors
        self.COLOR_BG = "#1e1e2e"
        self.COLOR_CARD = "#2a2b3d"
        self.COLOR_ACCENT_X = "#f38ba8"  # Coral Pink
        self.COLOR_ACCENT_O = "#89b4fa"  # Ice Blue
        self.COLOR_BTN = "#313244"
        self.COLOR_TEXT = "#cdd6f4"
        self.COLOR_STATUS = "#a6e3a1"    # Mint green

        self._build_ui()

    def _build_ui(self):
        # Header / Title Frame
        title_frame = tk.Frame(self.root, bg=self.COLOR_BG)
        title_frame.pack(pady=(15, 5))

        title_label = tk.Label(
            title_frame,
            text="TIC-TAC-TOE AI",
            font=("Segoe UI", 20, "bold"),
            bg=self.COLOR_BG,
            fg="#cdd6f4"
        )
        title_label.pack()

        subtitle_label = tk.Label(
            title_frame,
            text="Minimax Algorithm with Alpha-Beta Pruning | By Advait Dange",
            font=("Segoe UI", 9),
            bg=self.COLOR_BG,
            fg="#a6adc8"
        )
        subtitle_label.pack()

        # Difficulty & Mode Selection Frame
        controls_frame = tk.Frame(self.root, bg=self.COLOR_CARD, padx=10, pady=5)
        controls_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(controls_frame, text="Difficulty:", font=("Segoe UI", 10, "bold"), bg=self.COLOR_CARD, fg=self.COLOR_TEXT).pack(side="left", padx=5)
        self.diff_var = tk.StringVar(value="Unbeatable (Minimax)")
        diff_menu = tk.OptionMenu(
            controls_frame, self.diff_var, "Unbeatable (Minimax)", "Medium", "Easy", command=self._on_diff_change
        )
        diff_menu.config(bg=self.COLOR_BTN, fg=self.COLOR_TEXT, relief="flat", highlightthickness=0)
        diff_menu["menu"].config(bg=self.COLOR_BTN, fg=self.COLOR_TEXT)
        diff_menu.pack(side="left", padx=5)

        # Scoreboard Frame
        score_frame = tk.Frame(self.root, bg=self.COLOR_CARD, padx=15, pady=8)
        score_frame.pack(pady=5, padx=20, fill="x")

        self.score_label_human = tk.Label(
            score_frame, text=f"You (X): {self.score_human}", font=("Segoe UI", 10, "bold"), bg=self.COLOR_CARD, fg=self.COLOR_ACCENT_X
        )
        self.score_label_human.pack(side="left", expand=True)

        self.score_label_draw = tk.Label(
            score_frame, text=f"Ties: {self.score_draws}", font=("Segoe UI", 10, "bold"), bg=self.COLOR_CARD, fg="#fab387"
        )
        self.score_label_draw.pack(side="left", expand=True)

        self.score_label_ai = tk.Label(
            score_frame, text=f"AI (O): {self.score_ai}", font=("Segoe UI", 10, "bold"), bg=self.COLOR_CARD, fg=self.COLOR_ACCENT_O
        )
        self.score_label_ai.pack(side="left", expand=True)

        # Status Label
        self.status_label = tk.Label(
            self.root,
            text="Your turn! Click any cell to place 'X'.",
            font=("Segoe UI", 11, "bold"),
            bg=self.COLOR_BG,
            fg=self.COLOR_STATUS
        )
        self.status_label.pack(pady=10)

        # Board Grid Frame
        board_frame = tk.Frame(self.root, bg=self.COLOR_BG)
        board_frame.pack(pady=5)

        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            btn = tk.Button(
                board_frame,
                text=" ",
                font=("Segoe UI", 24, "bold"),
                width=4,
                height=1,
                bg=self.COLOR_BTN,
                fg=self.COLOR_TEXT,
                activebackground="#45475a",
                relief="flat",
                bd=0,
                command=lambda idx=i: self.on_cell_click(idx)
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.buttons.append(btn)

        # Reset / New Game Button
        btn_frame = tk.Frame(self.root, bg=self.COLOR_BG)
        btn_frame.pack(pady=15)

        reset_btn = tk.Button(
            btn_frame,
            text="🔄 Restart Game",
            font=("Segoe UI", 11, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#b4befe",
            relief="flat",
            padx=18,
            pady=6,
            command=self.reset_game
        )
        reset_btn.pack(side="left", padx=10)

    def _on_diff_change(self, _):
        self.reset_game()

    def on_cell_click(self, index):
        if self.board[index] != " " or self.game_over:
            return

        # Player move
        self.board[index] = self.human
        self.buttons[index].config(text=self.human, fg=self.COLOR_ACCENT_X)

        if self.check_winner(self.board, self.human):
            self.status_label.config(text="🎉 Congratulations! You won!", fg="#a6e3a1")
            self.score_human += 1
            self.update_scores()
            self.game_over = True
            return

        if self.is_board_full(self.board):
            self.status_label.config(text="🤝 It's a DRAW!", fg="#fab387")
            self.score_draws += 1
            self.update_scores()
            self.game_over = True
            return

        # AI Turn
        self.status_label.config(text="AI is calculating optimal move...", fg="#89b4fa")
        self.root.update()

        ai_idx = self.get_ai_move()
        if ai_idx is not None:
            self.board[ai_idx] = self.ai
            self.buttons[ai_idx].config(text=self.ai, fg=self.COLOR_ACCENT_O)

            if self.check_winner(self.board, self.ai):
                self.status_label.config(text="🤖 AI WINS! Minimax remains undefeated!", fg="#f38ba8")
                self.score_ai += 1
                self.update_scores()
                self.game_over = True
                return

            if self.is_board_full(self.board):
                self.status_label.config(text="🤝 It's a DRAW!", fg="#fab387")
                self.score_draws += 1
                self.update_scores()
                self.game_over = True
                return

        self.status_label.config(text="Your turn! Click an empty cell.", fg=self.COLOR_STATUS)

    def check_winner(self, board_state, player):
        win_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(all(board_state[i] == player for i in combo) for combo in win_combos)

    def is_board_full(self, board_state):
        return " " not in board_state

    def available_moves(self, board_state):
        return [i for i, spot in enumerate(board_state) if spot == " "]

    def minimax(self, board_state, depth, is_maximizing, alpha, beta):
        if self.check_winner(board_state, self.ai):
            return {"position": None, "score": 10 - depth}
        elif self.check_winner(board_state, self.human):
            return {"position": None, "score": depth - 10}
        elif self.is_board_full(board_state):
            return {"position": None, "score": 0}

        empty_indices = self.available_moves(board_state)

        if is_maximizing:
            best = {"position": None, "score": -math.inf}
            for move in empty_indices:
                board_state[move] = self.ai
                sim_score = self.minimax(board_state, depth + 1, False, alpha, beta)
                board_state[move] = " "
                sim_score["position"] = move

                if sim_score["score"] > best["score"]:
                    best = sim_score
                alpha = max(alpha, best["score"])
                if beta <= alpha:
                    break
            return best
        else:
            best = {"position": None, "score": math.inf}
            for move in empty_indices:
                board_state[move] = self.human
                sim_score = self.minimax(board_state, depth + 1, True, alpha, beta)
                board_state[move] = " "
                sim_score["position"] = move

                if sim_score["score"] < best["score"]:
                    best = sim_score
                beta = min(beta, best["score"])
                if beta <= alpha:
                    break
            return best

    def get_ai_move(self):
        available = self.available_moves(self.board)
        if not available:
            return None

        diff = self.diff_var.get()
        if "Easy" in diff:
            return random.choice(available)
        elif "Medium" in diff:
            if random.random() < 0.4:
                return random.choice(available)

        # Unbeatable (Minimax)
        if len(available) == 9:
            return 4  # Center spot
        best_move = self.minimax(self.board, 0, True, -math.inf, math.inf)
        return best_move["position"]

    def update_scores(self):
        self.score_label_human.config(text=f"You (X): {self.score_human}")
        self.score_label_draw.config(text=f"Ties: {self.score_draws}")
        self.score_label_ai.config(text=f"AI (O): {self.score_ai}")

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.game_over = False
        for btn in self.buttons:
            btn.config(text=" ", fg=self.COLOR_TEXT)
        self.status_label.config(text="Your turn! Click any cell to place 'X'.", fg=self.COLOR_STATUS)


def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
