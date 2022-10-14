import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

#summary of the data
data.describe()

#summary of the columns
data.info()

#counting the number of articles per source
data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping column
data = data.drop('engagement_comment_plugin_count', axis=1)

#creating a function 
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag=1
            else:
                flag=0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

k=keywordflag('murder')

#creating a new column in data frame
data['keyword_flag'] = pd.Series(k)

#SentimentIntensityAnalyzer

sent_int=SentimentIntensityAnalyzer()
text=data['title'][16]
sent=sent_int.polarity_scores(text)

neg=sent['neg']
pos=sent['pos']
neu=sent['neu']

#adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length=len(data)
for x in range(0,length):
    try:
        text=data['title'][x]
        sent_int=SentimentIntensityAnalyzer()
        sent=sent_int.polarity_scores(text)
        neg=sent['neg']
        pos=sent['pos']
        neu=sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

data['Negative Sentiment'] = pd.Series(title_neg_sentiment)
data['Positive Sentiment'] = pd.Series(title_pos_sentiment) 
data['Neutral Sentiment'] = pd.Series(title_neu_sentiment)

#writing to excel
data.to_excel('blogme_cleaned.xlsx', sheet_name='blogmedata', index = False)
