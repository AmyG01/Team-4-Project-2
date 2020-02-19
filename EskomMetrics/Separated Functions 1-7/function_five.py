### START FUNCTION
def number_of_tweets_per_day(df):

    """A function which calculates the number
    of tweets that were posted per day"""

    final_date = []
    for date in df['Date']:
        final_date = final_date + [date[0:10]]
    df = df.drop('Date', 1)
    df['Date'] = final_date
    no_of_tweets = df[['Date', 'Tweets']].groupby('Date').count()
    return no_of_tweets

### END FUNCTION
