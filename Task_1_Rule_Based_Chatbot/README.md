# Task 1: Chatbot with Rule-Based Responses 🤖

**Author:** Advait Dange  
**Internship Track:** Artificial Intelligence  
**Organization:** CodSoft  
**Repository:** [CODSOFT_TASKNO](https://github.com/AdvaitDange/CODSOFT_TASKNO)

---

## 📌 Project Overview
This project is a smart, interactive **Rule-Based Chatbot** developed in Python for **Task 1** of the CodSoft Artificial Intelligence Internship.

The chatbot parses user queries using regular expressions, keyword tokenization, and pattern-matching rules to understand user intents and deliver contextually relevant answers.

---

## 🎯 Key Features
- **Regex & Pattern Matching**: Employs Python's built-in `re` module to accurately detect sentence structures, greetings, and queries.
- **Dynamic Context Awareness**: Recognizes and remembers the user's name throughout the session.
- **Domain-Specific Responses**:
  - Greeting & Small Talk
  - AI & Machine Learning definitions
  - CodSoft Internship FAQs & Submission guidelines
  - Real-time Date and Time lookups
  - Humor & tech jokes
- **Intelligent Fallback**: Gracefully guides the user when an unrecognized query is encountered with suggested commands.
- **Zero External Dependencies**: Runs entirely on Python's standard library.

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd Task_1_Rule_Based_Chatbot
   ```

2. Run the chatbot:
   ```bash
   python chatbot.py
   ```

3. Type your messages in the prompt. Type `help` to see query suggestions or `bye` / `quit` to exit.

---

## 💬 Sample Conversation

```text
============================================================
🤖  Welcome to CodSoft AI Assistant!
    CodSoft AI Internship - Task 1 (Rule-Based Chatbot)
    Author: Advait Dange | Repository: CODSOFT_TASKNO
    Type 'help' for suggestions or 'quit'/'bye' to exit.
============================================================

You: Hello, my name is Advait
CodSoft AI Assistant: Nice to meet you, Advait! How can I assist you with your projects today?

You: What is artificial intelligence?
CodSoft AI Assistant: Artificial Intelligence (AI) is the simulation of human intelligence in machines programmed to think, learn, and solve problems.

You: What time is it?
CodSoft AI Assistant: The current system time is 12:45 AM.

You: Tell me about CodSoft internship
CodSoft AI Assistant: CodSoft is an educational platform providing practical tech internships. For the AI track, you complete at least 3 tasks, publish code on GitHub, and post a video demo on LinkedIn!

You: Tell me a joke
CodSoft AI Assistant: Why do programmers prefer dark mode? Because light attracts bugs! 😄

You: Bye
CodSoft AI Assistant: Goodbye! Have a great day!
```
