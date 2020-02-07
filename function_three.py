### START FUNCTION
def date_parser(dates):
    # My idea is to convert this list into a string
    # And then slice that string but my slice only
    # works only once, the rest of the dates are not formated
    #  and don't even appear
    # any ideas
    
    str1 = "" 
    for date in dates:
        for element in date:
            str1 += element
            slicer = slice(0, 10)
            str1 = str1[slicer]
        return str(str1)
d = ['2019-11-29 12:50:54',
    '2019-11-29 12:46:53',
    '2019-11-29 12:46:10']    
print(date_parser(d))

### END FUNCTION