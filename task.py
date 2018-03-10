import pandas as panda
import json

#subtask1: merging datasets
data1=panda.read_json('https://query.data.world/s/kpf4LLqAll5dYbMpV5WYbXkwQh6Bpq')    #twitter data of 01/11/2017
data2=panda.read_json('https://query.data.world/s/dYtdFJPEQdsAbA8oXDYTQJj0cWWoAR')    #twitter data of 02/11/2017
data3=panda.read_json('https://query.data.world/s/43i9j7GxCK7wCl1InvdLAgLsvEuewx')    #twitter data of 03/11/2017
final_data=panda.concat([data1, data2, data3])                                        #combining into a single dataset


#subtask2: finding accounts referenced trump
trump_refer=final_data[final_data['text'].str.contains("@realDonaldTrump")]           #references to Trump
print("Twitter accounts referring trump:\n")
print(trump_refer)


#subtask3- % of accounts referred trump
no_of_accounts=final_data.groupby('user_id').size().shape
accounts_referring_trump=trump_refer.groupby('user_id').size().shape
trump_accounts=accounts_referring_trump[0]                                        #no. of accounts which referred trump
total=no_of_accounts[0]
percentage= str((float(trump_accounts) / float(total))*100)                       #% of accounts referred Trump
print("% of accounts referenced trump:"+percentage)



#subtask4- user accounts in decreasing order of frequency of tweets
tweet_freq=trump_refer.groupby(['user_id', 'screen_name'])['text'].count()            #no. of tweets mentioning Trump from each account
descend_accounts=str(tweet_freq.nlargest(trump_accounts))                             #getting accounts in decreasing order
print("The accounts in descending order of frequency:\n"+descend_accounts)
