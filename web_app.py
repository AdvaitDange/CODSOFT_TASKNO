"""
CodSoft Artificial Intelligence Internship - Web Dashboard
Author: Advait Dange
Repository: https://github.com/AdvaitDange/CODSOFT_TASKNO

Interactive Web Application to run all 3 tasks in Google Chrome:
- Task 1: Rule-Based Chatbot (NLP Pattern Matching)
- Task 2: Tic-Tac-Toe AI (Unbeatable Minimax Algorithm)
- Task 3: Movie Recommendation System (TF-IDF & Cosine Similarity)
"""

import sys
import os
import math
import random
import streamlit as st

# Add workspace directory to python path for module imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Task_1_Rule_Based_Chatbot.chatbot import RuleBasedChatbot
from Task_2_Tic_Tac_Toe_AI.tictactoe_cli import TicTacToeAI
from Task_3_Movie_Recommendation_System.recommender import MovieRecommender

# Page Configuration
st.set_page_config(
    page_title="CodSoft AI Internship - Advait Dange",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #89b4fa;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #a6adc8;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: #1e1e2e;
        border: 1px solid #313244;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .badge {
        background-color: #89b4fa;
        color: #11111b;
        padding: 0.2rem 0.6rem;
        border-radius: 5px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/328119050?v=4", width=90)
    st.title("Advait Dange")
    st.markdown("**CodSoft AI Intern**")
    st.markdown("🌐 [GitHub Profile](https://github.com/AdvaitDange)")
    st.markdown("📁 [Repository: CODSOFT_TASKNO](https://github.com/AdvaitDange/CODSOFT_TASKNO)")
    st.divider()

    selected_page = st.radio(
        "Select Task to Explore:",
        [
            "🤖 Task 1: Rule-Based Chatbot",
            "🎮 Task 2: Tic-Tac-Toe AI (Minimax)",
            "🎬 Task 3: Movie Recommendation System",
            "📄 Project Portfolio & LinkedIn Template"
        ]
    )

    st.divider()
    st.caption("CodSoft Artificial Intelligence Internship")
    st.caption("Organization: @CODSOFT")


# ----------------- TASK 1: CHATBOT -----------------
if selected_page == "🤖 Task 1: Rule-Based Chatbot":
    st.markdown("<div class='main-header'>🤖 Task 1: Rule-Based Chatbot</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Conversational NLP Assistant using Regular Expression Pattern Matching & Intent Classification</div>", unsafe_allow_html=True)

    # Initialize chatbot in session state
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = RuleBasedChatbot()

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Hello! I am your CodSoft AI Assistant built by Advait Dange. How can I assist you with your AI projects today?"}
        ]

    # Suggestion chips
    st.write("**Quick Prompts:**")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    prompt_to_send = None
    if col1.button("👋 Introduce: Advait"):
        prompt_to_send = "Hello, my name is Advait"
    if col2.button("🧠 What is AI?"):
        prompt_to_send = "What is artificial intelligence?"
    if col3.button("⏰ Current Time"):
        prompt_to_send = "What time is it?"
    if col4.button("📋 CodSoft Info"):
        prompt_to_send = "Tell me about CodSoft internship"
    if col5.button("😄 Tell me a Joke"):
        prompt_to_send = "Tell me a joke"

    # Display chat history
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"], avatar="🤖" if msg["role"] == "assistant" else "👤"):
            st.markdown(msg["content"])

    # Chat input
    user_input = st.chat_input("Type your question or query here (or click a quick prompt above)...")
    if prompt_to_send:
        user_input = prompt_to_send

    if user_input:
        st.session_state.chat_messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)

        response = st.session_state.chatbot.respond(user_input)
        st.session_state.chat_messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(response)

    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Chat history cleared! How can I assist you?"}
        ]
        st.rerun()


