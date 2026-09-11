"""
CodSoft Artificial Intelligence Internship - Task 3 (PDF Task 4)
Project: Movie Recommendation System (Content-Based Filtering)
Author: Advait Dange
Repository: CODSOFT_TASKNO
"""

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    """
    Content-based movie recommendation system using TF-IDF vectorization
    and Cosine Similarity on rich movie metadata.
    """

    def __init__(self, dataset_path=None):
        if dataset_path is None:
            dataset_path = os.path.join(os.path.dirname(__file__), "movies.csv")
        self.dataset_path = dataset_path
        self.df = None
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.indices = None
        self._load_and_train()

    def _load_and_train(self):
        """Loads dataset, preprocesses text, and computes similarity matrix."""
        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(f"Dataset not found at {self.dataset_path}")

        self.df = pd.read_csv(self.dataset_path)

        # Fill missing values
        for col in ["title", "genre", "director", "cast", "description", "keywords"]:
            if col in self.df.columns:
                self.df[col] = self.df[col].fillna("")

        # Create combined metadata soup
        # We give weight to genres, keywords, overview, and director
        self.df["content_soup"] = (
            self.df["genre"] + " " +
            self.df["genre"] + " " +  # Repeated to boost genre importance
            self.df["keywords"] + " " +
            self.df["description"] + " " +
            self.df["director"]
        )

        # Initialize TF-IDF Vectorizer (removes English stop words)
        tfidf = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = tfidf.fit_transform(self.df["content_soup"])

        # Compute full Cosine Similarity matrix
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

        # Mapping of lower-case movie titles to dataframe indices
        self.indices = pd.Series(self.df.index, index=self.df["title"].str.lower()).drop_duplicates()

    def find_closest_title(self, query: str):
        """Finds closest matching movie title in the database."""
        query_clean = query.strip().lower()

        # 1. Exact match
        if query_clean in self.indices:
            return self.df.loc[self.indices[query_clean], "title"]

        # 2. Substring match
        matches = [t for t in self.df["title"] if query_clean in t.lower()]
        if matches:
            return matches[0]

        # 3. Word token overlap
        words = set(query_clean.split())
        best_match = None
        best_overlap = 0
        for title in self.df["title"]:
            title_words = set(title.lower().split())
            overlap = len(words.intersection(title_words))
            if overlap > best_overlap:
                best_overlap = overlap
                best_match = title

        return best_match

    def recommend(self, title: str, top_n: int = 5):
        """
        Returns top_n recommended movies similar to the given title.
        """
        matched_title = self.find_closest_title(title)
        if not matched_title:
            return None, []

        idx = self.indices[matched_title.lower()]
        if isinstance(idx, pd.Series):
            idx = idx.iloc[0]

        # Get pairwise similarity scores for this movie with all movies
        sim_scores = list(enumerate(self.cosine_sim[idx]))

        # Sort movies based on similarity score (descending)
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Exclude the queried movie itself (index 0)
        sim_scores = sim_scores[1:top_n + 1]

        recommendations = []
        for i, score in sim_scores:
            movie_row = self.df.iloc[i]
            recommendations.append({
                "title": movie_row["title"],
                "genre": movie_row["genre"],
                "director": movie_row["director"],
                "similarity": round(score * 100, 2),
                "description": movie_row["description"]
            })

        return matched_title, recommendations

    def list_movies(self):
        """Returns list of all available movies in database."""
        return self.df["title"].tolist()

    def interactive_cli(self):
        """Interactive command-line interface."""
        print("=" * 65)
        print("🎬  Movie Recommendation System (Content-Based Filtering AI)")
        print("    CodSoft AI Internship - Task 3 (PDF Task 4)")
        print("    Author: Advait Dange | Repository: CODSOFT_TASKNO")
        print("=" * 65)
        print(f"Total Movies in Database: {len(self.df)}")
        print("Commands: Type a movie name (e.g., 'Inception'), 'list' to view all, or 'exit'.\n")

        while True:
            try:
                user_input = input("Enter a movie you like: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nExiting. Goodbye!")
                break

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "q"]:
                print("Thank you for using Movie Recommender AI!")
                break

            if user_input.lower() == "list":
                print("\n--- Available Movies ---")
                for i, t in enumerate(self.list_movies(), 1):
                    print(f"  {i}. {t}")
                print("------------------------\n")
                continue

            matched_title, results = self.recommend(user_input, top_n=5)

            if not matched_title:
                print(f"❌ No matching movie found for '{user_input}'. Try typing 'list' to see available titles.\n")
                continue

            print(f"\n🎯 Top Recommendations for '{matched_title}':")
            print("-" * 65)
            for rank, rec in enumerate(results, 1):
                print(f"{rank}. {rec['title']} (Match: {rec['similarity']}%)")
                print(f"   Genre: {rec['genre']} | Director: {rec['director']}")
                print(f"   Plot:  {rec['description']}")
                print("-" * 65)
            print()


if __name__ == "__main__":
    recommender = MovieRecommender()
    recommender.interactive_cli()
