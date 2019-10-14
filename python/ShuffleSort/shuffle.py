import random

def shuffle_sort(list):
    count = 0
    while not _is_list_sorted(list):
        random.shuffle(list)
        count += 1
    
    return [list, count]

def _is_list_sorted(list):
    return all(list[i] <= list[i+1] for i in range(len(list) - 1))

if __name__ == '__main__':
    list = [3, 6, 2, 1]
    [result, count] = shuffle_sort(list)
    print(result)
    print('List sorted in ' + str(count) + ' shuffles')