# Task 2: Tic-Tac-Toe AI (Unbeatable Minimax Algorithm) 🎮

**Author:** Advait Dange  
**Internship Track:** Artificial Intelligence  
**Organization:** CodSoft  
**Repository:** [CODSOFT_TASKNO](https://github.com/AdvaitDange/CODSOFT_TASKNO)

---

## 📌 Project Overview
This project implements an **unbeatable AI agent** that plays Tic-Tac-Toe against a human player for **Task 2** of the CodSoft Artificial Intelligence Internship.

The AI uses the **Minimax Algorithm** enhanced with **Alpha-Beta Pruning**, ensuring it explores all possible future game states and makes the mathematically optimal move every single turn. Under the *Unbeatable* setting, the AI is mathematically impossible to defeat—it will either win or force a draw.

---

## 🧠 How the AI Works: The Minimax Algorithm

The Minimax algorithm is a decision-making rule used in two-player, zero-sum, perfect-information games:
1. **Maximizer (AI - 'O')**: Tries to get the highest score possible ($+10$).
2. **Minimizer (Human - 'X')**: Tries to minimize the AI's score ($-10$).
3. **Draw**: Evaluated as $0$.
4. **Depth Penalty**: Terminal scores subtract/add the depth ($10 - \text{depth}$) so the AI favors winning sooner and prolonging losses.
5. **Alpha-Beta Pruning**: Prunes branches in the game decision tree that are guaranteed not to influence the final decision, significantly cutting down search space.

---

## 🎯 Key Features
- **Dual Interface**:
  - `tictactoe_cli.py`: Fast, clean terminal experience with ASCII grid and input validation.
  - `tictactoe_gui.py`: Polished graphical interface (Tkinter) with dark mode UI, interactive buttons, and real-time score tracker (perfect for LinkedIn video demonstration!).
- **3 Difficulty Modes**:
  - **Easy**: AI makes random moves.
  - **Medium**: AI balances random exploration with smart defenses.
  - **Unbeatable**: AI utilizes full Minimax search; mathematically impossible to defeat.

---

## 🚀 How to Run

### 1. Run the Graphical User Interface (GUI) - *Recommended for Video Demo*
```bash
cd Task_2_Tic_Tac_Toe_AI
python tictactoe_gui.py
```

### 2. Run the Command-Line Interface (CLI)
```bash
cd Task_2_Tic_Tac_Toe_AI
python tictactoe_cli.py
```

---

## 📸 Gameplay Preview

```text
============================================================
🎮  Welcome to Tic-Tac-Toe AI!
    CodSoft AI Internship - Task 2
    Author: Advait Dange | Repository: CODSOFT_TASKNO
============================================================

Select Difficulty Level:
1. Easy (Random)
2. Medium (Hybrid)
3. Unbeatable (Minimax AI)
Enter choice (1-3, default 3): 3
Difficulty set to: UNBEATABLE

  X | 2 | 3
 -----------
  4 | O | 6
 -----------
  7 | 8 | 9

AI (O) is calculating optimal move...
AI placed 'O' at position 3.
```