# ----------------- TASK 2: TIC-TAC-TOE AI -----------------
elif selected_page == "🎮 Task 2: Tic-Tac-Toe AI (Minimax)":
    st.markdown("<div class='main-header'>🎮 Task 2: Tic-Tac-Toe AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Unbeatable Game Agent powered by the Minimax Search Algorithm with Alpha-Beta Pruning</div>", unsafe_allow_html=True)

    # Initialize game state in session
    if "ttt_board" not in st.session_state:
        st.session_state.ttt_board = [" " for _ in range(9)]
        st.session_state.ttt_game_over = False
        st.session_state.ttt_status = "Your turn! Click any cell to place 'X'."
        st.session_state.ttt_scores = {"Human": 0, "AI": 0, "Draws": 0}
        st.session_state.ttt_engine = TicTacToeAI()

    # Top Controls & Scoreboard
    col_c1, col_c2, col_c3, col_c4 = st.columns([2, 1, 1, 1])
    with col_c1:
        difficulty = st.selectbox(
            "Select AI Difficulty:",
            ["Unbeatable (Minimax AI)", "Medium", "Easy"],
            index=0
        )
    with col_c2:
        st.metric("You (X)", st.session_state.ttt_scores["Human"])
    with col_c3:
        st.metric("Ties / Draws", st.session_state.ttt_scores["Draws"])
    with col_c4:
        st.metric("AI (O)", st.session_state.ttt_scores["AI"])

    st.info(f"**Status:** {st.session_state.ttt_status}")

    # Board layout
    board_container = st.container()
    with board_container:
        _, center_col, _ = st.columns([1, 1.2, 1])
        with center_col:
            for r in range(3):
                b_cols = st.columns(3)
                for c in range(3):
                    idx = r * 3 + c
                    spot = st.session_state.ttt_board[idx]
                    
                    label = " " if spot == " " else ("❌" if spot == "X" else "⭕")
                    
                    if b_cols[c].button(
                        label,
                        key=f"cell_{idx}",
                        disabled=(spot != " " or st.session_state.ttt_game_over),
                        use_container_width=True
                    ):
                        # Player Move
                        st.session_state.ttt_board[idx] = "X"
                        engine = st.session_state.ttt_engine

                        # Check Player Win
                        if engine.check_winner(st.session_state.ttt_board, "X"):
                            st.session_state.ttt_status = "🎉 Incredible! You won against the AI!"
                            st.session_state.ttt_scores["Human"] += 1
                            st.session_state.ttt_game_over = True
                            st.balloons()
                            st.rerun()

                        # Check Draw
                        if engine.is_board_full(st.session_state.ttt_board):
                            st.session_state.ttt_status = "🤝 It's a DRAW! Well played!"
                            st.session_state.ttt_scores["Draws"] += 1
                            st.session_state.ttt_game_over = True
                            st.rerun()

                        # AI Move
                        diff_key = "easy" if "Easy" in difficulty else ("medium" if "Medium" in difficulty else "unbeatable")
                        engine.board = st.session_state.ttt_board.copy()
                        ai_move = engine.get_ai_move(diff_key)

                        if ai_move is not None:
                            st.session_state.ttt_board[ai_move] = "O"
                            if engine.check_winner(st.session_state.ttt_board, "O"):
                                st.session_state.ttt_status = "🤖 AI Wins! Minimax Algorithm remains undefeated!"
                                st.session_state.ttt_scores["AI"] += 1
                                st.session_state.ttt_game_over = True
                            elif engine.is_board_full(st.session_state.ttt_board):
                                st.session_state.ttt_status = "🤝 It's a DRAW! Well played!"
                                st.session_state.ttt_scores["Draws"] += 1
                                st.session_state.ttt_game_over = True
                            else:
                                st.session_state.ttt_status = f"AI placed 'O' at spot {ai_move + 1}. Your turn!"
                        
                        st.rerun()

    # Restart button
    if st.button("🔄 Restart Game Board", use_container_width=True):
        st.session_state.ttt_board = [" " for _ in range(9)]
        st.session_state.ttt_game_over = False
        st.session_state.ttt_status = "New game started! Click any cell to place 'X'."
        st.rerun()


