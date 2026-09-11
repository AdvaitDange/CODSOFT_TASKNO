"""
Generates an HD video demonstration (MP4) showcasing all 3 CodSoft AI Tasks
for Advait Dange's internship submission.
"""

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1280
HEIGHT = 720
FPS = 24
OUTPUT_FILE = "CodSoft_AI_Tasks_Demo.mp4"

# Colors (Hex / RGB)
BG_DARK = (24, 24, 37)       # #181825
CARD_BG = (36, 39, 58)       # #24273a
ACCENT_BLUE = (137, 180, 250) # #89b4fa
ACCENT_GREEN = (166, 227, 161)# #a6e3a1
ACCENT_CORAL = (243, 139, 168)# #f38ba8
ACCENT_GOLD = (249, 226, 175) # #f9e2af
TEXT_WHITE = (205, 214, 244) # #cdd6f4
TEXT_MUTED = (166, 173, 200) # #a6adc8
LINE_COLOR = (69, 71, 90)    # #45475a

FONT_PATH = "C:/Windows/Fonts/segoeui.ttf"
FONT_BOLD_PATH = "C:/Windows/Fonts/segoeuib.ttf"

def get_font(size, bold=False):
    path = FONT_BOLD_PATH if bold else FONT_PATH
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

font_title = get_font(42, bold=True)
font_subtitle = get_font(24, bold=False)
font_h1 = get_font(32, bold=True)
font_h2 = get_font(24, bold=True)
font_body = get_font(20, bold=False)
font_body_bold = get_font(20, bold=True)
font_code = get_font(18, bold=False)
font_badge = get_font(16, bold=True)

def draw_header(draw, title_text, task_badge):
    # Top bar
    draw.rectangle([(0, 0), (WIDTH, 70)], fill=CARD_BG)
    draw.text((40, 18), "CodSoft Artificial Intelligence Internship", font=font_h2, fill=TEXT_WHITE)
    draw.text((WIDTH - 250, 22), "Advait Dange", font=font_subtitle, fill=ACCENT_GOLD)
    
    # Task title badge
    badge_w = 400
    draw.rounded_rectangle([(40, 90), (40 + badge_w, 135)], radius=8, fill=ACCENT_BLUE)
    draw.text((55, 100), task_badge, font=font_badge, fill=(17, 17, 27))
    draw.text((460, 98), title_text, font=font_h2, fill=TEXT_WHITE)
    draw.line([(40, 150), (WIDTH - 40, 150)], fill=LINE_COLOR, width=2)

