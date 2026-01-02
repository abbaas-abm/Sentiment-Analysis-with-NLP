# Project 2: Sentiment Analysis with NLP

### Project Overview
This project utilizes a pre-trained BERT model from Hugging Face's Transformers library to perform sentiment analysis on text inputs. It classifies text as positive or negative with confidence scores. This demonstrates natural language processing (NLP) and transfer learning, making it a great portfolio addition for NLP enthusiasts.

The script analyzes sample texts and includes an interactive mode for real-time user input.

### Features
- Uses a state-of-the-art pre-trained model (distilbert-base-uncased-finetuned-sst-2-english).
- Analyzes multiple texts in batch.
- Interactive CLI for ongoing sentiment checks.
- Simple and efficient, no training required.

### Requirements
- Python 3.6+
- Transformers (install via `pip install transformers`)
- Torch (install via `pip install torch`)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sentiment-analysis-nlp.git
   cd sentiment-analysis-nlp
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   (Create a `requirements.txt` with: `transformers` and `torch`.)

### Usage
Run the main script:
```
python main.py
```
- It processes sample texts and enters interactive mode.
- Type text to analyze; enter 'quit' to exit.

### How It Works
1. **Model Loading**: Pipeline loads a pre-trained sentiment classifier.
2. **Batch Analysis**: Classifies a list of texts.
3. **Interactive Loop**: Takes user input, predicts sentiment, and responds until quit.

### Example
Snippet for batch analysis:

```python
texts = [
    "I love this product! It's amazing.",
    "This is the worst experience I've ever had.",
    "It's okay, nothing special."
]

results = classifier(texts)

for text, result in zip(texts, results):
    print(f'Text: {text}')
    print(f'Sentiment: {result["label"]}, Score: {result["score"]:.2f}\n')
```

**Sample Output**:
```
Text: I love this product! It's amazing.
Sentiment: POSITIVE, Score: 1.00

Text: This is the worst experience I've ever had.
Sentiment: NEGATIVE, Score: 1.00

Text: It's okay, nothing special.
Sentiment: NEGATIVE, Score: 0.99
```

**Interactive Example**:
```
Enter text for analysis (or 'quit' to exit): This movie was fantastic!
Sentiment: POSITIVE, Score: 1.00

Enter text for analysis (or 'quit' to exit): quit
```

### Performance Notes
- Accuracy: High due to pre-trained model (fine-tuned on SST-2 dataset).
- Inference Time: <1 second per text on CPU.
- Improvements: Fine-tune on custom data or handle multi-label sentiments.

### License
MIT License.

---