# ----------------- TASK 3: MOVIE RECOMMENDER -----------------
elif selected_page == "🎬 Task 3: Movie Recommendation System":
    st.markdown("<div class='main-header'>🎬 Task 3: Movie Recommendation System</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Content-Based Machine Learning Recommender using TF-IDF Vectorization & Cosine Similarity</div>", unsafe_allow_html=True)

    if "recommender" not in st.session_state:
        st.session_state.recommender = MovieRecommender()

    rec_engine = st.session_state.recommender
    all_movies = rec_engine.list_movies()

    col_m1, col_m2 = st.columns([3, 1])
    with col_m1:
        selected_movie = st.selectbox(
            "Select or Type a Movie You Enjoy:",
            all_movies,
            index=all_movies.index("Inception") if "Inception" in all_movies else 0
        )
    with col_m2:
        top_n = st.slider("Number of Recommendations:", min_value=3, max_value=8, value=5)

    if st.button("🎯 Generate Recommendations", use_container_width=True):
        matched_title, recommendations = rec_engine.recommend(selected_movie, top_n=top_n)

        st.subheader(f"Recommendations based on '{matched_title}':")
        for rank, rec in enumerate(recommendations, 1):
            with st.container():
                st.markdown(f"### {rank}. {rec['title']} &nbsp; <span class='badge'>Match: {rec['similarity']}%</span>", unsafe_allow_html=True)
                st.progress(float(rec['similarity']) / 100.0)
                st.write(f"🎭 **Genre:** {rec['genre']} &nbsp;|&nbsp; 🎬 **Director:** {rec['director']}")
                st.write(f"📖 **Synopsis:** {rec['description']}")
                st.divider()


# ----------------- OVERVIEW & LINKEDIN -----------------
else:
    st.markdown("<div class='main-header'>📄 Internship Overview & Submission Assets</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Advait Dange | CodSoft Artificial Intelligence Internship</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📌 Completed Tasks")
        st.markdown("""
        * **Task 1: Rule-Based Chatbot**
          - Natural Language Processing, Regex intent matching trees, date/time logic, and guided fallbacks.
        * **Task 2: Tic-Tac-Toe AI (Unbeatable Minimax)**
          - Adversarial game search, Alpha-Beta pruning, optimal decision-making.
        * **Task 3: Movie Recommendation System**
          - Content-based machine learning, TF-IDF vectorization, Cosine similarity metric.
        """)
        st.markdown(f"📁 **GitHub Repository:** [https://github.com/AdvaitDange/CODSOFT_TASKNO](https://github.com/AdvaitDange/CODSOFT_TASKNO)")

    with col2:
        st.write("### 📲 LinkedIn Submission Template")
        linkedin_text = (
            "🚀 Excited to share my Artificial Intelligence Internship projects with CodSoft!\n\n"
            "During this internship, I developed 3 core AI projects:\n\n"
            "1️⃣ Rule-Based Chatbot: NLP conversational assistant built with regex pattern matching and intent classification.\n"
            "2️⃣ Tic-Tac-Toe AI: Unbeatable game agent utilizing the Minimax algorithm and Alpha-Beta Pruning with an interactive GUI.\n"
            "3️⃣ Movie Recommendation System: Machine Learning recommender utilizing TF-IDF Vectorization and Cosine Similarity metrics.\n\n"
            "📂 GitHub Repository: https://github.com/AdvaitDange/CODSOFT_TASKNO\n\n"
            "A big thank you to @CODSOFT for this wonderful learning opportunity!\n\n"
            "#codsoft #internship #artificialintelligence #machinelearning #python #developer"
        )
        st.text_area("Copy and paste to LinkedIn:", linkedin_text, height=220)
