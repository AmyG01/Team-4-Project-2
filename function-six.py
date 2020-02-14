### START FUNCTION
def word_splitter(df):
    
    #spliting tweets sentences in Tweets column
    for tweet in df['Tweets']:
        tweet = df['Tweets'].str.split()

    #forming a Series of splited tweets as a list of lists   
    splited_tweets = pd.Series(tweet)

    #adding a new column "Split Tweets" and asigning it to a series "splited_tweets"
    df['Split Tweets'] = splited_tweets

    #converting rows of "Split Tweets" column to lowercase 
    df['Split Tweets']= df['Split Tweets'].astype(str).str.lower()
 
    return df

### END FUNCTION

###### Privious Solution################
# def word_spliter(df):
#   result = []
#   l1 = df['Tweets']
#   for tweet in l1:
#     result.append(tweet.lower().split(' '))
#   df['Split words'] = result
#   return df