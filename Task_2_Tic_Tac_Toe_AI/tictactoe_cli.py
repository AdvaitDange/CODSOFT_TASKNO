"""
CodSoft Artificial Intelligence Internship - Task 2
Project: Tic-Tac-Toe AI with Minimax Algorithm (CLI Version)
Author: Advait Dange
Repository: CODSOFT_TASKNO
"""

import math
import random


class TicTacToeAI:
    """
    Tic-Tac-Toe game engine powered by the Minimax algorithm
    with Alpha-Beta pruning for unbeatable AI gameplay.
    """

    def __init__(self):
        # 3x3 board represented as a 1D list of length 9
        self.board = [" " for _ in range(9)]
        self.human = "X"
        self.ai = "O"

    def print_board(self):
        """Displays current board with coordinates."""
        print()
        for i in range(3):
            row = [self.board[i * 3 + j] if self.board[i * 3 + j] != " " else str(i * 3 + j + 1) for j in range(3)]
            print(f"  {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print(" -----------")
        print()

    def available_moves(self):
        """Returns list of available indices (0-8)."""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, index, letter):
        """Places a move on the board."""
        if self.board[index] == " ":
            self.board[index] = letter
            return True
        return False

    def check_winner(self, board_state, player):
        """Checks if the given player has won the game."""
        win_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        return any(all(board_state[i] == player for i in combo) for combo in win_combos)

    def is_board_full(self, board_state):
        """Checks if the board has no empty spots left."""
        return " " not in board_state

    def minimax(self, board_state, depth, is_maximizing, alpha, beta):
        """
        Minimax decision algorithm with Alpha-Beta Pruning.
        Returns:
            dict with 'position' and 'score'
        """
        # Terminal evaluation
        if self.check_winner(board_state, self.ai):
            return {"position": None, "score": 10 - depth}
        elif self.check_winner(board_state, self.human):
            return {"position": None, "score": depth - 10}
        elif self.is_board_full(board_state):
            return {"position": None, "score": 0}

        empty_indices = [i for i, spot in enumerate(board_state) if spot == " "]

        if is_maximizing:
            best = {"position": None, "score": -math.inf}
            for move in empty_indices:
                board_state[move] = self.ai
                sim_score = self.minimax(board_state, depth + 1, False, alpha, beta)
                board_state[move] = " "  # Backtrack
                sim_score["position"] = move

                if sim_score["score"] > best["score"]:
                    best = sim_score

                alpha = max(alpha, best["score"])
                if beta <= alpha:
                    break  # Alpha-beta cutoff
            return best
        else:
            best = {"position": None, "score": math.inf}
            for move in empty_indices:
                board_state[move] = self.human
                sim_score = self.minimax(board_state, depth + 1, True, alpha, beta)
                board_state[move] = " "  # Backtrack
                sim_score["position"] = move

                if sim_score["score"] < best["score"]:
                    best = sim_score

                beta = min(beta, best["score"])
                if beta <= alpha:
                    break  # Alpha-beta cutoff
            return best

    def get_ai_move(self, difficulty="unbeatable"):
        """Returns the move index chosen by the AI according to difficulty."""
        available = self.available_moves()
        if not available:
            return None

        if difficulty == "easy":
            return random.choice(available)

        if difficulty == "medium":
            # 50% optimal, 50% random
            if random.random() < 0.5:
                return random.choice(available)

        # Unbeatable: Full Minimax search
        # If board is completely empty, pick center or corner for instant first move
        if len(available) == 9:
            return 4  # Center spot

        best_move = self.minimax(self.board, 0, True, -math.inf, math.inf)
        return best_move["position"]

    def play(self):
        """Main game loop for terminal play."""
        print("=" * 60)
        print("🎮  Welcome to Tic-Tac-Toe AI!")
        print("    CodSoft AI Internship - Task 2")
        print("    Author: Advait Dange | Repository: CODSOFT_TASKNO")
        print("=" * 60)

        # Choose Difficulty
        print("\nSelect Difficulty Level:")
        print("1. Easy (Random)")
        print("2. Medium (Hybrid)")
        print("3. Unbeatable (Minimax AI)")
        diff_choice = input("Enter choice (1-3, default 3): ").strip()
        difficulty = {"1": "easy", "2": "medium"}.get(diff_choice, "unbeatable")
        print(f"Difficulty set to: {difficulty.upper()}")

        # Choose symbol
        symbol_choice = input("\nChoose your symbol [X / O] (Default X goes first): ").strip().upper()
        if symbol_choice == "O":
            self.human = "O"
            self.ai = "X"
            current_turn = "AI"
        else:
            self.human = "X"
            self.ai = "O"
            current_turn = "Human"

        print(f"\nYou are '{self.human}' and AI is '{self.ai}'.")
        print("Grid positions are numbered 1 to 9 as shown below:")
        self.print_board()

        while True:
            if current_turn == "Human":
                # Human player move
                valid = False
                while not valid:
                    try:
                        move_input = input(f"Enter your move (1-9) [{self.human}]: ")
                        pos = int(move_input) - 1
                        if pos in self.available_moves():
                            self.make_move(pos, self.human)
                            valid = True
                        else:
                            print("That cell is already taken or out of range. Choose an empty cell (1-9).")
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 9.")

                self.print_board()

                if self.check_winner(self.board, self.human):
                    print("🎉 Congratulations! You won! (Incredible feat against Minimax!)")
                    break

                if self.is_board_full(self.board):
                    print("🤝 It's a DRAW! Well played!")
                    break

                current_turn = "AI"

            else:
                # AI move
                print(f"AI ({self.ai}) is calculating optimal move...")
                ai_move = self.get_ai_move(difficulty)
                self.make_move(ai_move, self.ai)
                print(f"AI placed '{self.ai}' at position {ai_move + 1}.")
                self.print_board()

                if self.check_winner(self.board, self.ai):
                    print("🤖 AI WINS! Minimax remains undefeated!")
                    break

                if self.is_board_full(self.board):
                    print("🤝 It's a DRAW! Well played!")
                    break

                current_turn = "Human"

        print("\nThank you for playing!")


if __name__ == "__main__":
    game = TicTacToeAI()
    game.play()
