def demonstrate_conditionals():
    # A bit messy, as requested
    print('--- Conditionals Demo ---')
    a, b, c = 10, 20, "hello"
    if a > 5: print("a is big")
    
    if b < 10:
        print("b is small")
    else:
        print("b is not small")
        
    if c == "world":
        print("c is world")
    elif c == "hello": print("c is hello")
    else: print("c is something else")

def demonstrate_loops():
    print('\n--- Loops Demo ---')
    # for loop
    for i in range(5):
        print('for loop:', i)

    # while loop
    x = 0
    while x < 5:
        print('while loop:', x)
        x = x + 1

# Runs the demonstration functions
if __name__ == "__main__":
    demonstrate_conditionals()
    demonstrate_loops()