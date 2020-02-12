def stop_words_remover(df):

    """A function which removes english stop words from a tweet"""

    
    stop_words = stop_words_dict['stopwords']
    result = []
    l1 = df['Tweets']
    for tweet in l1:
        result.append(tweet.lower().split(' '))
    df['Without Stop Words'] = result
    for the_list in df['Without Stop Words']:
        for i in the_list :
            if i in stop_words :
                the_list.remove(i)

    return df