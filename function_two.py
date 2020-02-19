### START FUNCTION
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
  
