
def alphabet_sort(list_to_sort):
    sorted_list = sorted(list_to_sort, key=str.lower)
    print('The sorted list is: ', sorted_list)



def configuration_function():
    list_to_sort = []

    length = int(input('How long would you like your list to be? '))

    if length <= 1:
        print('Length must be more than 1 to sort the list')
        configuration_function()
    
    for i in range (0, length):
        list_element = str(input('Enter the item you would like to add to the list: '))
        list_to_sort.append(list_element)
    
    alphabet_sort(list_to_sort)





configuration_function()

