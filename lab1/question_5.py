def dict_create_access_update():
    print("--- Dictionaries ---")
    d = {"key1": "value1", "key2": 123, "name": "John"}
    print("Dict:", d)
    print("Access d['key1']:", d["key1"])
    
    d['key2'] = 456 # update
    print("Updated:", d)
    
    d['new_key'] = 'new value' # add
    print("Added:", d)
    print("Length:", len(d))

def dict_remove_and_copy():
    print("\n--- Dict Remove & Copy ---")
    d = {"key1": "value1", "key2": 123, "name": "John"}
    d.pop("key2")
    print("After pop('key2'):", d)
    
    d.popitem() # removes last inserted
    print("After popitem():", d)
    
    d_copy = d.copy()
    print("Copied dict:", d_copy)
    d_copy.clear()
    print("Cleared copy:", d_copy)
    # del d_copy

def dict_looping():
    print("\n--- Dict Looping ---")
    d = {"name": "Alice", "age": 30, "city": "New York"}
    print("Looping keys:")
    for k in d: print("  ", k)
    
    print("Looping values:")
    for v in d.values(): print("  ", v)
        
    print("Looping items:")
    for k, v in d.items(): print(f"  {k}: {v}")

def nested_dicts():
    print("\n--- Nested Dictionaries ---")
    nested_dict = {
        "child1" : { "name" : "Emil", "year" : 2004 },
        "child2" : { "name" : "Tobias", "year" : 2007 }
    }
    print("Nested:", nested_dict)
    print("Access child1 name:", nested_dict["child1"]["name"])
    
    print("Looping nested:")
    for parent_k, child_v in nested_dict.items():
        print(f"  {parent_k}: {child_v}")

if __name__ == "__main__":
    dict_create_access_update()
    dict_remove_and_copy()
    dict_looping()
    nested_dicts()