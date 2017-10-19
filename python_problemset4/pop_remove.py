#!/usr/bin/env python3

# Pop

values = [101,2,15,22,95,33,2,27,72,15,52]

print("Original\n", values, "\n")
value_pop = values.pop()
print("\nOriginal\n", values, "\nEdited\n", value_pop)

# Remove

values = [101,2,15,22,95,33,2,27,72,15,52]

print("Original\n", values)
value_remove = values.remove(101) # remove value matching 101 as example
print("\nOriginal\n", values, "\nEdited\n", value_remove)
