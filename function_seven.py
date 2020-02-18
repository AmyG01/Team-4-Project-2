def stop_words_remover(df):

    """A function which removes english stop words from a tweet"""

    
    stop_words = stop_words_dict['stopwords']
    
    df['Without Stop Words'] = [' '.join([w for w in x.lower().split() if w not in stop_words]) 
    for x in df['Tweets'].tolist()]
    
    result = []
    l1 = df['Without Stop Words']
    for tweet in l1:
        result.append(tweet.split(' '))
    df['Without Stop Words'] = result
    
    return df