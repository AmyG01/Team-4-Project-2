import numpy as np
import pandas as pd
### START OF FUNCTION ONE
def dictionary_of_metrics(items):
    total = 0
    count = 0
    for value in items:
        total = total + value
        count = count + 1
        the_mean = round(total / count, 2)
    sorted_items = sorted(items)
    if count % 2 == 1:
        the_median = sorted_items[int(round(count+1)/2-1)]
    else:
        lower_median = sorted_items[int(round(count/2-1))]
        upper_median = sorted_items[int(round(count/2))]
        the_median = (lower_median + upper_median) / 2
    sum_of_sqz = 0  # Calculate Sum of squares for Varience
    for j in items:
        sqrz_calc = (j - the_mean)**2
        sum_of_sqz = sum_of_sqz + sqrz_calc
    the_varience = round(sum_of_sqz / (count - 1), 2)
    the_standard_dev = round((the_varience)**(1/2), 2)
    the_min = sorted_items[0]
    the_max = sorted_items[count - 1]
    dict = {
        'mean': the_mean,
        'median': the_median,
        'var': the_varience,
        'std': the_standard_dev,
        'min': the_min,
        'max': the_max
        }
    return dict

### FUNCTION END

### START OF FUNCTION TWO
def five_num_summary(items):
    """
    Takes a list of numbers and firstly sort them and calculate a
    five number Summary(minimum,first-quartile,median,second-quartile,maximum)
    Arg :
        items : unordered items(float/int)

    Returns :
            dict : a dictionary with the calculated five number summary
    
    Example :
            >>>five_num_summary(gauteng) == {
                                            'max': 39660.0,
                                            'median': 24403.5,
                                            'min': 8842.0,
                                            'q1': 18653.0,
                                            'q3': 36372.0
                                            }
    """
    sort_items = sorted(items)
    # assign minimum and maximum values of the list
    minimum = sort_items[0]
    maximum = sort_items[-1]
    # Calculating & Unpacking percentiles using Numpy
    x, y, z = np.percentile(items, [25, 50, 75])
    q1 = round(x, 2)
    med = round(y, 2)
    q3 = round(z, 2)
    #storing the five number summary in a dictionary
    dict = {'max': maximum, 'median': med, 'min': minimum, 'q1': q1, 'q3': q3}

    return dict

### END FUNCTION

### START OF FUNCTION THREE
def date_parser(dates):
    """
    Convert an input list of dates from the format of 'yyyy-mm-dd' and
    'hh:mm:ss',to an output date of the format 'yyyy-mm-dd'

    Arg :
        dates : List of strings where each element(date)
        is in the format 'yyyy-mm-dd' and 'hh:mm:ss'

    Returns :
        final_date : A new list of strings where each element(date)
        on the list contains only the date in the 'yyyy-mm-dd'
        format

    Examples :
        >>>date_parser(['2019-11-29 12:50:54' ,'2017-02-04 12:46:53'
        , '1994-07-14 12:33:36' ] )
        ['2019-11-29','2017-02-04','1994-07-14']
    """
    final_date = []
    for date in dates:
        final_date = final_date + [date[0:10]]
    return final_date

### END FUNCTION

### START OF FUNCTION FOUR
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

### START OF FUNCTION FIVE
def number_of_tweets_per_day(df):  
    final_date = []
    for date in df['Date']:
        final_date = final_date + [date[0:10]]
    df = df.drop('Date', 1)
    df['Date'] = final_date
    no_of_tweets = df[['Date', 'Tweets']].groupby('Date').count()
    return no_of_tweets

### END FUNCTION

### START OF FUNCTION SIX
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

### START OF FUNCTION SEVEN
def stop_words_remover(df):
    """A function which removes english stop words from a tweet"""
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
