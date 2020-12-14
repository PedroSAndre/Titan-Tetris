def check_pair_in_list(listx,listy,x,y,size):
    in_list=False
    for i in range(size):
        if(x==listx[i] and y==listy[i]):
            in_list = True

    return in_list