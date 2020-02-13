### START FUNCTION
def extract_municipality_hashtags(df):

  """a function which takes in a pandas dataframe and returns a modified dataframe that includes two
   new columns that contain information about the municipality and hashtag of the tweet"""

   mun_list = []
   
    for tweet in df['Tweets'] :
        mun_list_2 = []
        [mun_list_2.append(mun_dict[i]) for i in mun_dict if i in tweet.split()]
        mun_list.append(mun_list_2)

    df['municipality'] = mun_list
    df['municipality'] = df['municipality'].apply(lambda mun_list : mun_list if len(mun_list) != 0 else np.nan)

    hashtags = []
    
    for tweet in df['Tweets'] :
        hashtags_2 = []
        [hashtags_2.append(j.lower()) for j in tweet.split() if j[0] == '#']
        hashtags.append(hashtags_2)
        
    df['hashtags'] = hashtags
    df['hashtags'] = df['hashtags'].apply(lambda hashtags: hashtags if len(hashtags) != 0 else np.nan)

    return df


### END FUNCTION