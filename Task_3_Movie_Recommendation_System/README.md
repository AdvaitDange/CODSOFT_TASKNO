# Task 3: Movie Recommendation System (Content-Based Filtering) 🎬

**Author:** Advait Dange  
**Internship Track:** Artificial Intelligence  
**Organization:** CodSoft  
**Repository:** [CODSOFT_TASKNO](https://github.com/AdvaitDange/CODSOFT_TASKNO)

---

## 📌 Project Overview
This project implements an intelligent **Content-Based Movie Recommendation System** for **Task 4 (selected as 3rd Task)** of the CodSoft Artificial Intelligence Internship.

The system suggests relevant movies to users based on textual metadata (genres, plot synopsis, director, cast, and keywords) by computing vector embeddings with **TF-IDF (Term Frequency - Inverse Document Frequency)** and ranking similarities using **Cosine Similarity**.

---

## 🧠 Machine Learning Methodology

### 1. Feature Representation & Soup Construction
Metadata fields (`genre`, `keywords`, `description`, `director`) are preprocessed, lowercased, and combined into a unified content vector representation.

### 2. TF-IDF Vectorization
The text is transformed into a high-dimensional sparse matrix of TF-IDF word importance scores:
$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$
where words common across all movies (e.g., "the", "movie", "man") are penalized, while distinct identifiers (e.g., "superhero", "subconscious", "mafia") are emphasized.

### 3. Cosine Similarity Metric
The similarity between movie $A$ and movie $B$ is computed as the cosine of the angle between their vector representations:
$$\text{Cosine Similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$

---

## 🎯 Key Features
- **Curated Dataset**: Includes top-rated diverse titles across genres (`movies.csv`).
- **Fuzzy Title Search**: Resolves partial or lowercase queries (e.g. typing `"dark knight"` automatically resolves to `"The Dark Knight"`).
- **Match Percentage Scores**: Displays similarity confidence percentages for each recommendation.
- **Rich Output Details**: Displays genre, director, and plot overview for each recommendation.

---

## 🚀 How to Run

1. Navigate to the project folder:
   ```bash
   cd Task_3_Movie_Recommendation_System
   ```

2. Run the recommender:
   ```bash
   python recommender.py
   ```

3. Type a movie name (e.g., `Inception`, `The Dark Knight`, `Interstellar`, or `The Matrix`) to see recommendations. Type `list` to view all available movies or `exit` to quit.

---

## 📸 Sample Output

```text
=================================================================
🎬  Movie Recommendation System (Content-Based Filtering AI)
    CodSoft AI Internship - Task 3 (PDF Task 4)
    Author: Advait Dange | Repository: CODSOFT_TASKNO
=================================================================
Total Movies in Database: 30
Commands: Type a movie name (e.g., 'Inception'), 'list' to view all, or 'exit'.

Enter a movie you like: Inception

🎯 Top Recommendations for 'Inception':
-----------------------------------------------------------------
1. Interstellar (Match: 28.45%)
   Genre: Adventure Drama Sci-Fi | Director: Christopher Nolan
   Plot:  A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival as Earth faces famine.
-----------------------------------------------------------------
2. The Prestige (Match: 24.12%)
   Genre: Drama Mystery Sci-Fi | Director: Christopher Nolan
   Plot:  After a tragic accident two stage magicians in 1890s London engage in a battle to create the ultimate illusion while sacrificing everything they have to outwit each other.
-----------------------------------------------------------------
3. The Matrix (Match: 19.87%)
   Genre: Action Sci-Fi | Director: Lana Wachowski
   Plot:  When a beautiful stranger leads computer hacker Neo to a forbidding underworld he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.
-----------------------------------------------------------------
```
