from transformers import pipeline

# Load pre-trained sentiment analysis model
classifier = pipeline('sentiment-analysis')

# Sample texts
texts = [
    "I love this product! It's amazing.",
    "This is the worst experience I've ever had.",
    "It's okay, nothing special."
]

# Perform sentiment analysis
results = classifier(texts)

# Display results
for text, result in zip(texts, results):
    print(f'Text: {text}')
    print(f'Sentiment: {result["label"]}, Score: {result["score"]:.2f}\n')

# Interactive mode
while True:
    user_input = input("Enter text for analysis (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    result = classifier(user_input)[0]
    print(f'Sentiment: {result["label"]}, Score: {result["score"]:.2f}\n')