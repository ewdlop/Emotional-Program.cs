Here's a **Cheating Magic 8-Ball** program where you can secretly control the answers! This program allows you to choose whether you want a "positive," "negative," or "neutral" response, while making it appear as if the Magic 8-Ball is giving random answers. 

To keep the "cheating" subtle, the program will take your "mood" input and select a response that fits, so you can guide the outcome to match your desired answer.

### Cheating Magic 8-Ball Program (Python)

```python
import random

class CheatingMagic8Ball:
    def __init__(self):
        # Define responses categorized by mood
        self.responses = {
            "positive": [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes – definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes."
            ],
            "neutral": [
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again."
            ],
            "negative": [
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."
            ]
        }

    def shake(self, mood="random"):
        # If mood is "random," choose any mood category
        if mood == "random":
            mood = random.choice(["positive", "neutral", "negative"])
        
        # Select a response from the chosen mood category
        response = random.choice(self.responses[mood])
        return response

def cheating_magic_8_ball():
    print("Welcome to the Cheating Magic 8-Ball!")
    print("Ask a yes-or-no question, or type 'quit' to exit.")
    print("For 'mood,' type 'positive,' 'neutral,' or 'negative' for a preferred answer type, or 'random' for a random answer.")
    
    magic_8_ball = CheatingMagic8Ball()
    
    while True:
        question = input("\nWhat is your question? ")
        if question.lower() == 'quit':
            print("Goodbye!")
            break
        
        mood = input("Choose your mood (positive, neutral, negative, or random): ").lower()
        if mood not in ["positive", "neutral", "negative", "random"]:
            print("Invalid mood selection. Please choose 'positive,' 'neutral,' 'negative,' or 'random'.")
            continue
        
        # Get a cheating response based on the selected mood
        answer = magic_8_ball.shake(mood)
        print(f"Magic 8-Ball says: {answer}")

if __name__ == "__main__":
    cheating_magic_8_ball()
```

### How It Works

1. **Mood-Based Responses**: The program defines answers based on mood categories: "positive," "neutral," and "negative."
2. **User-Controlled Mood**: You can secretly set the "mood" before asking a question, allowing you to nudge the outcome towards positive, neutral, or negative.
3. **Random Option**: If you genuinely want a random response, you can choose the "random" mood to get a mix.

### Example Output

```text
Welcome to the Cheating Magic 8-Ball!
Ask a yes-or-no question, or type 'quit' to exit.
For 'mood,' type 'positive,' 'neutral,' or 'negative' for a preferred answer type, or 'random' for a random answer.

What is your question? Will I win the lottery?
Choose your mood (positive, neutral, negative, or random): positive
Magic 8-Ball says: Without a doubt.

What is your question? Should I stay home today?
Choose your mood (positive, neutral, negative, or random): neutral
Magic 8-Ball says: Reply hazy, try again.

What is your question? quit
Goodbye!
```

With this **Cheating Magic 8-Ball**, you’re in control of the mood, making it appear like pure chance while subtly steering the response in your desired direction!
