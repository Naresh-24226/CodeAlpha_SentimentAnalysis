import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("excel/reviews.csv")
# View dataset
print(df.head())
# Sentiment function
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(get_sentiment)
# Print result
print(df)
# Visualization
sns.countplot(x="Sentiment", data=df)
plt.title("Sentiment Analysis")
plt.show()
# Save output
df.to_csv("sentiment_output.csv", index=False)
print("Sentiment Analysis Completed")