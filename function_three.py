"""A function that takes as input a list of these datetime strings
 and returns only the date in 'yyyy-mm-dd' format"""

### START FUNCTION
def date_parser(dates):

    final_list = []
    for list_01 in dates: 
        final_list = final_list + [list_01[0:10]]   
    
    
    return final_list

### END FUNCTION