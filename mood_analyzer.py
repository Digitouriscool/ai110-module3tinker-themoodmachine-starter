# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

import re
import unicodedata
from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into normalized tokens.

        Handles:
          - Lowercase text
          - Repeated characters: "soooo" -> "soo"
          - Common emojis and emoticons as separate tokens
          - Full Unicode punctuation removal
        """
        cleaned = text.strip().lower()

        # Normalize long repeated character runs: "soooo" -> "soo".
        cleaned = re.sub(r"(.)\1{2,}", r"\1\1", cleaned)

        emoji_tokens = [":)", ":-)", ":(", ":-(", "😂", "💀", "🥲", "😭", "❤️", "🔥"]
        protected_tokens = {}
        for index, emoji in enumerate(emoji_tokens):
            placeholder = f"emojitoken{index}"
            protected_tokens[placeholder] = emoji
            cleaned = cleaned.replace(emoji, f" {placeholder} ")

        cleaned = "".join(
            " " if unicodedata.category(char).startswith("P") else char
            for char in cleaned
        )

        for placeholder, emoji in protected_tokens.items():
            cleaned = cleaned.replace(placeholder, emoji)

        tokens = cleaned.split()

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        tokens = self.preprocess(text)
        negators = {"not", "never", "no"}
        score = 0

        for index, token in enumerate(tokens):
            value = 0
            if token in self.positive_words:
                value = 1
            elif token in self.negative_words:
                value = -1

            if value and index > 0 and tokens[index - 1] in negators:
                value *= -1

            score += value

        return score

    def count_signals(self, text: str) -> Tuple[int, int]:
        """
        Count positive and negative mood signals after preprocessing.

        Returns:
          - positive_hits: number of positive signals
          - negative_hits: number of negative signals
        """
        tokens = self.preprocess(text)
        negators = {"not", "never", "no"}
        positive_hits = 0
        negative_hits = 0

        for index, token in enumerate(tokens):
            value = 0
            if token in self.positive_words:
                value = 1
            elif token in self.negative_words:
                value = -1

            if value and index > 0 and tokens[index - 1] in negators:
                value *= -1

            if value > 0:
                positive_hits += 1
            elif value < 0:
                negative_hits += 1

        return positive_hits, negative_hits

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        positive_hits, negative_hits = self.count_signals(text)
        score = self.score_text(text)

        if positive_hits > 0 and negative_hits > 0:
            return "mixed"
        if score > 0:
            return "positive"
        if score < 0:
            return "negative"
        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
