# utils.py

import re
import pickle
import os

# Load Label Encoder
with open(os.path.join("models", "label_encoder.pkl"), "rb") as f:
    label_encoder = pickle.load(f)

def clean_resume(text):
    """
    Cleans the input resume text by removing URLs, special characters,
    numbers, and converting to lowercase.
    """
    text = re.sub(r"http\S+", " ", text)  # remove URLs
    text = re.sub(r"RT|cc", " ", text)  # remove retweets
    text = re.sub(r"#\S+", "", text)  # remove hashtags
    text = re.sub(r"@\S+", " ", text)  # remove mentions
    text = re.sub(r"[%s]" % re.escape("""!"$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""), " ", text)  # punctuation
    text = re.sub(r"[^\x00-\x7f]", r" ", text)  # non-ASCII chars
    text = re.sub(r"\s+", " ", text)  # extra spaces
    text = re.sub(r"\d+", "", text)  # remove numbers
    return text.lower()
