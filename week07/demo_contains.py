destinations = ['Alaska', 'Rangiroa', 'New Zeland', 'Vancouver']

def contains(some_list, target):
    found = False
    i = 0
    while i < len(some_list) and not found:
        found = some_list == target
        i = i + 1
    return found

def index_of(some_list, target):
    idx = -1
    i = 0
    while idx == -1 and i < len(some_list):
        if some_list[i] == target:
            idx=i
        i = i+1
    return idx

print(index_of(destinations, 'Rome'))
