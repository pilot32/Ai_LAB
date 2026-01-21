def set_creation_and_add():
    print("--- Sets ---")
    s = {1, 2, 3, 2} # duplicates ignored
    print("Original set:", s, "Length:", len(s))
    
    s2 = {1, "hello", 3.14}
    print("Mixed type set:", s2)
    
    s3 = set([1,2,3,4,5])
    print("Set from list:", s3)
    
    s.add(4)
    print("After add(4):", s)
    s.update({5, 6})
    print("After update({5, 6}):", s)
    
    # Access is checking membership
    print("Is 4 in s?", 4 in s) 

def set_remove_items():
    print("\n--- Set Removal ---")
    s = {1, 2, 3, 4, 5, 6}
    s.remove(6)
    print("After remove(6):", s)
    
    popped = s.pop() # removes an arbitrary item
    print("After pop():", s, "| Popped:", popped)
    
    s.discard(1)
    print("After discard(1):", s)
    s.discard(100) # no error if not found
    print("After discard(100):", s)
    
    s.clear()
    print("After clear():", s)
    # del s # deletes variable

def set_operations():
    print("\n--- Set Operations ---")
    setA = {1, 2, 3, 4}
    setB = {3, 4, 5, 6}
    print("Set A:", setA, "Set B:", setB)
    
    print("Union:", setA.union(setB))
    print("Intersection:", setA.intersection(setB))
    print("Difference (A-B):", setA.difference(setB))
    print("Symmetric Difference:", setA.symmetric_difference(setB))
    print("Is {1, 2} disjoint from B?", {1, 2}.isdisjoint(setB))

if __name__ == "__main__":
    set_creation_and_add()
    set_remove_items()
    set_operations()