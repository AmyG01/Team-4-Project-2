### START FUNCTION
def number_of_tweets_per_day(df):
    '''Calculates the number of tweets posted per day
    for a given dataframe.

    Args:
        df: Takes a pandas dataframe as input.

    Returns:
        no_of_tweets : A new dataframe, which reflects the date and the
        corresponding number of tweets for each date.

    Examples:
        >>>Tweet : @BongaDlulane Please send an email to mediades...
        |Date : 2019-11-29 12:50:54
                    @saucy_mamiie Pls log a call on 0860037566
                    | Date : 2019-11-29 12:46:53
                    @ArthurGodbeer Is the power restored as yet?
                    | Date : 2019-11-20 10:07:59

        Date : 2019-11-29 | no_of_tweets : 2
        Date : 2019-11-20 | no_of_tweets : 1
        '''

    final_date = []
    for date in df['Date']:
        final_date = final_date + [date[0:10]]
    df = df.drop('Date', 1)
    df['Date'] = final_date
    no_of_tweets = df[['Date', 'Tweets']].groupby('Date').count()
    return no_of_tweets

### END FUNCTION
