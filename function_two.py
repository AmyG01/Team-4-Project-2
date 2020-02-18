### START FUNCTION
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
  
