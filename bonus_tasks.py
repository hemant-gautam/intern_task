import json
import pandas as panda
import re
from textblob import TextBlob


data1 = panda.read_json('https://query.data.world/s/kpf4LLqAll5dYbMpV5WYbXkwQh6Bpq')     # 1/11/2017 data
data2 = panda.read_json('https://query.data.world/s/dYtdFJPEQdsAbA8oXDYTQJj0cWWoAR')     # 2/11/2017 data
data3 = panda.read_json('https://query.data.world/s/43i9j7GxCK7wCl1InvdLAgLsvEuewx')     # 3/11/2017 data

data1_list = data1.values.tolist()
data2_list = data2.values.tolist()
data3_list = data3.values.tolist()
comb = [data1_list, data2_list, data3_list]
data = sum(comb, [])


#bonus question1:
no = 0
tag = "@realDonaldTrump"
tw=0

def sent_analyze(text):                                  # function for sentimental analysis
    analysis = TextBlob(text_trim(text))
    if analysis.sentiment.polarity > 0:
        return 1
    else:
        return 0

def text_trim(text):                        #function for text trimming and cleaning
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|(\w+:\/\/\S+)|([^0-9A-Za-z \t])", " ", text).split())

tweets = []
counts = []

for text in data:
    i = 0
    if tag in text[4]:
        trimmed_text = text_trim(text[4])
        i = sent_analyze(trimmed_text)
        if (i == 1):
            no = no + 1
        tweets.append(text[6])
        counts.append(i)

n=len(tweets)
t = str((float(no) / float(n)) * 100)
print("% of positive tweets "+t)


#bonus question2:
data = panda.DataFrame({'id':tweets,'number':counts},dtype=float)    #new dataset having users and their tweets count
data_mean=data.groupby(['id']).mean()                                     #mean number of tweets
size=len(data_mean)
for i in range(0,size):
    if(int(data_mean.iloc[i,0:1])>0.5):                                   #whether mean > or < 0.5
        tw=tw+1

users=str((float(tw)/float(size))*100)
print("% of accounts with more than 50% positive tweets about Donald Trump. "+users)



