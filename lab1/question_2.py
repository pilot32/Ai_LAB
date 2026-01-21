def tuple_creation_and_ops():
    print("--- Tuples ---")
    my_tup = (1, 2, 'a', 'b', 2)
    print("Original:", my_tup)
    print("Length:", len(my_tup))
    print("Duplicated:", my_tup * 2)
    # del my_tup # this would delete the tuple

def tuple_accessing():
    print("\n--- Tuple Accessing ---")
    my_tup = (1, 2, 'a', 'b', 'c', 'd')
    print("Element 0:", my_tup[0])
    print("Last Element:", my_tup[-1])
    print("Slice [1:4]:", my_tup[1:4])
    print("Is 'a' in tuple?", 'a' in my_tup)

def tuple_modification_indirect():
    print("\n--- Tuple Modification (via list) ---")
    my_tup = (1, 2, 3)
    temp_list = list(my_tup)
    temp_list.append(4)
    temp_list.remove(1)
    my_tup = tuple(temp_list)
    print("Modified tuple:", my_tup)

def tuple_looping_and_methods():
    print("\n--- Tuple Looping & Methods ---")
    my_tup = (1, 2, 'a', 'b', 2, 2)
    print("Looping:")
    for item in my_tup:
        print("  -", item)
    
    t2 = (10, 11)
    print("Joined:", my_tup + t2)
    print("Count of 2:", my_tup.count(2))
    print("Index of 'a':", my_tup.index('a'))

if __name__ == "__main__":
    tuple_creation_and_ops()
    tuple_accessing()
    tuple_modification_indirect()
    tuple_looping_and_methods()