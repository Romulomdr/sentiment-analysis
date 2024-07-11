import praw
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import config

# Configurar a API do Reddit
reddit = praw.Reddit(
    client_id = config.CLIENTE_ID,
    client_secret = config.CLIENT_SECRET,
    user_agent = config.USER_AGENT
)

# Função para coletar comentários de uma postagem específica
def get_reddit_comments(submission_id):
    submission = reddit.submission(id=submission_id)
    submission.comments.replace_more(limit=100) 
    comments = []
    for comment in submission.comments.list():
        comments.append(comment.body)
    return comments

# Exemplo de uso https://www.reddit.com/r/cats/comments/1dz9kj4/found_this_baby_car_in_the_road_i_couldnt_leave/#lightbox
submission_id = '1dz9kj4'
comments = get_reddit_comments(submission_id)
df_comments = pd.DataFrame(comments, columns=['comment'])
df_comments.to_csv('reddit_comments.csv', index=False)

nltk.download('punkt')
nltk.download('stopwords')

# Carregar comentários
df_comments = pd.read_csv('reddit_comments.csv')

# Função para limpar texto
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

df_comments['cleaned_comment'] = df_comments['comment'].apply(clean_text)
df_comments.to_csv('cleaned_reddit_comments.csv', index=False)

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores['compound']

df_comments['sentiment_score'] = df_comments['cleaned_comment'].apply(analyze_sentiment)
df_comments.to_csv('sentiment_reddit_comments.csv', index=False)

# Carregar comentários analisados
df_comments = pd.read_csv('sentiment_reddit_comments.csv')

# Plotar distribuição dos sentimentos
plt.figure(figsize=(10, 6))
sns.histplot(df_comments['sentiment_score'], bins=20, kde=True)
plt.title('Distribuição dos Sentimentos dos Comentários no Reddit')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()