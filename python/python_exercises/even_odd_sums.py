# a function that sums a list index based on their position 

def even_odd_sums(lst):
    even_position = sum(lst[0::2])
    odd_position = sum(lst[1::2])
    my_st=[]
    my_st.append(even_position)
    my_st.append(odd_position)
    return my_st

print(even_odd_sums((10, 20, 30, 40, 50, 60)))