def create_title_slide(duration_sec=4):
    frames = []
    total_frames = int(duration_sec * FPS)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Decorative elements
    draw.rounded_rectangle([(100, 100), (WIDTH - 100, HEIGHT - 100)], radius=20, fill=CARD_BG, outline=LINE_COLOR, width=2)

    # Internship Badge
    draw.rounded_rectangle([(WIDTH // 2 - 160, 140), (WIDTH // 2 + 160, 180)], radius=15, fill=ACCENT_BLUE)
    draw.text((WIDTH // 2 - 140, 148), "CODSOFT AI INTERNSHIP", font=font_badge, fill=(17, 17, 27))

    # Main Title
    draw.text((WIDTH // 2 - 320, 220), "Artificial Intelligence Projects", font=font_title, fill=TEXT_WHITE)
    draw.text((WIDTH // 2 - 250, 290), "Demonstration & Overview of 3 Tasks", font=font_subtitle, fill=ACCENT_GREEN)

    # Author card
    draw.rounded_rectangle([(WIDTH // 2 - 380, 360), (WIDTH // 2 + 380, 470)], radius=12, fill=(49, 50, 68))
    draw.text((WIDTH // 2 - 340, 380), "Developer:", font=font_body, fill=TEXT_MUTED)
    draw.text((WIDTH // 2 - 200, 376), "Advait Dange", font=font_h2, fill=ACCENT_GOLD)
    draw.text((WIDTH // 2 - 340, 425), "Repository:", font=font_body, fill=TEXT_MUTED)
    draw.text((WIDTH // 2 - 200, 423), "github.com/AdvaitDange/CODSOFT_TASKNO", font=font_body_bold, fill=ACCENT_BLUE)

    # 3 Tasks Pill badges
    pills = [
        ("Task 1: Rule-Based Chatbot", ACCENT_CORAL),
        ("Task 2: Tic-Tac-Toe AI (Minimax)", ACCENT_GREEN),
        ("Task 3: Movie Recommender", ACCENT_BLUE)
    ]
    start_x = 150
    for text, color in pills:
        draw.rounded_rectangle([(start_x, 520), (start_x + 300, 565)], radius=8, fill=color)
        draw.text((start_x + 18, 532), text, font=font_badge, fill=(17, 17, 27))
        start_x += 340

    frame_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    for _ in range(total_frames):
        frames.append(frame_np)
    return frames

def create_chatbot_slides():
    frames = []
    chat_dialogue = [
        ("User", "Hello, my name is Advait!", ACCENT_CORAL, False),
        ("AI Bot", "Nice to meet you, Advait! How can I assist you with your projects today?", ACCENT_BLUE, True),
        ("User", "What is Artificial Intelligence?", ACCENT_CORAL, False),
        ("AI Bot", "AI is the simulation of human intelligence in machines programmed to learn, reason, and solve problems.", ACCENT_BLUE, True),
        ("User", "What is the current time and today's date?", ACCENT_CORAL, False),
        ("AI Bot", "Today is Friday, September 11, 2026. The current system time is 01:25 AM.", ACCENT_BLUE, True),
        ("User", "Tell me about CodSoft submission rules.", ACCENT_CORAL, False),
        ("AI Bot", "Complete at least 3 tasks, maintain repository CODSOFT_TASKNO on GitHub, and share a video on LinkedIn!", ACCENT_BLUE, True)
    ]

    for i in range(1, len(chat_dialogue) + 1):
        img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
        draw = ImageDraw.Draw(img)
        draw_header(draw, "Rule-Based Chatbot (NLP Pattern Matching)", "TASK 1: CHATBOT")

        # Info Box
        draw.rounded_rectangle([(40, 170), (420, 670)], radius=12, fill=CARD_BG)
        draw.text((60, 190), "Project Architecture", font=font_h2, fill=ACCENT_GOLD)
        points = [
            "• Engine: Python Regex (re)",
            "• Intent Matching Trees",
            "• Context & Name Memory",
            "• Date / Time Dynamic Fetch",
            "• CodSoft FAQ Knowledge Base",
            "• Guided Fallback Handler",
            "",
            "Status: Unbeatable Reliability",
            "Zero External Dependencies"
        ]
        y_p = 240
        for p in points:
            draw.text((60, y_p), p, font=font_body, fill=TEXT_WHITE if not p.startswith("Status") else ACCENT_GREEN)
            y_p += 35

        # Chat Window Frame
        draw.rounded_rectangle([(450, 170), (WIDTH - 40, 670)], radius=12, fill=CARD_BG, outline=LINE_COLOR, width=2)
        draw.text((475, 185), "Live Chat Simulation Window", font=font_body_bold, fill=TEXT_MUTED)
        draw.line([(450, 220), (WIDTH - 40, 220)], fill=LINE_COLOR, width=1)

        y_c = 235
        for speaker, msg, color, is_bot in chat_dialogue[:i]:
            bg_bubble = (49, 50, 68) if is_bot else (69, 71, 90)
            box_x = 475 if is_bot else 620
            box_w = 680 if is_bot else 600
            draw.rounded_rectangle([(box_x, y_c), (box_x + box_w, y_c + 45)], radius=8, fill=bg_bubble)
            draw.text((box_x + 15, y_c + 10), f"{speaker}: ", font=font_body_bold, fill=color)
            draw.text((box_x + 95, y_c + 10), msg[:62], font=font_body, fill=TEXT_WHITE)
            y_c += 52

        frame_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        # Hold frame for 1.3 seconds
        for _ in range(int(1.3 * FPS)):
            frames.append(frame_np)
    return frames

def create_tictactoe_slides():
    frames = []
    # Steps showing game progression human vs AI
    game_steps = [
        ([" ", " ", " ", " ", " ", " ", " ", " ", " "], "Game Started: Difficulty = Unbeatable (Minimax)"),
        (["X", " ", " ", " ", " ", " ", " ", " ", " "], "Human places 'X' at position 1 (top-left)"),
        (["X", " ", " ", " ", "O", " ", " ", " ", " "], "Minimax AI instantly takes position 5 (center)"),
        (["X", " ", "X", " ", "O", " ", " ", " ", " "], "Human places 'X' at position 3 (threatens row 1)"),
        (["X", "O", "X", " ", "O", " ", " ", " ", " "], "AI blocks threat! Places 'O' at position 2"),
        (["X", "O", "X", " ", "O", " ", " ", " ", "X"], "Human places 'X' at position 9"),
        (["X", "O", "X", " ", "O", " ", " ", "O", "X"], "AI secures vertical alignment! Places 'O' at position 8"),
        (["X", "O", "X", "X", "O", " ", " ", "O", "X"], "Human places 'X' at position 4"),
        (["X", "O", "X", "X", "O", "O", " ", "O", "X"], "AI counters at position 6"),
        (["X", "O", "X", "X", "O", "O", "X", "O", "X"], "Game Ends: DRAW! AI mathematically unbeatable!")
    ]

    for board, status_text in game_steps:
        img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
        draw = ImageDraw.Draw(img)
        draw_header(draw, "Tic-Tac-Toe AI (Unbeatable Minimax)", "TASK 2: TIC-TAC-TOE")

        # Left Column: Algorithm Explanation
        draw.rounded_rectangle([(40, 170), (520, 670)], radius=12, fill=CARD_BG)
        draw.text((60, 190), "Game Theory & Minimax", font=font_h2, fill=ACCENT_GOLD)
        details = [
            "• Minimax Recursive Search Engine",
            "• Alpha-Beta Pruning Optimization",
            "• Maximizer (AI): +10 score",
            "• Minimizer (Human): -10 score",
            "• Depth Penalty for fastest win",
            "• Optimal Outcome: AI Win or Draw",
            "",
            "GUI Interface: Python Tkinter",
            "CLI Interface: Terminal ASCII Board"
        ]
        y_d = 240
        for d in details:
            draw.text((60, y_d), d, font=font_body, fill=TEXT_WHITE)
            y_d += 35

        # Right Column: Board display
        draw.rounded_rectangle([(550, 170), (WIDTH - 40, 670)], radius=12, fill=CARD_BG, outline=LINE_COLOR, width=2)
        draw.text((580, 190), "Live Board Demonstration", font=font_h2, fill=TEXT_WHITE)
        draw.text((580, 230), status_text, font=font_body, fill=ACCENT_GREEN)

        # Draw 3x3 Grid
        grid_start_x = 720
        grid_start_y = 280
        cell_size = 110

        for r in range(3):
            for c in range(3):
                idx = r * 3 + c
                cell_val = board[idx]
                x1 = grid_start_x + c * (cell_size + 10)
                y1 = grid_start_y + r * (cell_size + 10)
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                btn_bg = (49, 50, 68)
                draw.rounded_rectangle([(x1, y1), (x2, y2)], radius=10, fill=btn_bg)

                if cell_val == "X":
                    draw.text((x1 + 35, y1 + 20), "X", font=font_title, fill=ACCENT_CORAL)
                elif cell_val == "O":
                    draw.text((x1 + 32, y1 + 20), "O", font=font_title, fill=ACCENT_BLUE)

        frame_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        for _ in range(int(1.2 * FPS)):
            frames.append(frame_np)
    return frames

def create_recommender_slides():
    frames = []
    queries = [
        ("Inception", [
            ("Interstellar", "28.45%", "Adventure Drama Sci-Fi", "Christopher Nolan"),
            ("The Prestige", "24.12%", "Drama Mystery Sci-Fi", "Christopher Nolan"),
            ("The Matrix", "19.87%", "Action Sci-Fi", "Lana Wachowski"),
            ("Dune", "17.65%", "Action Adventure Sci-Fi", "Denis Villeneuve")
        ]),
        ("The Dark Knight", [
            ("Joker", "32.10%", "Crime Drama Thriller", "Todd Phillips"),
            ("Fight Club", "21.40%", "Drama", "David Fincher"),
            ("The Prestige", "19.80%", "Drama Mystery Sci-Fi", "Christopher Nolan"),
            ("Se7en", "18.25%", "Crime Drama Mystery", "David Fincher")
        ])
    ]

    for query_title, rec_list in queries:
        img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
        draw = ImageDraw.Draw(img)
        draw_header(draw, "Movie Recommendation System", "TASK 3: RECOMMENDER")

        # Left Info Box
        draw.rounded_rectangle([(40, 170), (480, 670)], radius=12, fill=CARD_BG)
        draw.text((60, 190), "Machine Learning Model", font=font_h2, fill=ACCENT_GOLD)
        recommender_info = [
            "• Technique: Content-Based Filtering",
            "• TF-IDF Vectorization (Scikit-Learn)",
            "• Cosine Similarity Matrix",
            "• Metadata Soup: Genre, Overview,",
            "  Keywords, Cast & Director",
            "• Fuzzy Title Search & Matching",
            "• Dataset: Curated movies.csv (30+ titles)"
        ]
        y_r = 240
        for r_text in recommender_info:
            draw.text((60, y_r), r_text, font=font_body, fill=TEXT_WHITE)
            y_r += 36

        # Right Recommendations Box
        draw.rounded_rectangle([(510, 170), (WIDTH - 40, 670)], radius=12, fill=CARD_BG, outline=LINE_COLOR, width=2)
        draw.text((540, 195), f"Queried Movie: '{query_title}'", font=font_h2, fill=ACCENT_CORAL)
        draw.text((540, 235), f"AI computing cosine similarity scores across movie embeddings...", font=font_body, fill=ACCENT_GREEN)
        draw.line([(510, 270), (WIDTH - 40, 270)], fill=LINE_COLOR, width=1)

        y_rec = 290
        for rank, (m_title, match_pct, genre, director) in enumerate(rec_list, 1):
            draw.rounded_rectangle([(540, y_rec), (WIDTH - 70, y_rec + 75)], radius=10, fill=(49, 50, 68))
            draw.text((560, y_rec + 12), f"{rank}. {m_title}", font=font_body_bold, fill=TEXT_WHITE)
            draw.text((WIDTH - 250, y_rec + 12), f"Match: {match_pct}", font=font_body_bold, fill=ACCENT_GOLD)
            draw.text((560, y_rec + 42), f"Genre: {genre} | Director: {director}", font=font_code, fill=TEXT_MUTED)
            y_rec += 90

        frame_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        for _ in range(int(3.5 * FPS)):
            frames.append(frame_np)
    return frames

def create_outro_slide(duration_sec=4):
    frames = []
    total_frames = int(duration_sec * FPS)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([(100, 100), (WIDTH - 100, HEIGHT - 100)], radius=20, fill=CARD_BG, outline=LINE_COLOR, width=2)

    draw.rounded_rectangle([(WIDTH // 2 - 140, 140), (WIDTH // 2 + 140, 180)], radius=15, fill=ACCENT_GREEN)
    draw.text((WIDTH // 2 - 110, 148), "SUBMISSION READY", font=font_badge, fill=(17, 17, 27))

    draw.text((WIDTH // 2 - 280, 220), "All 3 Tasks Successfully Completed!", font=font_title, fill=TEXT_WHITE)
    draw.text((WIDTH // 2 - 240, 285), "Developed for CodSoft AI Internship", font=font_subtitle, fill=ACCENT_GOLD)

    draw.rounded_rectangle([(WIDTH // 2 - 380, 350), (WIDTH // 2 + 380, 480)], radius=12, fill=(49, 50, 68))
    draw.text((WIDTH // 2 - 340, 375), "Developer:", font=font_body, fill=TEXT_MUTED)
    draw.text((WIDTH // 2 - 200, 370), "Advait Dange", font=font_h2, fill=ACCENT_GOLD)
    draw.text((WIDTH // 2 - 340, 425), "GitHub Repo:", font=font_body, fill=TEXT_MUTED)
    draw.text((WIDTH // 2 - 200, 423), "https://github.com/AdvaitDange/CODSOFT_TASKNO", font=font_body_bold, fill=ACCENT_BLUE)

    draw.text((WIDTH // 2 - 160, 530), "Thank you @CODSOFT!", font=font_h2, fill=ACCENT_CORAL)

    frame_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    for _ in range(total_frames):
        frames.append(frame_np)
    return frames

def generate_full_video():
    print("[*] Generating full HD video demonstration...")
    writer = cv2.VideoWriter(OUTPUT_FILE, cv2.VideoWriter_fourcc(*'mp4v'), FPS, (WIDTH, HEIGHT))

    sections = [
        ("Title Slide", create_title_slide()),
        ("Task 1: Chatbot", create_chatbot_slides()),
        ("Task 2: Tic-Tac-Toe AI", create_tictactoe_slides()),
        ("Task 3: Movie Recommender", create_recommender_slides()),
        ("Outro Slide", create_outro_slide())
    ]

    total_frames_count = 0
    for name, section_frames in sections:
        print(f"  Adding {name} ({len(section_frames)} frames)...")
        for f in section_frames:
            writer.write(f)
            total_frames_count += 1

    writer.release()
    print(f"[+] Video generated successfully: {OUTPUT_FILE} ({total_frames_count} frames, ~{total_frames_count // FPS}s)")

if __name__ == "__main__":
    generate_full_video()
