### START FUNCTION
def extract_municipality_hashtags(df):
    """
    a function which takes in a pandas dataframe and returns a modified
    dataframe that includes two new columns that contain information about
    the municipality and hashtag of the tweet

    Arg:
        df : takes a pandas dataframe as input

    Result:
        mun_list_2 : returns a column of information about Municipality 
        hashtags   : returns a column of hashtag of the tweet
    """
    #instantiate an empty list for adding splitted tweet as a list
    mun_list = []
    for tweet in df['Tweets']:
        mun_list_2 = []
        [mun_list_2.append(mun_dict[i])for i in mun_dict if i in tweet.split()]
        mun_list.append(mun_list_2)
    #check validity of municipality information in the list
    df['municipality'] = mun_list
    df['municipality'] = df['municipality'].apply(
        lambda a: a
        if len(mun_list) != 0 else np.nan)
    #instantiate an empty list for adding hashtags
    hashtags = []
    for tweet in df['Tweets']:
        hashtags_2 = []
        [hashtags_2.append(j.lower()) for j in tweet.split() if j[0] == '#']
        hashtags.append(hashtags_2)
    #check validity of hashtags in the list
    df['hashtags'] = hashtags
    df['hashtags'] = df['hashtags'].apply(
        lambda x: x
        if len(hashtags) != 0 else np.nan)
    return df


### END FUNCTION
