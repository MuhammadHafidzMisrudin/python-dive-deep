list1 , list2 = [1, 5, 29, 78, 81], [2, 5, 6, 100]
addList = list1+list2
print('result added lists: ', addList)


max_val_list1, max_val_list2  = max(list1), max(list2)
min_val_list1, min_val_list2  = min(list1), min(list2)
print('max val for list1 = {0}, and max val for list2 = {1}'.format(max_val_list1, max_val_list2))
print('min val for list1 = {0}, and min val for list2 = {1}'.format(min_val_list1, min_val_list2))
