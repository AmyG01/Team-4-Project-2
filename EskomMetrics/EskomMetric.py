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
    """A function which takes in a list of integers and returns a dictionary of the
    the five number summary"""

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
    """A function that takes as input a list of these datetime strings
    and returns only the date in 'yyyy-mm-dd' format"""
    final_date = []
    for date in dates:
        final_date = final_date + [date[0:10]]
    return final_date
    
### END FUNCTION
