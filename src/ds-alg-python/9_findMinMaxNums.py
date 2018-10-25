list1 , list2 = [1, 5, 29, 78, 81], [2, 5, 6, 100]
addList = list1+list2
print('list 1 = ', list1)
print('list 2 = ', list2)
print('result added lists: ', addList)

print('\n')

max_val_list1, max_val_list2  = max(list1), max(list2)
min_val_list1, min_val_list2  = min(list1), min(list2)
print('max val for list1 = {0}, and max val for list2 = {1} - using max()'.format(max_val_list1, max_val_list2))
print('min val for list1 = {0}, and min val for list2 = {1} - using min()'.format(min_val_list1, min_val_list2))

print('\n')

def check_max_nums_func(someList):
    max_num = 0

    for i in someList:
        if i == max_num:
            max_num = i
        elif i > max_num:
            max_num = i

    return max_num

result_max1 = check_max_nums_func(list1)
result_max2 = check_max_nums_func(list2)
print('max value of list1 = {0} - using custom function'.format(result_max1))
print('max value of list2 = {0} - using custom function'.format(result_max2))
