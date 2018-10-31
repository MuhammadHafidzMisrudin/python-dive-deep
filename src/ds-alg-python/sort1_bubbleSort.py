def bubbleSort(alist):

    # Setting the range for comparison (first round: n, second round: n-1  and so on).
    for i in range(len(alist)-1, 0, -1):
        # print('i = {0}'.format(i))

        # Comparing within set range.
        for j in range(i):
            # print('j = {0}'.format(j))

            # Comparing element with its right side neighbor.
            if alist[j] > alist[j+1]:
                print('Comparison between elements = ', alist[j] > alist[j+1])
                print('{0} > {1} = {2}'.format(alist[j], alist[j+1], alist[j] > alist[j+1]))

                # Swapping elements.
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
                print('Elements have been swapped.')

    return alist



print(bubbleSort([5,1,2,3,9,8,0]))
