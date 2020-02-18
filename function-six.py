### START FUNCTION
def word_splitter(d):
    
    """A function which splits the sentences in a dataframe's column into a list of the separate words"""
    
    result = []
    l1 = df['Tweets']
    for tweet in l1:
         result.append(tweet.lower().split(' '))
    df['Split Tweets'] = result
    return df
