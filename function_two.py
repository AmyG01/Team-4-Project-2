"""A function which takes in a list of integers and returns a dictionary of the
the five number summary"""

### START FUNCTION
def five_num_summary(items):

    numbers = []
    for i in items :
        numbers.append(i)
    sort_numbers = sorted(numbers)
    minimum = sort_numbers[0]
    maximum = sort_numbers[-1]


    len_numbers = len(sort_numbers)
    index = (len_numbers - 1)//2
    if (len_numbers % 2 == 0):
        med = (sort_numbers[index] + sort_numbers[index+1])/2
        
    else:
        med = sort_numbers[index]

    q1_len = len(range(0,index))
    q1_range = (q1_len-1)//2
    if (q1_len+1) % 2 == 0:
        q1 = (sort_numbers[q1_range] + sort_numbers[(q1_range+1)])/2

    else:
        q1 = sort_numbers[q1_range]


    rev_sort_numbers = sort_numbers[::-1]                
    
    q3_len = len(range(0,index))
    q3_range = (q3_len-1)//2
    if (q3_len+1) % 2 == 0:
        q3 = (rev_sort_numbers[q3_range] + rev_sort_numbers[(q3_range+1)])/2

    else:
        q3 = rev_sort_numbers[q1_range]

    dict = {'max' : maximum, 'median' : med,'min' : minimum,  'q1' : q1 , 'q3' : q3}

    return dict

### END FUNCTION
  
