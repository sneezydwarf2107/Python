def get_List(grenze):
    my_list = list(range(2, grenze+1))
    return(my_list)

def calculation(my_list, grenze):

    for x in range(0, len(my_list)):
        
        if x >= len(my_list):
            break

        if my_list[x] != 0:
            term = my_list[x]
            for y in range(x+1, len(my_list)):

                if y >= len(my_list):
                    break


                if (my_list[y] % term) == 0:
                    my_list.pop(y)
                    

    return(my_list)