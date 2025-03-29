from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import Tuple  

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert").to(device)
labels = ["positive", "negative", "neutral"]

@torch.inference_mode()  # Disables gradient tracking for faster inference
def estimate_sentiment(news):
    if not news:
        return 0, "neutral"

    # Tokenize and move inputs to the correct device
    tokens = tokenizer(news, return_tensors="pt", padding=True, truncation=True).to(device)

    # Run model inference
    logits = model(**tokens).logits  
    probs = torch.nn.functional.softmax(logits, dim=-1).mean(dim=0)  # Average sentiment scores

    # Get sentiment with the highest probability
    max_idx = torch.argmax(probs)
    probability = probs[max_idx].item()
    sentiment = labels[max_idx]

    return probability, sentiment

# Example test
if __name__ == "__main__":
    tensor, sentiment = estimate_sentiment(['Markets responded negatively to the news!', 'Traders were displeased!'])
    print(tensor, sentiment)
    print("CUDA Available:", torch.cuda.is_available())