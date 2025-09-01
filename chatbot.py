import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openrouter_api import query_openrouter

class FAQChatbot:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

        # Normalize column names
        self.data.columns = self.data.columns.str.strip().str.lower()

        # Rename to expected names
        self.data.rename(columns={"question": "expanded_question"}, inplace=True)

        required_cols = {"expanded_question", "answer"}
        if not required_cols.issubset(self.data.columns):
            raise ValueError(f"CSV must contain columns: {required_cols}")

        # Information retrieval setup
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.data["expanded_question"])

    def retrieve_relevant_answer(self, user_input):
        user_vector = self.vectorizer.transform([user_input])
        similarities = cosine_similarity(user_vector, self.question_vectors).flatten()
        top_idx = similarities.argmax()
        if similarities[top_idx] < 0.3:
            return None  # Confidence too low
        return self.data.iloc[top_idx]["answer"], self.data.iloc[top_idx]["expanded_question"]

    def generate_answer(self, user_input):
        retrieved = self.retrieve_relevant_answer(user_input)

        # If no strong match, use LLM directly
        if retrieved is None:
            return query_openrouter(user_input)

        # RAG: combine IR + LLM
        context, matched_q = retrieved
        prompt = f"""You are an intelligent FAQ assistant. 
Use the following retrieved answer to respond to the user query.
Retrieved Answer: "{context}"
User's Question: "{user_input}"
Please respond clearly."""
        return query_openrouter(prompt)
