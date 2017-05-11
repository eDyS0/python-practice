"""
Write a function remove_duplicates that takes in a list
and removes elements of the list that are the same.
"""

def remove_duplicates(dup):
    clean_list = []
    for nb in dup:
        if nb not in clean_list:
            clean_list.append(nb)
    return clean_list

#remove_duplicates([1,1,2,2])
#[1, 2]
