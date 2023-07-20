
def bubble_sort(list_to_sort):
    swap_count = 0

    for j in range (0, len(list_to_sort) - 1):
        if list_to_sort[j] >= list_to_sort[j+1]:
            list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
            swap_count += 1
    
    if swap_count >= 1:
        swap_count = 0
        bubble_sort(list_to_sort)
    else:
        print(list_to_sort)


def configuration_function():
    list_to_sort = []

    length = int(input('How long would you like your list to be? '))

    if length <= 1:
        print('Length must be more than 1 to sort the list')
        configuration_function()
    
    for i in range (0, length):
        list_element = float(input('Enter the item you would like to add to the list: '))
        list_to_sort.append(list_element)
    
    bubble_sort(list_to_sort)



configuration_function()
