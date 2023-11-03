
lst = ["world", "is", "great", "world", "is", "world"]

def replace(lst, target, swap_value):
    for i in range(len(lst)):
        if lst[i] == target:
            lst[i] = swap_value
    return lst

replace(lst, "world", "python")
print(lst)