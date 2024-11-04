# Global variable
count = 10

def outer_function():
    # Enclosing variable for inner_function
    count = 20
    
    def inner_function():
        nonlocal count  # Refers to the variable in the enclosing scope (outer_function)
        count += 5
        print("Inside inner_function:", count)  # Should print 25

    print("Before calling inner_function:", count)  # Should print 20
    inner_function()
    print("After calling inner_function:", count)  # Should print 25

def global_update():
    global count  # Refers to the global variable
    count += 10

# Function calls
print("Initial global count:", count)  # Should print 10
outer_function()
print("Global count after calling outer_function:", count)  # Should still print 10

global_update()
print("Global count after calling global_update:", count)  # Should print 20
