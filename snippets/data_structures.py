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


def dict_ex():
    # Ways to initialize a dictionary
    my_dict = {}

def tuple_ex():
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
