### START FUNCTION
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
