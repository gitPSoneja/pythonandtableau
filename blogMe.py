# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:48:49 2022

@author: psson
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading data from excel files

data=pd.read_excel('articles.xlsx')

data.describe()

data.info()


#counting the no. of articles per source

data.groupby(['source_id'])['article_id'].count()

#number of reactions per pyblisher

data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column

data=data.drop('engagement_comment_plugin_count' , axis=1)

#function

def thisFunction():
    print('This is my name')
    
thisFunction()

def aboutMe(name):
    print('This is my name ' +name)
    
aboutMe('Pooja')


#returning value in a function

def aboutMe(name):
    print('This is my name ' +name)
    return name
    
var=aboutMe('Pooja')

#using loopsin functions

def favfood(food):
    for x in food:
        print('Top Food is '+x)
        
fastfood=['Pizza','burger','Pasta']

favfood(fastfood)

#for loop to isolate each title row

# keyword_flag=[]
# for x in range(0,10):
#     heading=data['title'][x]
#     if 'crash' in heading:
#         flag=1
#     else:
#         flag=0
#     keyword_flag.append(flag)
    
    
  #for loop to isolate each title row (loop inside the function) 
def keywordFlag(keyword):
    length=len(data)
    keyword_flag=[]
    for x in range(0,data):
        heading=data['title'][x]
        if keyword in heading:
            flag=1
        else:
            flag=0
        keyword_flag.append(flag)
    
    
#SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][15]

sent = sent_int.polarity_scores(text)

pos = sent['pos']
neg = sent['neg']
neu = sent['neu']

#adding for loop to get sentiment of each title from the dataframe

title_pos_sentiment = []
title_neg_sentiment = []
title_neu_sentiment = []
sent_int = SentimentIntensityAnalyzer()
length = len(data['title'])

for x in range(0,length):
    try:
        text = data['title'][x]
        sent = sent_int.polarity_scores(text)
        pos = sent['pos']
        neg = sent['neg']
        neu = sent['neu']
    except:
        pos = 0
        neg = 0
        neu = 0
    title_pos_sentiment.append(pos)
    title_neg_sentiment.append(neg)
    title_neu_sentiment.append(neu)

title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_pos_sentiment'] = title_pos_sentiment
data['title_neg_sentiment'] = title_neg_sentiment
data['title_neu_sentiment'] = title_neu_sentiment


data.to_excel('blogme_clean.xlsx', sheet_name = 'blogme_data', index = False)





