### START FUNCTION
def extract_municipality_hashtags(df):

    '''First, on the left we create two columns i.e. municipality and hashtags.
        On the right we use the map feature which let you create a new column by
        mapping the dataframe column values with the dictionary keys of num_dict.
        Lastly, apply str.extract() to extract Regular expressions that matches # in the begining
    '''
    twitter_df['municipality'],  twitter_df['hashtags'] = twitter_df['Tweets'].map(mun_dict), twitter_df['Tweets'].str.extract(pat = '([#].)')

    return twitter_df

### END FUNCTION