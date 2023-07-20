
def selection_sort(list_to_sort):
    min_element = list_to_sort[0]
    min_position = 0

    for k in range (0, len(list_to_sort) - 1):
        for j in range (k, len(list_to_sort)):
            if list_to_sort[j] <= min_element:
                min_element = list_to_sort[j]
                min_position = j
        
        # print(list_to_sort)
        list_to_sort[k], list_to_sort[min_position] = list_to_sort[min_position], list_to_sort[k]
        # print(list_to_sort)
        min_element = list_to_sort[k+1]

    print(list_to_sort)

    
    
def configuration_function():
    list_to_sort = []

    length = int(input('How long would you like your list to be? '))

    if length <= 1:
        print('Length must be more than 1 to sort the list')
        configuration_function()
    
    for i in range (0, length):
        list_element = int(input('Enter the item you would like to add to the list: '))
        list_to_sort.append(list_element)
    
    selection_sort(list_to_sort)


configuration_function()