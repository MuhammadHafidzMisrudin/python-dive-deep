def linear_search(array, key_data):

    foundData = 0
    found = False
    for i in range(len(array)):
        if array[i] == key_data:
            foundData = i
            found = True
    return foundData, found

def main():
    key = 110
    val, isFound =  linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], key)
    print('{0} is found at index {1}, {2}'.format(key, val, isFound))

if __name__ == '__main__':
    main()
