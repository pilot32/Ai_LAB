def list_creation_and_access():
    print("--- Lists (Arrays) ---")
    # Python's list is like an array
    my_list = [1, "two", 3.0]
    print("List:", my_list)
    print("Length:", len(my_list))
    print("Element 1:", my_list[1])

def list_looping():
    print("\n--- List Looping ---")
    my_list = [1, "two", 3.0]
    for x in my_list:
        print("  Item:", x)

def list_modification():
    print("\n--- List Modification ---")
    my_list = [1, "two", 3.0]
    print("Original:", my_list)
    my_list.append(4)
    print("After append(4):", my_list)
    popped = my_list.pop()
    print("After pop():", my_list, "| Popped:", popped)
    my_list.pop(0)
    print("After pop(0):", my_list)

if __name__ == "__main__":
    list_creation_and_access()
    list_looping()
    list_modification()