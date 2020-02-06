gauteng = [39660.0,
            36024.0,
            32127.0,
            39488.0,
            18422.0,
            23532.0,
            8842.0,
            37416.0,
            16156.0,
            18730.0,
            19261.0,
            25275.0]


def dictionary_of_metrics(items) :

    s = 0
    count = 0
    for value in items :
        s = s + value
        count = count + 1

        the_mean = round ( s / count , 2) #mean_calculation

    
    sorted_items = sorted(items)

    if count % 2 == 1:
        return sorted_items[round(count+1)/2-1]
    else:
            lower = sorted_items[round(count/2-1)  ]
            upper = sorted_items[round(count/2)]

    the_median = (lower + upper) / 2  #median_calculation
            

    sum_of_sqz = 0
    for j in items :
        sqrz_calc = (j - the_mean)**2
        sum_of_sqz = sum_of_sqz + sqrz_calc
            
    the_varience = sum_of_sqz / (count - 1)   #varience_calculation


    the_standard_dev = (the_varience)**(1/2)  #the_standard_deviation_calculation

    the_min = sorted_items[0] 

    the_max = sorted_items[count - 1]

    print({'mean':round(the_mean,2) ,'median':round(the_median,2) ,'varience':round(the_varience,2),'standard deviation':round(the_standard_dev,2),'min':round(the_min,2),'max':round(the_max,2)})

dictionary_of_metrics(gauteng)
