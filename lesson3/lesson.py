


def analyze_list(my_list):
    lst_str = str(my_list)
    if not my_list:
        return None
    min = my_list[1]
    max = my_list[1]
    mem = 0
    newSet = set()
    for ls in my_list:
        mem += ls
        if my_list.count(ls) == 1:
            newSet.add(ls)
        if min > ls:
            min = ls
        if max < ls:
            max = ls
    mem = mem / len(my_list)
    my_milon={
        "set":newSet,
        "max":max,
        "min":min,
        "avg":mem
    }
    return my_milon

print(analyze_list([1,3,3,6,7]))

def filter_dict(d, threshold):
    my_list = []
    for key, value in d:
        if value > threshold:
            my_list.insert(key)
    return  my_list

dict={"a":1,"b": 3,"b": 3,"c": 6,"d": 7}
print(filter_dict(dict,5))