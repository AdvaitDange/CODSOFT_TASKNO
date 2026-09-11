"""
CodSoft Artificial Intelligence Internship - Task 1
Project: Rule-Based Chatbot
Author: Advait Dange
Repository: CODSOFT_TASKNO
"""

import re
import random
from datetime import datetime


class RuleBasedChatbot:
    """
    A smart rule-based chatbot utilizing regular expressions and 
    pattern matching to simulate intelligent conversation.
    """

    def __init__(self, bot_name="CodSoft AI Assistant"):
        self.bot_name = bot_name
        self.user_name = None
        self.rules = self._initialize_rules()

    def _initialize_rules(self):
        """
        Defines pattern-to-response mappings categorized by intent.
        """
        return [
            # 1. Greetings
            {
                "intent": "greeting",
                "patterns": [
                    r"\b(hi|hello|hey|greetings|hola|namaste|sup|yo)\b",
                    r"\bgood\s*(morning|afternoon|evening|day)\b"
                ],
                "responses": [
                    "Hello! How can I assist you with your AI tasks today?",
                    "Hey there! Great to meet you. What would you like to explore?",
                    "Greetings! I am ready to answer your questions on AI and tech.",
                    "Hi! Hope you are having a productive day. How can I help?"
                ]
            },

            # 2. Name capture / User introduction
            {
                "intent": "user_name_intro",
                "patterns": [
                    r"\b(?:my name is|i am|call me)\s+([A-Za-z]+)\b"
                ],
                "responses": [
                    "Nice to meet you, {name}! How can I help you today?",
                    "A pleasure to assist you, {name}! What's on your mind?",
                    "Welcome, {name}! Let's talk about Artificial Intelligence!"
                ]
            },

            # 3. Bot Identity & Purpose
            {
                "intent": "identity",
                "patterns": [
                    r"\b(who are you|what is your name|your name|introduce yourself)\b",
                    r"\b(what can you do|your capabilities|your purpose|why were you made)\b"
                ],
                "responses": [
                    f"I am {self.bot_name}, a rule-based AI chatbot built by Advait Dange for the CodSoft AI Internship! I can answer FAQs, discuss AI concepts, tell jokes, and more.",
                    f"I'm {self.bot_name}! I use pattern matching and rule engines to analyze your queries and respond accurately."
                ]
            },

            # 4. CodSoft Internship FAQs
            {
                "intent": "codsoft_faq",
                "patterns": [
                    r"\b(what is codsoft|about codsoft|codsoft internship|tasks|submission)\b",
                    r"\b(certificate|tasksno|linkedin|demo video)\b"
                ],
                "responses": [
                    "CodSoft is an educational platform providing practical tech internships. For the AI track, you complete at least 3 tasks, publish code on GitHub, and post a video demo on LinkedIn!",
                    "Internship requirement: Complete 3 tasks (e.g. Chatbot, Tic-Tac-Toe AI, Recommendation System), submit your GitHub repo, and share a demo video on LinkedIn tagging @CODSOFT."
                ]
            },

            # 5. Artificial Intelligence Concepts
            {
                "intent": "ai_concepts",
                "patterns": [
                    r"\bwhat is (artificial intelligence|ai)\b",
                    r"\bwhat is (machine learning|ml)\b",
                    r"\bwhat is (natural language processing|nlp)\b",
                    r"\bwhat is (deep learning|neural network)\b"
                ],
                "responses": [
                    "Artificial Intelligence (AI) is the simulation of human intelligence in machines programmed to think, learn, and solve problems.",
                    "Machine Learning is a subset of AI that allows systems to learn patterns from data and improve performance without explicit hardcoding.",
                    "Natural Language Processing (NLP) is the branch of AI focused on enabling computers to understand, interpret, and generate human languages.",
                    "Deep Learning uses multi-layered neural networks inspired by the human brain to learn complex representations from massive datasets."
                ]
            },

            # 6. Time and Date inquiries
            {
                "intent": "time_date",
                "patterns": [
                    r"\b(what time is it|current time|tell me the time)\b",
                    r"\b(what is today'?s? date|current date|today'?s? date|what day is it)\b"
                ],
                "responses": [
                    lambda: f"The current system time is {datetime.now().strftime('%I:%M %p')}.",
                    lambda: f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."
                ]
            },

            # 7. Humor & Small Talk
            {
                "intent": "small_talk",
                "patterns": [
                    r"\b(how are you|how'?s? it going|are you fine|how do you do)\b",
                    r"\btell me a joke|make me laugh|joke\b",
                    r"\b(thank you|thanks|great job|awesome|cool)\b"
                ],
                "responses": [
                    "I'm running at optimal performance, thank you for asking! How are you?",
                    "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
                    "Why did the AI go to school? To improve its learning rate! 🤖",
                    "You're very welcome! I'm always happy to help."
                ]
            },

            # 8. Help / Menu
            {
                "intent": "help",
                "patterns": [
                    r"\b(help|commands|options|what can i ask)\b"
                ],
                "responses": [
                    "You can ask me about:\n"
                    "  • Greetings & introductions ('Hello, my name is Advait')\n"
                    "  • AI & ML definitions ('What is AI?', 'Explain Machine Learning')\n"
                    "  • CodSoft internship FAQs ('Tell me about CodSoft', 'Submission rules')\n"
                    "  • Time & Date ('What time is it?', 'Today's date')\n"
                    "  • Jokes & Casual talk ('Tell me a joke', 'How are you?')\n"
                    "  • Exit ('exit' or 'bye')"
                ]
            },

            # 9. Goodbye
            {
                "intent": "goodbye",
                "patterns": [
                    r"\b(bye|goodbye|see you|exit|quit|later)\b"
                ],
                "responses": [
                    "Goodbye! Best of luck with your CodSoft AI internship!",
                    "See you later! Feel free to return if you have more questions.",
                    "Have a wonderful day ahead! Keep coding!"
                ]
            }
        ]

    def respond(self, user_input: str) -> str:
        """
        Processes user query against regular expression rules and returns an answer.
        """
        cleaned_input = user_input.strip()
        if not cleaned_input:
            return "Please enter a message so I can assist you!"

        # Check for user introducing their name
        name_match = re.search(r"\b(?:my name is|i am|call me)\s+([A-Za-z]+)\b", cleaned_input, re.IGNORECASE)
        if name_match:
            self.user_name = name_match.group(1).capitalize()
            return f"Nice to meet you, {self.user_name}! How can I assist you with your projects today?"

        # Match against predefined rule sets
        for rule in self.rules:
            for pattern in rule["patterns"]:
                if re.search(pattern, cleaned_input, re.IGNORECASE):
                    choice = random.choice(rule["responses"])
                    if callable(choice):
                        return choice()
                    if "{name}" in choice:
                        return choice.format(name=self.user_name or "friend")
                    return choice

        # Graceful fallback response
        return (
            "I'm sorry, I didn't quite catch that. Could you please rephrase?\n"
            "Tip: Type 'help' to see sample questions I can answer!"
        )

    def chat_loop(self):
        """
        Interactive command-line loop.
        """
        print("=" * 60)
        print(f"🤖  Welcome to {self.bot_name}!")
        print("    CodSoft AI Internship - Task 1 (Rule-Based Chatbot)")
        print("    Author: Advait Dange | Repository: CODSOFT_TASKNO")
        print("    Type 'help' for suggestions or 'quit'/'bye' to exit.")
        print("=" * 60)

        while True:
            try:
                user_msg = input("\nYou: ")
            except (KeyboardInterrupt, EOFError):
                print("\nExiting. Goodbye!")
                break

            if re.search(r"\b(quit|exit|bye|goodbye)\b", user_msg.strip(), re.IGNORECASE):
                print(f"{self.bot_name}: Goodbye! Have a great day!")
                break

            response = self.respond(user_msg)
            print(f"{self.bot_name}: {response}")


if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.chat_loop()
