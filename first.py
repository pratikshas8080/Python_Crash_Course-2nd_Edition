# Initial Dictionary 
Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
        'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
        'B': {1: 'Geeks', 2: 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value 
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

# Deleting a Key  
# using pop() 
Dict.pop(5)
print("\nPopping specific element: ")
print(Dict)

# Deleting an arbitrary Key-value pair 
# using popitem() 
Dict.popitem()
print("\nPops an arbitrary key-value pair: ")
print(Dict)

# Deleting entire Dictionary 
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict) 