import openai

openai.api_key = "your-api-key-here"

def analyze_sentiment(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Analyze the sentiment of this text: {text}"}]
    )
    return response["choices"][0]["message"]["content"]

user_input = input("Enter text for sentiment analysis: ")
print("Sentiment:", analyze_sentiment(user_input))
