### START FUNCTION
def word_splitter(df):
    """
    Splits the sentences of a specific dataframe column into a list of the
    separate words

    Arg :
        df : Pandas Dataframe

    Returns :
        df : Modified original dataframe where the specific column sentences
        are now a list of seperated lowercase words

    Example :
        >>>df.column_name = @ArthurGodbeer Is the power restored as yet?
        [@arthurgodbeer, is, the, power, restored, as, yet, ?]
    """
    result = []
    l1 = df['Tweets']
    for tweet in l1:
        result.append(tweet.lower().split(' '))
    df['Split Tweets'] = result
    return df

### END FUNCTION
