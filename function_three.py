### START FUNCTION
def date_parser(dates):

    """A function that takes as input a list of these datetime strings
    and returns only the date in 'yyyy-mm-dd' format"""

    final_date = []
    for date in dates:
        final_date = final_date + [date[0:10]]

    return final_date

### END FUNCTION
