# Data structure snippets
def list_ex():
    # Ways to initialize a list
    my_empty_list = []
    my_non_empty_list = [1, 4, 9, 16, 25]

    print(my_empty_list)
    print(my_non_empty_list)

    # You can index and slice a list
    print(my_non_empty_list[0])   # Returns the first element
    print(my_non_empty_list[-1])  # Returns the last element 
    print(my_non_empty_list[-3:]) # Slicing returns a new list

    # Lists also support concatenation
    print(my_non_empty_list + [5, 6, 11, 13])

    # You can get the length of a list
    print(len(my_non_empty_list))

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters)
    # You can replace some values by slices
    letters[2:5] = ['C', 'D', 'E']
    print(letters)

    # Now remove them
    letters[2:5] = []
    print(letters)

    # Searching for values in a list
    search_list = ['harambe', 'was', 'an', 'inside', 'job']

    # Prints number of 'was' in the list
    print(search_list.count('was'))

    # Prints the index of 'harambe'
    print(search_list.index('harambe'))

    # Errors if not in list
#    print(search_list.index('justice'))


def dict_ex():
    # Ways to initialize a dictionary
    my_dict = {}

def tuple_ex():
    # Tuples are immutable lists. It can't be changed in any way once it's created
    # Ways to initialize a tuple
    my_tuple = ()

def set_ex():
    # Ways to initialize a set
    my_set = {1,2}

def counter_ex():
    # Ways to initialize a counter
    my_counter = Counter()



list_ex()
dict_ex()
tuple_ex()
set_ex()
