import numpy as np
import pandas as pd
#First function 
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
    sort_items = sorted(items)
    minimum = sort_items[0]
    maximum = sort_items[-1]
    # Calculating & Unpacking percentiles using Numpy
    x, y, z = np.percentile(items, [25, 50, 75])
    q1 = round(x, 2)
    med = round(y, 2)
    q3 = round(z, 2)

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
    mun_list = []
    for tweet in df['Tweets']:
        mun_list_2 = []
        [mun_list_2.append(mun_dict[i])for i in mun_dict if i in tweet.split()]
        mun_list.append(mun_list_2)

    df['municipality'] = mun_list
    df['municipality'] = df['municipality'].apply(
        lambda a: a
        if len(mun_list) != 0 else np.nan)

    hashtags = []
    for tweet in df['Tweets']:
        hashtags_2 = []
        [hashtags_2.append(j.lower()) for j in tweet.split() if j[0] == '#']
        hashtags.append(hashtags_2)
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