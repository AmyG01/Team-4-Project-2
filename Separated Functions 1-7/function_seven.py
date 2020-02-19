### START FUNCTION
def stop_words_remover(df):
    """Removes english stop words from a tweet and return in a separate colunm
 
    Args:
        df : Pandas DataFrame

    Returns:
        df : Modified original dataframe returned with a column named
        'Without Stop Words' all words will also be return in lower case
        and will remove English stop words.

    Example:
        >>>df.column_name == @saucy_mamiie Pls log a call on 0860037566
        [@saucy_mamiie, pls, log, 0860037566]
    """
    stop_words = stop_words_dict['stopwords']

    df['Without Stop Words'] = [' '.join([w for w in x.lower().split()
                                if w not in stop_words])
                                for x in df['Tweets'].tolist()
                                ]
    result = []
    l1 = df['Without Stop Words']
    for tweet in l1:
        result.append(tweet.split(' '))
    df['Without Stop Words'] = result
    return df

### END FUNCTION
