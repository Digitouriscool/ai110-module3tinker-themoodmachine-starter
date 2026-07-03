"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "hopeful",
    "proud",
    "grateful",
    "passed",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "exhausted",
    "anxious",
    "stuck",
    "traffic",
    "waiting",
    "late",
    "delayed",
    "annoying",
    "frustrating",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "I am not feeling good",
    "No cap this made my whole day 😂",
    "This meeting could have been an email 💀",
    "Lowkey exhausted but proud I got everything done",
    "I passed the test but I still feel weirdly anxious",
    "Bruh today was actually amazing",
    "Highkey grateful for my friends today :)",
    "Lowkey this pizza fixed my mood",
    "I absolutely love getting stuck in traffic :)",
    "Not gonna lie, I am stressed and excited at the same time",
    "Nothing really happened today",
    "No cap that movie was boring 💀",
    "I miss my old routine but this new job is kind of fun",
    "Finally finished my project 😂",
    "Everything is fine I guess 🥲"
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this",
    "negative", # I am not feeling good
    "positive", # No cap this made my whole day 😂
    "negative", # This meeting could have been an email 💀
    "mixed", # Lowkey exhausted but proud I got everything done
    "mixed", # I passed the test but I still feel weirdly anxious
    "positive", # Bruh today was actually amazing
    "positive", # Highkey grateful for my friends today :)
    "positive", # Lowkey this pizza fixed my mood
    "negative", # I absolutely love getting stuck in traffic :)
    "mixed", # Not gonna lie, I am stressed and excited at the same time
    "neutral", # Nothing really happened today
    "negative", # No cap that movie was boring 💀
    "mixed", # I miss my old routine but this new job is kind of fun
    "positive", # Finally finished my project 😂
    "mixed" # Everything is fine I guess 🥲
]
